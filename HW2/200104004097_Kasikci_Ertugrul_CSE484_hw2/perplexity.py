import math

def calculate_ngram_probability(ngram, ngram_model, zero_count_prob):
    return ngram_model.get(ngram, zero_count_prob)


def calculate_sentence_probability(sentence, ngram_model, n, zero_count_prob):
    probability = 1
    syllables = sentence.split()

    for i in range(len(syllables) - n + 1):
        ngram = tuple(syllables[i:i + n])
        probability *= calculate_ngram_probability(ngram, ngram_model, zero_count_prob)

    return probability


def calculate_perplexity(sentence, ngram_model, n, zero_count_prob):
    log_probability_sum = 0
    syllables = sentence.split()
    num_ngrams = len(syllables) - n + 1

    if num_ngrams <= 0:
        return float('inf')

    for i in range(num_ngrams):
        ngram = tuple(syllables[i:i + n])
        ngram_prob = calculate_ngram_probability(ngram, ngram_model, zero_count_prob)
        if ngram_prob <= 0:
            return float('inf')  # Return infinite perplexity for zero probability
        log_probability_sum += math.log(ngram_prob)

    average_log_probability = log_probability_sum / num_ngrams
    return math.exp(-average_log_probability)



def calculate_average_perplexity(sentences, ngram_model, n, zero_count_prob):
    total_perplexity = 0
    count = 0

    for sentence in sentences:
        sentence_perplexity = calculate_perplexity(sentence, ngram_model, n, zero_count_prob)
        if sentence_perplexity != float('inf'):  # To avoid infinite perplexity values
            total_perplexity += sentence_perplexity
            count += 1

    return total_perplexity / count if count > 0 else float('inf')

