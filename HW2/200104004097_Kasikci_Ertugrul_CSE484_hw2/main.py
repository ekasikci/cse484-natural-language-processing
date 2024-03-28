import random
from split_syllables import split_into_syllables, split_into_sentences
from ngram_model import apply_good_turing_smoothing
from generate_sentence import generate_unigram_sentence, generate_bigram_sentence, generate_trigram_sentence
from perplexity import calculate_average_perplexity


with open('file_5ps.txt', 'r') as file1:
    file_5p = file1.read()

with open('file_95ps.txt', 'r') as file1:
    file_95p = file1.read()

end_tokens = {'.', '!', '?'}

syllables_list = split_into_syllables(file_95p)
sentence_list = split_into_sentences(file_5p, end_tokens)

# Initialize N-gram dictionaries
unigrams = {}
bigrams = {}
trigrams = {}

# Populate N-gram dictionaries
for i in range(len(syllables_list)):
    # Unigrams
    unigram = syllables_list[i]
    unigrams[unigram] = unigrams.get(unigram, 0) + 1

    # Bigrams
    if i < len(syllables_list) - 1:
        bigram = (syllables_list[i], syllables_list[i + 1])
        bigrams[bigram] = bigrams.get(bigram, 0) + 1

    # Trigrams
    if i < len(syllables_list) - 2:
        trigram = (syllables_list[i], syllables_list[i + 1], syllables_list[i + 2])
        trigrams[trigram] = trigrams.get(trigram, 0) + 1

print(f"""
Unigrams - Unique Syllables: {len(unigrams)}
Unigrams - Total Syllables: {sum(unigrams.values())}

Bigrams - Unique Syllable Pairs: {len(bigrams)}
Bigrams - Total Syllable Pairs: {sum(bigrams.values())}

Trigrams - Unique Syllable Triplets: {len(trigrams)}
Trigrams - Total Syllable Triplets: {sum(trigrams.values())}
""")

# Usage Example
adjusted_trigrams, zero_count_prob = apply_good_turing_smoothing(trigrams)

# Apply smoothing
adjusted_unigrams, unigram_zero_count_prob = apply_good_turing_smoothing(unigrams)
adjusted_bigrams, bigram_zero_count_prob = apply_good_turing_smoothing(bigrams)
adjusted_trigrams, trigram_zero_count_prob = apply_good_turing_smoothing(trigrams)


perplexity_unigram = calculate_average_perplexity(sentence_list, unigrams, 1, unigram_zero_count_prob)
perplexity_bigram = calculate_average_perplexity(sentence_list, bigrams, 2, bigram_zero_count_prob)
perplexity_trigram = calculate_average_perplexity(sentence_list, trigrams, 3, trigram_zero_count_prob)

print("Unigram Perplexity:", perplexity_unigram)
print("Bigram Perplexity:", perplexity_bigram)
print("Trigram Perplexity:", perplexity_trigram, "\n")

best_syllables = sorted(unigrams, key=unigrams.get, reverse=True)[:5]
start_syllable = random.choice(best_syllables)
start_pair = (random.choice(best_syllables), random.choice(best_syllables))

unigram_sentences = [generate_unigram_sentence(unigrams, end_tokens) for _ in range(5)]
bigram_sentences = [generate_bigram_sentence(bigrams, unigrams, end_tokens) for _ in range(5)]
trigram_sentences = [generate_trigram_sentence(trigrams, bigrams, unigrams, end_tokens) for _ in range(5)]

print("Unigram Sentences:")
for sentence in unigram_sentences:
    print(sentence)

print("\nBigram Sentences:")
for sentence in bigram_sentences:
    print(sentence)

print("\nTrigram Sentences:")
for sentence in trigram_sentences:
    print(sentence)
