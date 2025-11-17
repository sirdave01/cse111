# running a test file for address.py
from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main St, Springfield, IL 62704") == "Springfield"
    assert extract_city("456 Elm St, Los Angeles, CA 90001") == "Los Angeles"
    assert extract_city("789 Oak St, New York, NY 10001") == "New York"
    assert extract_city("101 Pine St, Miami, FL 33101") == "Miami"
    assert extract_city("202 Maple St, Seattle, WA 98101") == "Seattle"

def test_extract_state():
    assert extract_state("123 Main St, Springfield, IL 62704") == "IL"
    assert extract_state("456 Elm St, Los Angeles, CA 90001") == "CA"
    assert extract_state("789 Oak St, New York, NY 10001") == "NY"
    assert extract_state("101 Pine St, Miami, FL 33101") == "FL"
    assert extract_state("202 Maple St, Seattle, WA 98101") == "WA"

def test_extract_zipcode():
    assert extract_zipcode("123 Main St, Springfield, IL 62704") == "62704"
    assert extract_zipcode("456 Elm St, Los Angeles, CA 90001") == "90001"
    assert extract_zipcode("789 Oak St, New York, NY 10001") == "10001"
    assert extract_zipcode("101 Pine St, Miami, FL 33101") == "33101"
    assert extract_zipcode("202 Maple St, Seattle, WA 98101") == "98101"

# run the tests
pytest.main()
