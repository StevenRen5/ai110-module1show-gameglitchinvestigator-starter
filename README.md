# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Describe the game's purpose: The game's purpose is to allow us to see what features are broken and to fix them.
- Detail which bugs you found: The difficulty level and the range were not aligned and the popup for go higher or lower is incorrect.
- [ ] Explain what fixes you applied: I correctly paired the difficulty level with the range, and I redefined the logical statements for whether the popup should say go higher or lower.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects a difficulty level of easy
2. User enteres a guess of 15
3. Game retruns "Go HIGHER!"
4. User enteres a guess of 17 -> "Too High"
5. Atempts update after each guess
6. Game ends after the correct guess

## 🧪 Test Results
test_game_logic.py .....                                                                         [100%]

========================================== 5 passed in 0.01s ===========================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
