import pytest
from word_frequency_analyzer import word_frequency, read_file

def test_word_frequency():
    text = "Hello world! Hello everyone."
    result = word_frequency(text)
    assert result['hello'] == 2
    assert result['world'] == 1
    assert result['everyone'] == 1

def test_read_file(tmp_path):
    #create a temp file for testing
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("This is a test.")
    content = read_file(temp_file)
    assert content == "This is a test."