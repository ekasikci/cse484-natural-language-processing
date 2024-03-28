from filer_letters import keep_letters, filter_nonletters, translate_syllables
from parser import parse_text

file = open('wiki_00', 'r', encoding='utf-8')

file_100p = file.read()

# Filter URLs and other metadata
file_100p_filtered = filter_nonletters(file_100p)

# Remove non-Turkish characters and unnecessary symbols
file_100p_preprocessed = keep_letters(file_100p_filtered)

# Parse the text into syllables
file_100p_parsed = parse_text(file_100p_preprocessed)

file_100p_processed = translate_syllables(file_100p_parsed)

total_length = len(file_100p_processed)
split_point_95 = int(0.95 * total_length)

file_95p_parsed = file_100p_processed[:split_point_95]
file_5p_parsed = file_100p_processed[split_point_95:]

# Convert the list of syllables to a single string
file_95p_parsed_str = ' '.join(file_95p_parsed)
file_5p_parsed_str = ' '.join(file_5p_parsed)

with open('file_95p.txt', 'w', encoding='utf-8') as file:
    # Write the content to the file
    file.write(file_95p_parsed_str)


with open('file_5p.txt', 'w', encoding='utf-8') as file:
    # Write the content to the file
    file.write(file_5p_parsed_str)

file.close()