import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    DB_STRING = os.environ.get('DB_STRING')
    MAX_COMPLETION_TOKENS = os.environ.get('MAX_TOKENS', 4096)
    MAX_TOTAL_TOKENS = os.environ.get('MAX_TOKENS', 10000)
    SYSTEM_PROMPT = os.environ.get('SYSTEM_PROMPT', "You are friendly assistant, your name is Rick")
    OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-4o')