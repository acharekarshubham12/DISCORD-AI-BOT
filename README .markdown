# DISCORD-AI-BOT

## Overview
DISCORD-AI-BOT is a powerful and versatile Discord bot built using Python, leveraging the `discord.py` library and the Hugging Face `transformers` library. This bot integrates advanced natural language processing (NLP) capabilities, including sentiment analysis, named entity recognition (NER), question answering, text summarization, text generation, translation, and zero-shot classification. Designed for seamless integration into Discord servers, it provides an interactive command-based interface with support for GPU acceleration when available.

The bot is highly modular, utilizing a `ModelManager` class to dynamically load and manage pre-trained transformer models. It includes utilities for formatting output and handling Discord's message length limits, ensuring a robust user experience.

## Features
- **Sentiment Analysis**: Determines the sentiment of user-provided text.
- **Named Entity Recognition (NER)**: Identifies and extracts entities (e.g., names, locations) from text.
- **Question Answering**: Answers questions based on provided context.
- **Text Summarization**: Generates concise summaries of long text.
- **Text Generation**: Creates new text based on a given prompt.
- **Translation**: Translates English text to French.
- **Zero-Shot Classification**: Classifies text into predefined categories (e.g., news, sports).
- **GPU Support**: Utilizes CUDA if available for faster processing.
- **Customizable Commands**: Configurable via a `.env` file and `config.py`.

## Prerequisites
- **Python 3.8+**
- **Required Libraries**:
  - `discord.py`
  - `transformers`
  - `torch`
  - `asyncio`
  - `python-dotenv`
- **Discord Bot Token**: Obtain from the [Discord Developer Portal](https://discord.com/developers/applications).
- **GPU (Optional)**: NVIDIA GPU with CUDA support for accelerated model inference.

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/acharekarshubham12/DISCORD-AI-BOT.git
   cd DISCORD-AI-BOT
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
   - Create a `requirements.txt` file with:
     ```
     discord.py
     transformers
     torch
     asyncio
     python-dotenv
     ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Discord bot token:
     ```
     DISCORD_TOKEN=your_discord_bot_token_here
     ```
   - Customize `config/config.py` with your preferred `BOT_PREFIX` (e.g., `!`) and `BOT_STATUS` (e.g., "AI Assistant").

4. **Configure Models**:
   - Edit `config/config.py` to define `MODEL_CONFIG` with desired Hugging Face model names (e.g., `"bert-base-uncased"` for sentiment analysis).

5. **Run the Bot**:
   ```
   python bot.py
   ```

## Usage
- **Invite the Bot to Your Server**:
  - Go to the [Discord Developer Portal](https://discord.com/developers/applications), select your bot, and generate an OAuth2 URL with the `bot` scope and necessary permissions. Invite it to your server.
- **Available Commands**:
  - `!ping`: Check bot responsiveness (returns "Pong!").
  - `!analyze <text>`: Perform sentiment analysis on the provided text.
  - `!entities <text>`: Extract entities from the text.
  - `!summarize <text>`: Summarize the provided text.
  - `!answer context: <context> question: <question>`: Answer a question based on context.
  - `!generate <prompt>`: Generate text based on a prompt.
  - `!translate <text>`: Translate text to French.
  - `!classify <text>`: Classify text into categories (news, sports, etc.).
- **Example**:
  ```
  !analyze I love this movie!
  ```
  Output: `📝 Sentiment: positive (0.95)`

## File Structure
- `bot.py`: Main bot script with commands and event handlers.
- `config/config.py`: Configuration file for bot prefix, status, and model settings.
- `src/models.py`: `ModelManager` class for loading and managing transformer models.
- `src/utils.py`: Utility functions for formatting entities and splitting long messages.
- `.env`: Environment variables (e.g., Discord token).

## Contributing
We welcome contributions to enhance DISCORD-AI-BOT! Please fork the repository, create a feature branch, and submit a pull request with detailed changes. Ensure code adheres to PEP 8 standards and include tests where applicable.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support or inquiries, please contact [acharekarshubham12@gmail.com](mailto:acharekarshubham12@gmail.com).

## Acknowledgments
- Built with [discord.py](https://github.com/Rapptz/discord.py) and [Hugging Face Transformers](https://github.com/huggingface/transformers).
- Thanks to the open-source community for pre-trained models and libraries.
