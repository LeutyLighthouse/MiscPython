"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True iff puzzle is the same as view.

    >>>is_win('banana', 'banana')
    True
    >>>is_win('apple', 'apple')
    True
    >>>is_win('apple', 'a^^le')
    False
    >>>is_win('', '')
    True
    """
    # put the function body here
    return puzzle == view

def game_over(puzzle: str, view: str, selection: str) -> bool:
    """The first parameter represents a puzzle, the second represents its view,
    and the third represents the current selection (one of CONSONANT, VOWEL,
    SOLVE, or QUIT). 
    Return True if and only if the puzzle is the same as
    the view or the selection is QUIT.
    
    >>>game_over('apple', 'apple', SOLVE)
    True
    >>>game_over('apple', '^ppl^', QUIT)
    True
    >>>game_over('apple', '^^^le', SOLVE)
    False
    >>>game_over('banana', '^^^^^^', CONSONANT)
    False
    >>>game_over('banana', '^^^^^^', VOWEL)
    False
    >>>game_over('', '', SOLVE)
    True
    >>>game_over('', '', QUIT)
    True
    """
    return (is_win(puzzle, view)) or (selection == QUIT)
    
def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """The parameters represent a puzzle, its view, and a letter to evaluate. 
    Return True if and only if the letter is a consonant that appears in the 
    puzzle but not in its view.
    
    >>>bonus_letter('apple', 'a^^le', 'p')
    True
    >>>bonus_letter('apple', 'a^^le', 'P')
    True
    >>>bonus_letter('apple', '^pp^^', 'p')
    False
    >>>bonus_letter('apple', '^pp^^', 'j')
    False
    >>>bonus_letter('', '', '')
    False
    >>>bonus_letter('p', '', 'p')
    True
    >>>bonus_letter('p', '', 'P')
    True
    """
    return (letter.lower() in "qwrtypsdfghjklzxcvbnm") and (letter.lower()\
    in puzzle) and (letter.lower() not in view)

    
    
def update_letter_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """The first parameter represents a puzzle, the second 
    represents its view, the third represents the index of 
    the character to update, and the fourth represents the
    letter that has been guessed. 
    Return a single character string representing the next 
    view of the character at the given index. If the character
    at that index of the puzzle matches the guess, then return
    that character. Otherwise, return the character at that 
    index of the view.
    
    >>>update_letter_view('apple', '^^^^^', 0, 'a')
    'a'
    >>>update_letter_view('apple', 'a^^^^', 0, 'a')
    'a'
    >>>update_letter_view('apple', '^^^^^', 1, 'p')
    'p'
    >>>update_letter_view('apple', '^pp^^', 1, 'j')
    'p'
    >>>update_letter_view('apple', '^^^^^', 1, 'k')
    '^'
    >>>update_letter_view('apple', '^^^^^', 1, '')
    '^'
    """
    if puzzle[index] == guess:
        return puzzle[index]
    else:
        return view[index]
    
def calculate_score(c_score: int, numo_letters: int, c_or_v: str) -> int:
    """The first parameter represents the current score,
    the second represents the number of occurrences of a
    letter in the puzzle, and the third represents whether
    that letter is a CONSONANT or VOWEL (from the constants above). 
    Return the new score by adding CONSONANT_POINTS per 
    occurrence of the letter to the original score if the letter is 
    a consonant, or by deducting the VOWEL_PRICE from 
    the score if the letter is a vowel.
    
    >>>calculate_score(5, 3, CONSONANT)
    8
    >>>calculate_score(5, 3, VOWEL)
    4
    >>>calculate_score(0, 2, VOWEL)
    -1
    >>>calculate_score(0, 2, CONSONANT)
    2
    >>>calculate_score(0, 2, '')
    0
    """
        
    if c_or_v == CONSONANT:
        c_score = c_score + CONSONANT_POINTS * numo_letters
        return c_score
    elif c_or_v == VOWEL:
        c_score = c_score - VOWEL_PRICE
        return c_score
    else:
        return c_score
    
    
def next_player(c_player: str, numlast_choice: int) -> str:
    """The first parameter is the current player 
    (one of PLAYER_ONE or PLAYER_TWO) and the second 
    parameter is the number of occurrences in the puzzle 
    of the letter last chosen by the current player. 
    If and only if the number of occurrences is greater 
    than zero, the current player plays again. Return 
    the next player (one of PLAYER_ONE or PLAYER_TWO, 
    that wasn't playing before).
    
    >>>next_player(PLAYER_TWO, -2)
    'Player One'
    >>>next_player(PLAYER_ONE, 0)
    'Player Two'
    >>>next_player(PLAYER_TWO, 1)
    'Player Two'
    >>>next_player(PLAYER_ONE, 3)
    'Player One'
    """
    if numlast_choice > 0:
        return c_player
    else:
        if c_player == PLAYER_ONE:
            return PLAYER_TWO
        elif c_player == PLAYER_TWO:
            return PLAYER_ONE

    
    
    
    