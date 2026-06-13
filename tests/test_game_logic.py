import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess


def test_correct_guess_shows_win_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_high_guess_shows_go_lower_message():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_low_guess_shows_go_higher_message():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_one_above_secret_shows_go_lower_message():
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_one_below_secret_shows_go_higher_message():
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
