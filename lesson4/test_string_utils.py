import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
    """POSITIVE"""
    assert utils.capitalize("hi") == "Hi"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("789") == "789"
    """NEGATIVE"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("789тест") == "789тест"

"""trim"""

def test_trim():
    """POSITIVE"""
    assert utils.trim(" hi") == "hi"
    assert utils.trim(" hello world ") == "hello world "
    assert utils.trim(" RME ") == "RME "
    """NEGATIVE"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_invalid_input():
    with pytest.raises(AttributeError):
        utils.trim(None)

"""to_list"""

@pytest.mark.parametrize("string, delimiter, result", [
    # POSITIVE
    ("мандарин,яблоко,апельсин", ",", ["мандарин", "яблоко", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("a:b:c", ":", ["a", "b", "c"]),
    # NEGATIVE
    ("", ",", []),
    ("a b c", None, ["a b c"]),
])
def test_to_list(string, delimiter, result):
    if delimiter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimiter)
    assert res == result


"""contains"""

@pytest.mark.parametrize("string, symbol, result", [
    ("яблоко", "я", True),
    (" шуруп", "п", True),
    ("мир ", "р", True),
    ("диван-кровать", "-", True),
    ("789", "1", False),
    ("", "", False),
    ("Москва", "м", False),
    ("привет", "ё", False),
    ("кот", "@", False),
    ("", "а", False),
    ("12345", "h", False),
    ("hello", "", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

"""delete_symbol"""

@pytest.mark.parametrize("string, symbol, result", [
    ("09876", "76", "098"),
    ("Maша", "ша", "Ma"),  # Заменил "Ма" на "Ma", чтобы не было путаницы с латиницей и кириллицей
    ("!@#$%^&", "$%", "!@#^&"),
    ("Delete", "e", "Dlt"),
    ("", "", ""),
    ("12345", "CP", "12345"),
    ("Когда", "", "Когда")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

    


