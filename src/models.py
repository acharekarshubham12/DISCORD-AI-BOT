import torch
from transformers import pipeline
import asyncio
from config.config import MODEL_CONFIG

class ModelManager:
    def __init__(self):
        self.models = {}
        self.device = 0 if torch.cuda.is_available() else -1
        print("Using GPU" if self.device == 0 else "Using CPU")
    
    async def preload_models(self):
        """Pre-load all models at startup"""
        print("Pre-loading all models...")
        for model_name in MODEL_CONFIG.keys():
            model = self._load_model(model_name)
            if model:
                self.models[model_name] = model
                print(f"✓ {model_name} loaded successfully")
            else:
                print(f"✗ Failed to load {model_name}")
        print("All models loaded!")
    
    def _load_model(self, name):
        """Load a specific model by name"""
        try:
            config = MODEL_CONFIG[name]
            if name == "sentiment":
                return pipeline("sentiment-analysis", device=self.device)
            elif name == "ner":
                return pipeline("ner", model=config["model_name"], device=self.device)
            elif name == "qa":
                return pipeline("question-answering", model=config["model_name"], device=self.device)
            elif name == "summarize":
                return pipeline("summarization", model=config["model_name"], device=self.device)
            elif name == "text_gen":
                return pipeline("text-generation", model=config["model_name"], device=self.device)
            elif name == "translate":
                return pipeline("translation_en_to_fr", model=config["model_name"], device=self.device)
            elif name == "zero_shot":
                return pipeline("zero-shot-classification", model=config["model_name"], device=self.device)
        except Exception as e:
            print(f"Error loading model {name}: {e}")
            return None
    
    async def process(self, model_name, input_data, **kwargs):
        """Process input with the specified model"""
        if model_name not in self.models:
            self.models[model_name] = self._load_model(model_name)
            if not self.models[model_name]:
                return None
        
        try:
            if model_name == "qa":
                result = await asyncio.to_thread(self.models[model_name], **input_data)
            else:
                result = await asyncio.to_thread(self.models[model_name], input_data, **kwargs)
            return result
        except Exception as e:
            print(f"Error processing with {model_name}: {e}")
            return None
