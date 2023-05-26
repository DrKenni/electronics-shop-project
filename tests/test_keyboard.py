from src.keyboard import Keyboard
import pytest

"""Тесты класса Keyboard"""


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = 'UK'
