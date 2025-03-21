# SRT Subtitle Processing and Translation Tool

This Python script processes and translates SRT subtitle files. It standardizes the subtitle format, converts multi-line subtitles into single-line format, translates the text from English to Persian, and recreates the subtitle file with the translated text. The tool is designed to handle subtitles for educational content, such as lecture videos.

## Input File

The input file for this tool is an SRT subtitle file. For example:

**Input File Name:** `lecture0-1.srt`

**Description:** This file contains the subtitles for Week 0 of the CS50 Introduction to Computer Science 2025 course by David Malan.

## Output Files

The script generates the following output files:

1. **`0001-standardized_subtitle.srt`**

   **Description:** The standardized version of the input SRT file. This file ensures proper formatting of subtitles with counters, timestamps, and text.

2. **`0002-SingleLineSrt.srt`**

   **Description:** The subtitle file converted into a single-line format. Multi-line subtitle text is combined into a single line for easier processing.

3. **`0003-third_cells.txt`**

   **Description:** A text file containing only the third cells (subtitle text) from each section of the single-line SRT file.

4. **`0004-output_sentences_path.txt`**

   **Description:** A text file containing all extracted sentences from the subtitle text.

5. **`0005-translations.txt`**

   **Description:** A text file containing the translated Persian text for each sentence.

6. **`0006-output_line_mapping_path.txt`**

   **Description:** A mapping file that links line numbers to sentence numbers in the extracted sentences.

7. **`0007-output_length_mapping_path.txt`**

   **Description:** A mapping file that links line numbers to their lengths in the extracted sentences.

8. **`0008-FinalSubtitle.srt`**

   **Description:** The final subtitle file with the translated Persian text. This file is ready for use with the lecture video.

## How It Works

1. **Standardization:** The script reads the input SRT file (`lecture0-1.srt`) and ensures proper formatting of subtitles.
2. **Single-Line Conversion:** Multi-line subtitle text is converted into a single-line format.
3. **Text Extraction:** The third cells (subtitle text) are extracted and saved for translation.
4. **Translation:** The extracted text is translated from English to Persian using the Google Translate API.
5. **Recreation:** The final subtitle file is recreated with the translated text.

## Usage

1. Clone this repository to your local machine:

   `git clone https://github.com/Mehranism/Persian_srt-subtitle-translator.git`

2. Install the required Python library:

   `pip install googletrans==4.0.0-rc1`

3. Place your input SRT file (`lecture0-1.srt`) in the project directory.

4. Run the script:

   `python3 Persian_srt-subtitle-translator`

5. Check the output files in the project directory.

## Example Input

The input file `lecture0-1.srt` contains subtitles for Week 0 of the CS50 Introduction to Computer Science 2025 course by David Malan. Here is an example of the input format:

1  
00:00:00,000 --> 00:00:02,000  
Welcome to CS50!  

2  
00:00:02,000 --> 00:00:05,000  
This is Week 0, where we introduce you to the world of computer science.  

## Example Output

The script generates the following output files:

- **`0001-standardized_subtitle.srt`:** Standardized version of the input SRT file.
- **`0002-SingleLineSrt.srt`:** Single-line format of the subtitles.
- **`0003-third_cells.txt`:** Extracted subtitle text.
- **`0004-output_sentences_path.txt`:** Extracted sentences.
- **`0005-translations.txt`:** Translated Persian text.
- **`0006-output_line_mapping_path.txt`:** Line-to-sentence mapping.
- **`0007-output_length_mapping_path.txt`:** Line-to-length mapping.
- **`0008-FinalSubtitle.srt`:** Final subtitle file with translated text.

## Dependencies

- Python 3.x
- `googletrans==4.0.0-rc1`

## License

This project is licensed under the MIT License. See the LICENSE file for details.
