from .repeated_word import repeated_word


def test_import():
    assert repeated_word


def test_repeated_word_with_repeats():
    """Test that a string with repeated words returns correct word."""
    s1 = 'dog cat dog cat'
    s2 = 'Dog, cat, dog, cat!'
    s3 = '1 dog, 2 dog, red dog, blue dog'
    assert repeated_word(s1) == 'dog'
    assert repeated_word(s2) == 'cat'
    assert repeated_word(s3) == 'dog'


def test_repeated_word_no_repeats():
    """Test that a string with no repeated words returns None."""
    s1 = 'dog cat pig whale'
    s2 = 'Dog, cat, dog, Cat!'
    s3 = '1 1 2 2 3 3'
    assert repeated_word(s1) == None
    assert repeated_word(s2) == None
    assert repeated_word(s3) == None
