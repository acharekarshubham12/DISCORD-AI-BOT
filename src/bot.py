import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Import from our modules
from config.config import BOT_PREFIX, BOT_STATUS
from src.models import ModelManager
from src.utils import format_entities, split_long_message

# --------------------------
# Bot Setup
# --------------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Initialize model manager
model_manager = ModelManager()

# --------------------------
# Events
# --------------------------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name=BOT_STATUS))
    await model_manager.preload_models()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    await ctx.send(f"Error: {error}")

# --------------------------
# Commands
# --------------------------
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def analyze(ctx, *, text=None):
    if not text:
        await ctx.send("Provide text for sentiment analysis. Usage: `!analyze Your text here`")
        return
    
    async with ctx.typing():
        result = await model_manager.process("sentiment", text)
    
    if result:
        await ctx.send(f"📝 Sentiment: {result[0]['label']} ({result[0]['score']:.2f})")
    else:
        await ctx.send("❌ Error processing sentiment analysis")

@bot.command()
async def entities(ctx, *, text=None):
    if not text:
        await ctx.send("Provide text for entity recognition. Usage: `!entities Your text here`")
        return
    
    async with ctx.typing():
        result = await model_manager.process("ner", text)
    
    if result:
        formatted = format_entities(result)
        for chunk in split_long_message(formatted):
            await ctx.send(chunk)
    else:
        await ctx.send("❌ Error processing entity recognition")

@bot.command()
async def summarize(ctx, *, text=None):
    if not text:
        await ctx.send("Provide text to summarize. Usage: `!summarize Your text here`")
        return
    
    async with ctx.typing():
        result = await model_manager.process("summarize", text, max_length=100, min_length=30)
    
    if result:
        await ctx.send(f"📝 Summary: {result[0]['summary_text']}")
    else:
        await ctx.send("❌ Error processing summarization")

@bot.command()
async def answer(ctx, *, input_text=None):
    if not input_text:
        await ctx.send("Provide context and question. Usage: `!answer context: Your context here question: Your question here`")
        return
    
    # Parse context and question from input
    if "context:" in input_text and "question:" in input_text:
        try:
            context_part, question_part = input_text.split("question:")
            context = context_part.replace("context:", "").strip()
            question = question_part.strip()
        except:
            await ctx.send("Please format your input as: `context: your context here question: your question here`")
            return
    else:
        await ctx.send("Please include both context and question in your input")
        return
    
    async with ctx.typing():
        result = await model_manager.process("qa", {"context": context, "question": question})
    
    if result:
        await ctx.send(f"💡 Answer: {result['answer']} (score: {result['score']:.2f})")
    else:
        await ctx.send("❌ Error processing question answering")

@bot.command()
async def generate(ctx, *, prompt=None):
    if not prompt:
        await ctx.send("Provide a prompt for text generation. Usage: `!generate Your prompt here`")
        return
    
    async with ctx.typing():
        result = await model_manager.process("text_gen", prompt, max_length=50)
    
    if result:
        await ctx.send(f"📝 Generated: {result[0]['generated_text']}")
    else:
        await ctx.send("❌ Error processing text generation")

@bot.command()
async def translate(ctx, *, text=None):
    if not text:
        await ctx.send("Provide text to translate. Usage: `!translate Your text here`")
        return
    
    async with ctx.typing():
        result = await model_manager.process("translate", text)
    
    if result:
        await ctx.send(f"🌐 Translation: {result[0]['translation_text']}")
    else:
        await ctx.send("❌ Error processing translation")

@bot.command()
async def classify(ctx, *, text=None):
    if not text:
        await ctx.send("Provide text to classify. Usage: `!classify Your text here`")
        return
    
    labels = ["news", "sports", "entertainment", "technology", "science", "politics"]
    async with ctx.typing():
        result = await model_manager.process("zero_shot", text, candidate_labels=labels)
    
    if result:
        await ctx.send(f"🏷️ Classification: {result['labels'][0]} (score: {result['scores'][0]:.2f})")
    else:
        await ctx.send("❌ Error processing classification")

# --------------------------
# Run Bot
# --------------------------
if __name__ == "__main__":
    bot.run(TOKEN)
