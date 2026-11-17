# Swearword Fixer

## Rules for work on this challenge:
* You may NOT use AI for anything related to this challenge.
* You may NOT share strategies with other students.
* You may NOT receive help from other students.
* You MAY look up information from the following: 
    - [Python docs](https://docs.python.org/3.13/)
    - [Real Python](https://realpython.com/)
    - [W3Schools Python Tutorial](https://www.w3schools.com/python/)
    - [CodeHS](https://codehs.com/)
* You MAY receive help from your teacher regarding getting pytest working correctly or any other technical issue related to getting python, GitHub, or VSCode working
    - *But I won't help you with the challenge itself.*

## TODO: Define the following function
### `swearword_fixer`: 
* **Goal**: replace all vowels in a four-letter word with corresponding symbols.
* **Rules**: [worth up to 3 pts.]
    - Receives 1 parameter (a string)
    - If the word has 4 letters, each vowel must be replace by a specific symbol (according to the vowel)
        + An `a`gets replaced with `@`
        + `e` with `#`
        + `i` with `!`
        + `o` with `*`
        + `u` with `^`
    - Either upper or lowercase vowels must be replaced with the proper symbol
* **Additional (Exceeds) Rules**: [worth 1pt]
    - Ignore any spaces before or after the word.
        + ` sell` and `sell ` and ` sell ` would all qualify as four letter words
        + However, the return value should remove any spaces before or after the words (` sell ` becomes `s#ll`)
    - Spaces inside the word do NOT count towards the 4 letters
        + `se ll` will be counted as a 4-letter word
        + The return value will keep any interior spaces, so `se ll` would return `s# ll`
    - Treat any other symbol or special character as a normal letter
        + `s#ll` or `s#11` both count as 4 letter words.
* **Expected inputs & Outputs**: 
    - `"bath"` -> `"b@th"`
    - `"able"` -> `"@bl#"`
    - `"crwd"` -> `"crwd"` (no vowels)
    - `"check"` -> `"check"` (5 letter word)

## Look fors in your grade
* [] You pass all proficiency tests (`swearword_fixer_proficient`)
* [] You use a variety of Python structures to solve the challenge
* [] You demonstrate multiple concepts related to the strings data type

***NOTE:** In the initial challenge, you received a score based on outcome #1. If that score was lower than a 3, this score can possible bring it back up to a 3 (depending on your success or not).*
