from googletrans import Translator

# Ensure the googletrans library is installed using:
# pip install googletrans==4.0.0-rc1

def fix_srt(input_file):
    """
    Standardizes an SRT file by ensuring proper formatting of subtitles.
    This function reads the input SRT file, processes its content, and ensures that
    subtitles are properly formatted with counters, timestamps, and text.

    Args:
        input_file (str): Path to the input SRT file.

    Returns:
        str: The standardized subtitle text.
    """
    # Open and read the input SRT file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    standardized_lines = []  # List to store the standardized subtitle lines
    counter = 1  # Counter for subtitle numbering
    i = 0  # Index for iterating through the lines

    # Process each line in the SRT file
    while i < len(lines):
        line = lines[i].strip()  # Remove leading/trailing whitespace from the line

        # If the line is empty, it is ignored
        if not line:
            i += 1
            continue

        # If the line contains a timestamp (indicated by '-->')
        if '-->' in line:
            time_line = line  # Store the timestamp line
            i += 1  # Move to the next line

            # Collect all subtitle text lines until an empty line is encountered
            subtitle_lines = []
            while i < len(lines) and lines[i].strip():
                subtitle_lines.append(lines[i].strip())
                i += 1

            # If subtitle text exists, add it to the standardized output
            if subtitle_lines:
                standardized_lines.append(str(counter))  # Add the subtitle counter
                counter += 1  # Increment the counter
                standardized_lines.append(time_line)  # Add the timestamp
                standardized_lines.extend(subtitle_lines)  # Add the subtitle text
                standardized_lines.append('')  # Add an empty line to separate subtitles
        else:
            # If the line is a counter (a digit), ignore it and move to the next line
            if line.isdigit():
                # The counter is ignored, and the next line is processed
                i += 1
            else:
                # If the line is subtitle text, it is added as part of the previous subtitle
                standardized_lines.append(line)
                i += 1

    Output = '\n'.join(standardized_lines)
    
    # Save the standardized subtitle to a new file
    with open("0001-standardized_subtitle.srt", 'w', encoding='utf-8') as file:
        file.write(Output)

    print(f"The standardized subtitle text has been created.\n")
    return Output

def convert_to_singleLine(input_Text):
    """
    Processes a multi-line text by splitting its content into sections, formatting them,
    and returning the formatted output as a single string.

    Args:
        input_Text (str): The input text to be processed.

    Returns:
        str: The formatted text as a single string.
    """
    # Split the content into sections based on double newlines
    sections = input_Text.split("\n\n")

    # Remove leading and trailing whitespace from each section
    sections = [section.strip() for section in sections]

    # Create a nested list to store formatted sections
    formatted_sections = []
    for section in sections:
        lines = section.split("\n")  # Split the section into individual lines
        if len(lines) >= 3:  # Only process sections with more than 3 lines
            formatted_section = [
                lines[0],  # First line (e.g., a title or identifier)
                lines[1],  # Second line (e.g., a subtitle or metadata)
                " ".join(lines[2:])  # Combine remaining lines into a single string
            ]
            formatted_sections.append(formatted_section)

    # Convert the formatted sections into a single string
    output_text = ""
    for section in formatted_sections:
        for line in section:
            output_text += line + "\n"  # Add each line of the section
        output_text += "\n"  # Add an empty line between sections

    # Save the single-line subtitle to a new file
    with open("0002-SingleLineSrt.srt", 'w', encoding='utf-8') as file:
        file.write(output_text)
    print(f"The single line subtitle text has been created.\n")
    return output_text.strip()  # Remove the trailing newline

