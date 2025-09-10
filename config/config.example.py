# Bot Configuration
BOT_PREFIX = "!"
BOT_STATUS = "Processing AI requests"

# Model Configuration
MODEL_CONFIG = {
    "sentiment": {
        "model_name": "sentiment-analysis",
        "display_name": "Sentiment Analysis"
    },
    "ner": {
        "model_name": "dslim/bert-base-NER",
        "display_name": "Named Entity Recognition"
    },
    "qa": {
        "model_name": "distilbert-base-cased-distilled-squad",
        "display_name": "Question Answering"
    },
    "summarize": {
        "model_name": "sshleifer/distilbart-cnn-12-6",
        "display_name": "Text Summarization"
    },
    "text_gen": {
        "model_name": "distilgpt2",
        "display_name": "Text Generation"
    },
    "translate": {
        "model_name": "Helsinki-NLP/opus-mt-en-fr",
        "display_name": "Translation"
    },
    "zero_shot": {
        "model_name": "typeform/distilbert-base-uncased-mnli",
        "display_name": "Zero-Shot Classification"
    }
}

# Response Settings
MAX_MESSAGE_LENGTH = 2000
