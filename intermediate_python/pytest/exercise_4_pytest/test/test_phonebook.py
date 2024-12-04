from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    "Provieds an empty Phonebook"
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"

def test_conatins_all_names(phonebook):
    phonebook.add("Bob", "12345")
    assert phonebook.all_names() == {"Bob"}

def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")

def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "01234")
    assert phonebook.is_consistent()

def test_inconsistent_with_duplicate_entries(phonebook):
     phonebook.add("Bob", "12345")
     phonebook.add("Sue", "12345")
     assert not phonebook.is_consistent()

def test_inconsistent_with_duplicate_prefix(phonebook):
     phonebook.add("Bob", "12345")
     phonebook.add("Sue", "123")
     assert not phonebook.is_consistent()

@pytest.mark.parametrize("entry1, entry2, is_consistent", [ 
    (("Bob", "12345"), ("Anna", "01234"), True),
      (("Bob", "12345"), ("Sue", "12345"), False),
      (("Bob", "12345"), ("Sue", "123"), False),]
)
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent
# different from unit testing. 
#Unit testing steps:
#1. Inherit a TestCase class
#2. Test case naming convention
#Inherited assertEqual method

#Pytest
#1. Test case naming convention
#Built-in assert function