def process_single_line_srt(single_line_srt):
    """
    Processes single-line SRT text to extract and format sections.
    This function extracts the third cell (subtitle text) from each section
    and saves it to a separate file.

    Args:
        single_line_srt (str): The single-line SRT text.

    Returns:
        str: The processed text containing only the third cells of each section.
    """
    # Split the input text into sections based on double newlines
    sections = single_line_srt.split("\n\n")

    # Strip each section of leading and trailing whitespace
    sections = [section.strip() for section in sections]

    # Create a nested list to store sections as nested lists
    nested_list = []
    for section in sections:
        lines = section.split("\n")  # Split the section into lines
        if len(lines) >= 3:  # Only process sections with at least 3 lines
            cell = [
                lines[0],  # First line (subtitle counter)
                lines[1],  # Second line (timestamp)
                " ".join(lines[2:])  # Third line (combined subtitle text)
            ]
            nested_list.append(cell)

    # Replace the first cell of each section with a sequential number
    for index, section in enumerate(nested_list, start=1):
        section[0] = str(index)

    # Save the third cells (subtitle text) to a new file
    with open("0003-third_cells.txt", "w") as third_cells_file:
        for section in nested_list:
            third_cells_file.write(section[2] + "\n")

    # Prepare the output text (only the third cells)
    output_text = "\n".join([section[2] for section in nested_list])

    print("Third cells saved to 'third_cells.txt'")
    return output_text


def translate_english_to_persian(text):
    """
    Translates English text to Persian. If an error occurs, returns the original text.

    Args:
        text (str): The input English text.

    Returns:
        str: The translated Persian text or the original text if an error occurs.
    """
    try:
        # Create an instance of the Translator class
        translator = Translator()  # Create a Translator instance
        translated = translator.translate(text, src='en', dest='fa')  # Translate text
        return translated.text  # Return the translated text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return text  # Return the original text if translation fails

def split_sentence_by_percentages(sentence, percentages):
    """
    Splits a Persian sentence into parts based on given percentages.
    This function is used to divide a translated sentence into parts that match
    the original subtitle line lengths.

    Args:
        sentence (str): The input Persian sentence.
        percentages (list): A list of percentages (e.g., [45, 56]).

    Returns:
        list: A list containing the parts of the sentence.
    """
    total_length = len(sentence)  # Total length of the sentence
    words = sentence.split()  # Split the sentence into words
    parts = []  # List to store the parts of the sentence
    current_index = 0  # Index to track the current position in the sentence
    
    # Iterate through the percentages (ignoring the last one)
    for percent in percentages[:-1]:
        part_length = int(total_length * percent / 100)  # Calculate the length of the current part
        current_part = []  # List to store words for the current part
        current_part_length = 0  # Track the length of the current part
        
        # Add words to the current part until the length is reached
        while current_index < len(words):
            word = words[current_index]
            if current_part_length + len(word) + len(current_part) <= part_length:
                current_part.append(word)
                current_part_length += len(word)
                current_index += 1
            else:
                break
        
        parts.append(' '.join(current_part))  # Add the current part to the list
    
    # Add the remaining words as the final part
    remaining_words = words[current_index:]
    if remaining_words:
        parts.append(' '.join(remaining_words))
    
    return parts


