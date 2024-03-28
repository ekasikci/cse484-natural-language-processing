import re


def keep_letters(text):
    pattern = r'[^a-zA-ZçöşğıüÇÖŞĞIÜ,.!?; ]'
    return re.sub(pattern, '', text)


# Remove URLs and similar characters
def filter_nonletters(text):
    pattern = r'<doc id="[^"]*" url="[^"]*" title="[^"]*">'
    return re.sub(pattern, '', text)

# Translate Turkish characters to English
def translate_syllables(syllables):
    turkish_to_english = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o',
        'ş': 's', 'ü': 'u', 'Ç': 'C', 'Ğ': 'G',
        'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
    }

    processed_syllables = []
    for syllable in syllables:
        syllable = syllable.lower()

        for turkish_char, english_char in turkish_to_english.items():
            syllable = syllable.replace(turkish_char, english_char)

        processed_syllables.append(syllable)

    return processed_syllables
