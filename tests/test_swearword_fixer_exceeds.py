import pytest
from swearword_fixer import swearword_fixer


@pytest.mark.parametrize("input_word,expected_output", [
    # Empty string
    ("", ""),
    
    # Single character
    ("a", "a"),
    ("b", "b"),
    
    # Two characters
    ("ab", "ab"),
    ("hi", "hi"),
    
    # Three characters
    ("cat", "cat"),
    ("the", "the"),
    
    # Five characters
    ("hello", "hello"),
    ("world", "world"),
    
    # All vowels (4-letter)
    ("aaaa", "@@@@"),
    ("ee ee", "## ##"),
    ("iiii", "!!!!"),
    ("oooo", "****"),
    ("uuuu", "^^^^"),
    ("aeio", "@#!*"),
    ("uoie", "^*!#"),
    
    # All consonants (4-letter)
    ("bcdf", "bcdf"),
    ("ghkl", "ghkl"),
    ("mnps", "mnps"),
    ("qrst", "qrst"),
    
    # Mixed case (if case sensitivity matters)
    ("Word", "W*rd"),
    ("WORD", "W*RD"),
    ("WoRd", "W*Rd"),
    ("EACH", "#@CH"),
    
    # Numbers in word (4 characters)
    ("w0rd", "w0rd"),
    ("w1rd", "w1rd"),
    ("te5t", "te5t"),
    ("1234", "1234"),
    
    # Special characters (4 characters)
    ("w@rd", "w@rd"),
    ("t#st", "t#st"),
    ("wo-d", "w*-d"),
    ("ea_h", "#@_h"),
    
    # Whitespace
    ("    ", ""),
    ("word ", "word"),
    (" word", "word"),
    ("wo rd", "w* rd"),
    (" W o r d", "W * r d"),
    
    # Y as vowel/consonant (typically not considered a vowel in basic exercises)
    ("myth", "myth"),
    ("hype", "hyp#"),
    ("your", "y*^r"),
    
    # Repeated vowels in 4-letter words
    ("aero", "@#r*"),
    ("ease", "#@s#"),
    ("ieee", "!###"),
    
    # Edge positions - vowels at start, end, middle
    ("area", "@r#@"),
    ("bare", "b@r#"),
    ("code", "c*d#"),
    
    # Unicode/Special characters (if supported)
    ("café", "c@fé"),  # Non-ASCII character
    ("naïv", "n@ïv"),  # With diacritic
    
    # Tabs and newlines (4 characters including whitespace)
    ("wo\td", "w*\td"),
    ("ea\nh", "#@\nh"),
])
def test_swearword_fixer_edge_cases(input_word, expected_output):
    """Test the swearword_fixer function with edge cases."""
    result = swearword_fixer.swearword_fixer(input_word)
    assert result == expected_output
