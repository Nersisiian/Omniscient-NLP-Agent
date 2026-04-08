import asyncio
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from core.logger import logger
from core.config import config

tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL)
model = AutoModelForCausalLM.from_pretrained(config.LLM_MODEL)
llm_pipeline = pipeline('text-generation', model=model, tokenizer=tokenizer)

async def generate_response(query: str, context: list):
    prompt = f"Context: {' '.join(context)}\nQuestion: {query}"
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, llm_pipeline, prompt)
    logger.info(f"Generated response for query: {query}")
    return result[0]['generated_text']