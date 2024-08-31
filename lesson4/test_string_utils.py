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

"""start _with"""

@pytest.mark.parametrize("string, symbol, result", [

    ("свет", "с", True),
    ("", "", True),
    ("Минск", "М", True),
    ("Cinema ", "C", True),
    ("Ира-Аня", "И", True),
    ("123", '1', True),

    ("Иван", "и", False),
    ("мир", "М", False),
    ("", "@", False),
    ("зонт", "ж", False),
    ("животное", "з", False)
])
def test_starts_witch(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""

@pytest.mark.parametrize("string, symbol, result", [

    ("Мария", "я", True),
    ("СУП", "П", True),
    ("", "", True),
    ("кот ", "", True),
    ("87", "7", True),
    ("ОДИН-ДВа", "а", True),
    ("Илья1", "1", True),
    ("БаобаБ", "Б", True),
    
    ("лес", "п", False),
    ("тигр", "с", False),
    ("дверь", "Ь", False),
    ("", "*", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""

@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    ("значение с пробелом", False),
    ("123", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

"""list_to_string"""

@pytest.mark.parametrize("lst, joiner, result", [
   (["s", "o", "s"], ",", "s,o,s"),
   ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
   (["Первый", "Второй"], "-", "Первый-Второй"),
   (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
   (["в", "у", "з"], "", "вуз"),

   ([], None, ""),
   ([], ",", ""),
   ([], "кот", "") 
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result



    


