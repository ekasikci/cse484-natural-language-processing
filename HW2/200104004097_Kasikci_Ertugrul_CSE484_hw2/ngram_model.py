def calculate_frequency_of_frequencies(ngram_dict):
    freq_of_freqs = {}
    for count in ngram_dict.values():
        freq_of_freqs[count] = freq_of_freqs.get(count, 0) + 1
    return freq_of_freqs

def apply_good_turing_smoothing(ngram_dict):
    freq_of_freqs = calculate_frequency_of_frequencies(ngram_dict)
    total_ngrams = sum(ngram_dict.values())

    adjusted_ngram_dict = {}
    for ngram, count in ngram_dict.items():
        next_count = freq_of_freqs.get(count + 1, 0)
        if next_count == 0:  # Handle the case where N_{r+1} is zero
            adjusted_count = count
        else:
            adjusted_count = (count + 1) * next_count / freq_of_freqs[count]
        adjusted_ngram_dict[ngram] = adjusted_count / total_ngrams  # Convert to probability

    # Handle zero counts
    if 1 in freq_of_freqs:
        zero_count_prob = freq_of_freqs[1] / total_ngrams
    else:
        zero_count_prob = 0

    return adjusted_ngram_dict, zero_count_prob