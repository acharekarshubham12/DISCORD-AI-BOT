# Discord AI Bot 🤖

A powerful Discord bot that uses Hugging Face transformers for various NLP tasks.

## Features
-  Sentiment Analysis
-  Named Entity Recognition
-  Text Summarization
-  Question Answering
-  Text Generation
-  Translation (English to French)
-  Zero-Shot Classification

## Setup
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Discord token
4. Run: `python src/bot.py`

## Commands
- `!ping` - Check if bot is responsive
- `!analyze <text>` - Analyze sentiment of text
- `!entities <text>` - Extract named entities from text
- `!summarize <text>` - Summarize text
- `!answer context: <context> question: <question>` - Answer questions based on context
- `!generate <prompt>` - Generate text from a prompt
- `!translate <text>` - Translate English to French
- `!classify <text>` - Classify text into categories
