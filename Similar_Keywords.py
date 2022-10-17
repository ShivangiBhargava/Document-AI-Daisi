# convert keywords to vector
def createKeywordsVectors(keyword, nlp):
    doc = nlp(keyword)  # convert to document object

    return doc.vector


# method to find cosine similarity
def cosineSimilarity(vect1, vect2):
    # return cosine distance
    return 1 - spatial.distance.cosine(vect1, vect2)


# method to find similar words
def getSimilarWords(keyword, nlp):
    similarity_list = []

    keyword_vector = createKeywordsVectors(keyword, nlp)

    for tokens in nlp.vocab:
        if (tokens.has_vector):
            if (tokens.is_lower):
                if (tokens.is_alpha):
                    similarity_list.append((tokens, cosineSimilarity(keyword_vector, tokens.vector)))

    similarity_list = sorted(similarity_list, key=lambda item: -item[1])
    similarity_list = similarity_list[:30]

    top_similar_words = [item[0].text for item in similarity_list]

    top_similar_words = top_similar_words[:3]
    top_similar_words.append(keyword)

    for token in nlp(keyword):
        top_similar_words.insert(0, token.lemma_)

    for words in top_similar_words:
        if words.endswith("s"):
            top_similar_words.append(words[0:len(words)-1])

    top_similar_words = list(set(top_similar_words))

    top_similar_words = [words for words in top_similar_words if enchant_dict.check(words) == True]

    return ", ".join(top_similar_words)

  
 keywords = ['label', 'package']
 similar_keywords = getSimilarWords(keywords, nlp)
