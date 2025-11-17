# writing the test file for names.py

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("Jane", "Doe") == "Doe; Jane"
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Olivier","Toussaint") == "Toussaint; Olivier"
    assert make_full_name("George","Washington") == "Washington; George"

    # for short names
    assert make_full_name("An", "Li") == "Li; An"

    # for long names
    assert make_full_name("Maximiliano", "Alexanderson") == "Alexanderson; Maximiliano"

    # for hyphenated names
    assert make_full_name("Anna-Marie", "Smith-Jones") == "Smith-Jones; Anna-Marie"
    assert make_full_name("Mary-Jane", "Watson-Parker") == "Watson-Parker; Mary-Jane"

# for the extract_family_name function
def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("Doe; Jane") == "Doe"
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Toussaint; Olivier") == "Toussaint"
    assert extract_family_name("Washington; George") == "Washington"

    # for short names
    assert extract_family_name("Li; An") == "Li"

    # for long names
    assert extract_family_name("Alexanderson; Maximiliano") == "Alexanderson"

    # for hyphenated names
    assert extract_family_name("Smith-Jones; Anna-Marie") == "Smith-Jones"

# for the extract_given_name function
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("Doe; Jane") == "Jane"
    assert extract_given_name("Toussaint; Marie") == "Marie"
    assert extract_given_name("Toussaint; Olivier") == "Olivier"
    assert extract_given_name("Washington; George") == "George"

    # for short names
    assert extract_given_name("Li; An") == "An"

    # for long names
    assert extract_given_name("Alexanderson; Maximiliano") == "Maximiliano"

    # for hyphenated names
    assert extract_given_name("Smith-Jones; Anna-Marie") == "Anna-Marie"
    assert extract_given_name("Watson-Parker; Mary-Jane") == "Mary-Jane"

# Run the tests
if __name__ == "__main__":
    pytest.main()