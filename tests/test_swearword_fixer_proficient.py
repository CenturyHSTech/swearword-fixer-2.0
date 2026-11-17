import pytest
from swearword_fixer import swearword_fixer


@pytest.mark.parametrize("input_word,expected_output", [
    # Basic 4-letter words from examples
    ("word", "w*rd"),
    ("each", "#@ch"),
    
    # 4-letter words with single vowels
    ("bath", "b@th"),
    ("test", "t#st"),
    ("lift", "l!ft"),
    ("plot", "pl*t"),
    ("club", "cl^b"),
    
    # 4-letter words with multiple vowels
    ("able", "@bl#"),
    ("idea", "!d#@"),
    ("auto", "@^t*"),
    
    # 4-letter words with no vowels
    ("crwd", "crwd"),
    ("hymn", "hymn"),
    
    # Non 4-letter words (should remain unchanged)
    ("check", "check"),
    ("hi", "hi"),
    ("hello", "hello"),
    ("programming", "programming"),
])
def test_swearword_fixer_standard_cases(input_word, expected_output):
    """Test the swearword_fixer function with standard inputs."""
    result = swearword_fixer.swearword_fixer(input_word) 
    assert result == expected_output
