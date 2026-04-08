import os

class Config:
    VECTOR_DB_PATH = os.getenv('VECTOR_DB_PATH', './db/vector_db.faiss')
    LLM_MODEL = os.getenv('LLM_MODEL', 'tiiuae/falcon-7b-instruct')
    API_KEY = os.getenv('API_KEY', 'YOUR_API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

config = Config()