def process_text_file(Text):
    """
    Processes a text file to extract sentences, map lines to sentences, and save results.
    This function processes the subtitle text, translates it, and splits it into parts
    based on the original line lengths.

    Args:
        Text (str): The input text.

    Returns:
        list: A list of translations for each sentence.
    """
    lines = Text.splitlines()  # Split the text into lines
    sentences = []  # List to store extracted sentences
    translations = []  # List to store translated sentences
    current_sentence = ""  # Temporary variable to build the current sentence
    line_to_sentence_mapping = {}  # Maps line numbers to sentence numbers
    line_to_length_mapping = {}  # Maps line numbers to their lengths
    current_line_numbers = []  # Temporary list to store line numbers for the current sentence
    current_line_lengths = []  # Temporary list to store line lengths for the current sentence

    # Process each line in the file
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()  # Remove extra spaces and empty lines
        if line:  # If the line is not empty
            current_sentence += line + " "  # Add the line to the current sentence
            current_line_numbers.append(line_number)  # Track the line number
            current_line_lengths.append(len(line))  # Track the line length

        # Check if the line ends with a sentence-ending punctuation mark
        if line.endswith('.') or line.endswith('?') or line.endswith('!') or line.endswith(']'):
            sentences.append(current_sentence.strip())  # Save the completed sentence

            # Map line numbers to the current sentence number
            for line_num in current_line_numbers:
                line_to_sentence_mapping[line_num] = len(sentences)

            # Map line numbers to their lengths
            for i, line_num in enumerate(current_line_numbers):
                line_to_length_mapping[line_num] = current_line_lengths[i]

            # Calculate percentages for splitting the translated sentence
            percentages = []
            for i in range(len(current_line_lengths)):
                percentages.append((current_line_lengths[i]*100//len(current_sentence))+1)
            print(current_sentence)
            current_sentence_translation = translate_english_to_persian(current_sentence)  # Translate the sentence
            result = split_sentence_by_percentages(current_sentence_translation, percentages)  # Split the translated sentence
            for i, part in enumerate(result, start=1):
                print(part)
                translations.append(part)
            # Reset for the next sentence
            current_sentence = ""
            current_line_numbers = []
            current_line_lengths = []

    # Handle any remaining sentence without ending punctuation
    if current_sentence:
        sentences.append(current_sentence.strip())
        for line_num in current_line_numbers:
            line_to_sentence_mapping[line_num] = len(sentences)

    # Save the extracted sentences to a file
    with open("0004-output_sentences_path.txt", 'w', encoding='utf-8') as output_file:
        for sentence in sentences:
            output_file.write(sentence + '\n')

    # Save the translations to a file
    with open('0005-translations.txt', 'w', encoding='utf-8') as output_file:
        for translation in translations:
            output_file.write(translation + '\n')

    # Save the line-to-sentence mapping to a file
    with open("0006-output_line_mapping_path.txt", 'w', encoding='utf-8') as mapping_file:
        for line_num, sentence_num in sorted(line_to_sentence_mapping.items()):
            mapping_file.write(f"{line_num}:{sentence_num}\n")

    # Save the line-to-length mapping to a file
    with open("0007-output_length_mapping_path.txt", 'w', encoding='utf-8') as mapping_file:
        for line_num, line_length in sorted(line_to_length_mapping.items()):
            mapping_file.write(f"{line_num}:{line_length}\n")

    return translations



def recreate_subtitle(input_Text,TranslationList):
    """
    Recreates the subtitle file using translated text.
    This function replaces the original subtitle text with the translated text
    and saves the final subtitle file.

    Args:
        input_Text (str): The input subtitle text.
        TranslationList (list): A list of translated sentences.
    """
    # Split the input text into sections based on double newlines
    sections = input_Text.split("\n\n")

    # Remove leading and trailing whitespace from each section
    sections = [section.strip() for section in sections]

    # Create a nested list to store formatted sections
    formatted_sections = []
    for section in sections:
        lines = section.split("\n")  # Split the section into lines
        if len(lines) >= 3:  # Only process sections with at least 3 lines
            formatted_section = [
                lines[0],  # First line (subtitle counter)
                lines[1],  # Second line (timestamp)
                TranslationList[int(lines[0])-1]  # Translated text
            ]
            formatted_sections.append(formatted_section)

    # Convert the formatted sections into a single string
    output_text = ""
    for section in formatted_sections:
        for line in section:
            output_text += line + "\n"
        output_text += "\n"

    # Save the final subtitle to a new file
    with open("0008-FinalSubtitle.srt", 'w', encoding='utf-8') as file:
        file.write(output_text)
    print(f"The final subtitle text has been created.\n")

# Example usage
input_srt = 'lecture0-1.srt'  # Input file name
standardized_subtitle = fix_srt(input_srt)  # Standardize the SRT file
SingleLineSrt = convert_to_singleLine(standardized_subtitle)  # Convert to single-line format
ProcessedLines = process_single_line_srt(SingleLineSrt)  # Process single-line SRT
TranslationList = process_text_file(ProcessedLines)  # Translate and process text
recreate_subtitle(SingleLineSrt,TranslationList)  # Recreate the subtitle with translations