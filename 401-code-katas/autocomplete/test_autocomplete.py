"""Tests for autocomplete class."""

import pytest

TEST_LIST = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
TEST_FILE = "test_word_list.txt"


@pytest.fixture
def auto():
    """Fixture with basic set of words."""
    from autocomplete import AutoCompleter
    return AutoCompleter(TEST_LIST)


@pytest.fixture
def auto_f():
    """Create AutoCompleter with test file."""
    from autocomplete import AutoCompleter
    return AutoCompleter(TEST_FILE)


def test_init_with_list():
    """Test Autocompleter can be initialized with a vocab list."""
    from autocomplete import AutoCompleter
    c = AutoCompleter(TEST_LIST)
    for word in TEST_LIST:
        assert c._container.contains(word) is True


def test_init_with_file():
    """Test initializing Autocompeter with file."""
    from autocomplete import AutoCompleter
    c = AutoCompleter(TEST_FILE)
    with open(TEST_FILE, 'r') as f:
            vocab = f.readlines()
    for word in vocab:
        assert c._container.contains(word.strip()) is True


def test_complete_me_with_small_word_list(auto):
    """Test complete me function with small word list."""
    assert auto.complete_me("fi") == ["fix", "fit", "fist", "finch"]


def test_complete_me_smaller_max_comp():
    """Test complete me with smaller max_completions."""
    from autocomplete import AutoCompleter
    c = AutoCompleter(TEST_LIST, 2)
    assert c.complete_me("fi") == ["fix", "fit"]


def test_complete_me_with_file(auto_f):
    """Test autocompleter initialize with test file."""
    assert auto_f.complete_me("aber") == ["aberdevine", "aberrance", "aberrancy", "aberrant"]
    assert auto_f.complete_me("aa") == ["aardvark", "aardwolf"]
