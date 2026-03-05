from sklearn.metrics.pairwise import cosine_similarity

def rank_documents(query_vector, document_vectors):
    scores = cosine_similarity(query_vector, document_vectors)
    return scores.flatten()
