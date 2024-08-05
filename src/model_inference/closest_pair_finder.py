from sentence_transformers import util

def find_closest_cosine_pair(sentences, model):        
    # Encode all sentences
    embeddings = model.encode(sentences)

    # Compute cosine similarity between all pairs
    cosine_scores = util.pytorch_cos_sim(embeddings, embeddings)

    # Find the closest pair
    closest_pair = None
    highest_cosine_score = -1

    for i in range(len(cosine_scores) - 1):
        for j in range(i + 1, len(cosine_scores)):
            if cosine_scores[i][j] > highest_cosine_score:
                highest_cosine_score = cosine_scores[i][j]
                closest_pair = (sentences[i], sentences[j])
                
    # Return the closest pair and the highest cosine score
    return closest_pair, highest_cosine_score.item()