import re

def split_into_syllables(text):
    # Pattern to match any word or a single space (when surrounded by two spaces)
    pattern = r'\S+|\s(?=\s{2})'
    return re.findall(pattern, text)


def split_into_sentences(text, end_tokens):
    sentences = []
    current_sentence = []

    for syllable in split_into_syllables(text):
        current_sentence.append(syllable)
        if syllable in end_tokens:
            sentences.append(''.join(current_sentence).strip())
            current_sentence = []

    return sentences
