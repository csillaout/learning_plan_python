import os
from collections import Counter
filename = os.path.join(os.path.dirname(__file__), 'sample.txt')

def read_file(filename):
    """Reads a file and returns its contents."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("The file was not found. Please check the file path")
        raise
    except Exception as e:
        print(f"An error occurred:{e}")
        raise

def word_frequency(text):
    """Calculates word frequency from the input text"""
    words = text.lower().split()
    clean_words=[word.strip(".,!?;:'\"()") for word in words]
    return Counter(clean_words)

def generate_report(counter):
    """Generates a frequency report from the counter object."""
    print("Word Frequency Report:")
    for word, count in counter.most_common():
         print(f"{word}:{count}")

if __name__ == "__main__":
    filename = "sample.txt"
    try:
        text = read_file(filename)
        frequencies = word_frequency(text)
        generate_report(frequencies)
    except Exception as e:
        print(f"Failed to analyze the file:{e}")


#run the program and print result in terminal: python3 word_frequency_analyzer.py
#run the test: pytest 