from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "Assassins" in get_phrases("Assassins")
