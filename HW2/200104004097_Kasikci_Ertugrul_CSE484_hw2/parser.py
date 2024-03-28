import re

consonant = ["b", "c", "d", "g", "ğ", "j", "l", "m", "n", "r", "v", "y", "z", "ç", "f", "h", "k", "p", "s", "ş", "t"]
vowel = ["a", "ı", "o", "u", "e", "i", "ö", "ü", "â"]


def isolate_punctuations(word):
    return re.sub(r'([,.!?; \n])', r' \1 ', word)


def parse_to_syllable(word):
    if len(word) == 0:
        return []

    if word in [" ", "\n", ",", ".", "!", "?", ";"]:
        return [word]

    word = word.lower()
    spell = list(word)
    vowel_count = sum([1 for i in spell if i in vowel])

    if len(word) in [1, 2] or (len(word) in [3, 4] and vowel_count == 1):
        return [word]

    if word[0] in consonant:
        if word[1] in consonant:
            if len(word) > 4 and word[4] in consonant:
                return [word[:4]] + parse_to_syllable(word[4:])
            else:
                return [word[:3]] + parse_to_syllable(word[3:])
        else:
            if len(word) > 4 and word[2] in consonant and word[3] in consonant:
                return [word[:3]] + parse_to_syllable(word[3:])
            else:
                return [word[:2]] + parse_to_syllable(word[2:])
    else:
        if word[1] in vowel:
            return [word[0]] + parse_to_syllable(word[1:])
        else:
            if len(word) > 2 and word[2] in vowel:
                return [word[:1]] + parse_to_syllable(word[1:])
            else:
                return [word[:2]] + parse_to_syllable(word[2:])

def parse_text(text):
    text_with_spaces = text.replace(" ", " <space> ")

    isolated_text = isolate_punctuations(text_with_spaces)

    words = isolated_text.split()
    syllables = []

    for word in words:
        if word == "<space>":
            syllables.append(" ")
        elif word in ["\n", ",", ".", "!", "?", ";"]:
            syllables.append(word)
        else:
            syllables.extend(parse_to_syllable(word))

    return syllables

text = "Merhaba, dünya!"
parsed_syllables = parse_text(text)
print(parsed_syllables)

