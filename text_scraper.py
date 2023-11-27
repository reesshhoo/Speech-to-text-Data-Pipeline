import os
import num2words
from PyPDF2 import PdfReader
from string import punctuation

def convert_pdf_to_text(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(input_dir, file_name)
            output_text_file = f"{os.path.splitext(file_name)[0]}.txt"
            output_path = os.path.join(output_dir, output_text_file)

            with open(file_path, "rb") as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()

                # Convert text to lowercase
                text = text.lower()

                # Remove punctuation
                text = text.translate(str.maketrans('', '', punctuation))

                # Convert digits to words
                words = []
                for word in text.split():
                    if word.isdigit():
                        word = num2words.num2words(int(word))
                    words.append(word)

                cleaned_text = ' '.join(words)

                # Write cleaned text to a new file
                with open(output_path, "w", encoding='utf-8') as output_file:
                    output_file.write(cleaned_text[130:])

                print(f"Extracted text from {file_name} and saved as {output_text_file}")

# Replace with your input and output directories
input_directory = input("Enter path to input directory containing pdf files: ")
output_directory = input("Enter path to output directory: ")

convert_pdf_to_text(input_directory, output_directory)
