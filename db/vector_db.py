import faiss
import numpy as np

dimension = 768
index = faiss.IndexFlatL2(dimension)
document_embeddings = np.random.rand(100, dimension).astype('float32')
index.add(document_embeddings)