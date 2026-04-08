from fastapi import FastAPI
from pydantic import BaseModel
from api.llm_engine import generate_response
from api.rag_search import search_documents

app = FastAPI(title='Omniscient NLP Agent')

class Query(BaseModel):
    text: str

@app.post('/query')
async def query_nlp(query: Query):
    results = await search_documents(query.text)
    answer = await generate_response(query.text, results)
    return {'answer': answer, 'context': results}