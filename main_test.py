import pytest
from unittest.mock import patch

# This function simulates the betting input part of your game.
# In a real game, this would be integrated into a larger game loop.
def get_bet(current_points):
    """
    Simulates the betting input process, handling invalid inputs.
    Returns the valid bet amount.
    """
    while True:
        try:
            bet_input = input(f"You have {current_points} points. ")
            bet = float(bet_input)
            if bet <= 0 or not bet.is_integer():
                # For this simple example, we assume bets must be positive integers.
                # Adjust this logic based on your actual game rules (e.g., allowing floats, minimum bet).
                print("Invalid input. Please enter a positive whole number.")
                continue
            return int(bet) # Return as integer if it's a whole number
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


# Pytest functions to test the get_bet function

def test_valid_bet_input():
    """
    Tests that a valid integer bet is accepted.
    """
    with patch('builtins.input', side_effect=['1']):
        assert get_bet(10) == 1

def test_invalid_non_numeric_input():
    """
    Tests that non-numeric inputs are rejected with the correct message.
    """
    # We expect 'Invalid input. Please enter a numerical value.' to be printed.
    # We patch print to capture its output and assert on it.
    with patch('builtins.input', side_effect=['ten', '1']), \
         patch('builtins.print') as mock_print:
        get_bet(10)
        # Check if the correct error message was printed for the 'ten' input
        mock_print.assert_any_call("Invalid input. Please enter a numerical value.")

def test_invalid_float_input():
    """
    Tests that a non-integer numerical input (like 0.001) is rejected.
    """
    with patch('builtins.input', side_effect=['0.001', '1']), \
         patch('builtins.print') as mock_print:
        get_bet(10)
        # Check if the correct error message was printed for the '0.001' input
        mock_print.assert_any_call("Invalid input. Please enter a positive whole number.")

def test_zero_bet_input():
    """
    Tests that a zero bet input is rejected.
    """
    with patch('builtins.input', side_effect=['0', '1']), \
         patch('builtins.print') as mock_print:
        get_bet(10)
        mock_print.assert_any_call("Invalid input. Please enter a positive whole number.")

def test_negative_bet_input():
    """
    Tests that a negative bet input is rejected.
    """
    with patch('builtins.input', side_effect=['-5', '1']), \
         patch('builtins.print') as mock_print:
        get_bet(10)
        mock_print.assert_any_call("Invalid input. Please enter a positive whole number.")

def test_multiple_invalid_inputs_then_valid():
    """
    Tests that multiple invalid inputs are handled correctly before a valid one is accepted.
    """
    with patch('builtins.input', side_effect=['foo', '0.5', '0', '5']), \
         patch('builtins.print') as mock_print:
        assert get_bet(10) == 5
        # Verify that the correct error messages were printed for the invalid attempts
        mock_print.assert_any_call("Invalid input. Please enter a numerical value.")
        mock_print.assert_any_call("Invalid input. Please enter a positive whole number.")
        mock_print.assert_any_call("Invalid input. Please enter a positive whole number.")

