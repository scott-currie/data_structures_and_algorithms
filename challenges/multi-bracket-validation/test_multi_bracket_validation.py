from multi_bracket_validation import multi_bracket_validation
import pytest


def test_mbv_empty_string_returns_true():
    """Test function accepts empty string and returns True."""
    input_str = ''
    assert multi_bracket_validation(input_str) is True


def test_mbv_rejects_non_string():
    """Test an exception is raised and handled if input is not str."""
    input_str = 9
    with pytest.raises(TypeError):
        multi_bracket_validation(input_str)


def test_mbv_various_cases():
    """Test various input strings against cases provided in challenge spec."""
    i = (('{}', True),
         ('{}(){}', True),
         ('()[[Extra Characters]]', True),
         ('(){}[[]]', True),
         ('{}{Code}[Fellows](())', True),
         ('[({}]', False),
         ('(](', False),
         ('{(})', False))
    for input_str, expected in i:
        assert multi_bracket_validation(input_str) is expected
