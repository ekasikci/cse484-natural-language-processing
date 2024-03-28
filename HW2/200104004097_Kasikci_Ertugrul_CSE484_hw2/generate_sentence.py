import random

def generate_unigram_sentence(unigrams, end_tokens):
    top_syllables = sorted(unigrams, key=unigrams.get, reverse=True)[:5]
    start_syllable = random.choice(top_syllables)
    sentence = [start_syllable]

    while True:
        next_syllable = random.choices(list(unigrams.keys()), weights=unigrams.values(), k=1)[0]
        sentence.append(next_syllable)
        if next_syllable in end_tokens:
            break

    return ''.join(sentence)



def generate_bigram_sentence(bigrams, unigrams, end_tokens):
    top_syllables = sorted(unigrams, key=unigrams.get, reverse=True)[:5]
    start_syllable = random.choice(top_syllables)
    sentence = [start_syllable]

    while True:
        last_syllable = sentence[-1]
        candidates = [(b[1], bigrams[b]) for b in bigrams if b[0] == last_syllable]
        if not candidates:
            break
        next_syllable = random.choices([b[0] for b in candidates], weights=[c[1] for c in candidates], k=1)[0]
        sentence.append(next_syllable)
        if next_syllable in end_tokens:
            break

    return ''.join(sentence)




def generate_trigram_sentence(trigrams, bigrams, unigrams, end_tokens):
    top_syllables = sorted(unigrams, key=unigrams.get, reverse=True)[:5]
    start_pair = (random.choice(top_syllables), random.choice(top_syllables))
    sentence = list(start_pair)

    while True:
        if len(sentence) >= 2:
            last_two = tuple(sentence[-2:])
            trigram_candidates = [(t, trigrams[t]) for t in trigrams if t[:2] == last_two]
            if trigram_candidates:
                next_syllable = random.choices([t[0][2] for t in trigram_candidates], weights=[c[1] for c in trigram_candidates], k=1)[0]
                sentence.append(next_syllable)
                if next_syllable in end_tokens:
                    break
        else:
            break  # If sentence has less than 2 syllables, break the loop

        # Fallback to bigram model if no trigram candidates found
        last_syllable = sentence[-1]
        bigram_candidates = [(b, bigrams[b]) for b in bigrams if b[0] == last_syllable]
        if bigram_candidates:
            next_syllable = random.choices([b[0][1] for b in bigram_candidates], weights=[c[1] for c in bigram_candidates], k=1)[0]
            sentence.append(next_syllable)
            if next_syllable in end_tokens:
                break

    return ''.join(sentence)

