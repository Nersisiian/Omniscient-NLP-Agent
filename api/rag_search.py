import faiss
import numpy as np
from core.logger import logger

dimension = 768
index = faiss.IndexFlatL2(dimension)
document_embeddings = np.random.rand(100, dimension).astype('float32')
index.add(document_embeddings)

async def search_documents(query: str, top_k: int = 5):
    query_vector = np.random.rand(1, dimension).astype('float32')
    distances, indices = index.search(query_vector, top_k)
    results = [f'Document {i}' for i in indices[0]]
    logger.info(f"RAG search for query: {query} -> {results}")
    return results