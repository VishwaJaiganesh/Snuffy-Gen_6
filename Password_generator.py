import random
import string
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Character sets
SIMILAR_CHARS = 'il1Lo0O'
AMBIGUOUS_CHARS = '{}[]()/\'"`~,;:.<>\\'
CHAR_SETS = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'digits': string.digits,
    'special': string.punctuation
}

def exclude_characters(char_set, exclude):
    """Exclude specified characters from a character set."""
    return ''.join(c for c in char_set if c not in exclude)

def prepare_char_sets(exclude_similar, exclude_ambiguous):
    """Prepare character sets based on exclusion preferences."""
    # Making a copy of the character sets so we don't mess up the originals
    char_sets = CHAR_SETS.copy()
    if exclude_similar:
        # Get rid of those confusing characters
        char_sets = {key: exclude_characters(value, SIMILAR_CHARS) for key, value in char_sets.items()}
    if exclude_ambiguous:
        # Remove ambiguous ones too
        char_sets['special'] = exclude_characters(char_sets['special'], AMBIGUOUS_CHARS)
    return char_sets

