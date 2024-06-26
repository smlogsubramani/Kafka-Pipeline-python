from sentence_transformers import SentenceTransformer, util

query = "How many people live in London?"
docs = ["Around 9 Million people live in London", "London is known for its financial district"]

# Load the model
model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')

# Encode query and documents
query_emb = model.encode(query)
doc_emb = model.encode(docs)

# Compute cosine similarity between query and all document embeddings
scores = util.pytorch_cos_sim(query_emb, doc_emb)[0].tolist()

# Combine docs & scores
doc_score_pairs = list(zip(docs, scores))

# Sort by decreasing score
doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

# Output passages & scores
for doc, score in doc_score_pairs:
    print(score, doc)
