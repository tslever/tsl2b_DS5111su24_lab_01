'''
Module test_tokenizer, which has a function to test tokenizing text
'''


from fixtures import logger, quote_from_The_Raven
from tsl2b_DS5111su24_lab_01.word_processors import clean_text, tokenize


def test_tokenize(logger, quote_from_The_Raven):
    '''
    Given a string text_to_tokenize of text with words
    that is cleanish according to a restriction on using function tokenize,
    when I pass text_to_tokenize to tokenize,
    I should get a list of those words as return.
    The words should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        none

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from text

    Exceptions raised:
        AssertionError if actual list of words does not equal expected list of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing tokenizing text")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    expected_list_of_words = [
        "but",
        "the",
        "raven",
        "sitting",
        "lonely",
        "on",
        "the",
        "placid",
        "bust",
        "spoke",
        "only",
        "that",
        "one",
        "word",
        "as",
        "if",
        "his",
        "soul",
        "in",
        "that",
        "one",
        "word",
        "he",
        "did",
        "outpour"
    ]

    assert \
        actual_list_of_words == expected_list_of_words, \
        f"Given text {text_to_tokenize}, actual list of words is not equal to expected list of words."


def test_that_there_are_no_hyphens(logger, quote_from_The_Raven):
    '''
    Given a string quote_from_The_Raven of text with words
    that is cleanish according to a restriction on using function tokenize,
    when I pass quote_from_The_Raven to tokenize,
    I should get a list of those words as return.
    The words should consist of lowercase characters not in string.punctuation.

    Keyword arguments:
        none

    Return values:
        none

    Side effects:
        Compares actual and expected lists of words from text

    Exceptions raised:
        AssertionError if actual list of words does not equal expected list of words

    Restrictions on when this method can be called:
        none
    '''

    logger.info("Testing that there are no hyphens in quote from The Raven")

    text_to_tokenize = clean_text(quote_from_The_Raven)

    actual_list_of_words = tokenize(text_to_tokenize)

    there_are_no_hyphens = True
    for word in actual_list_of_words:
        if '-' in word:
            there_are_no_hyphens = False

    assert \
        there_are_no_hyphens, \
        f"Given text {quote_from_The_Raven}, there are no hyphens in the words in a cleaned version of this text."
