from string_utils import reverse_string, is_palindrome

def test_reverse_sting():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"

def is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False