# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

RESPONSE: Message popup is incorrect after guessing a number (says the opposite). Difficulty level doesn't match with number range. Normal level range id 1 to 100 and Easy level is to 1 to 20.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Guess: 39 | "Go LOWER!"      | "Go HIGHER!"    | None
Difficuly: Normal | Range 1 - 50 | Range 1 - 100 | None
Enter a guess number | Log the guess number to the array | None


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
RESPONSE: Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
RESPONSE: 
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
I verified the result through a reasoning check. If the guess > secret, guess is too high. Vice versa. I tried on the game too.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
RESPONSE:
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
The g can be written as guess for readability as g can mean anything.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
RESPONSE: I reasoned through the changes that Claude suggested and went through examples of inputs.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
A test I ran was when the guess is 60 and the secret number is 50. I checked that it's supposed to say "GO LOWER!," which it did.
- Did AI help you design or understand any tests? How?
AI did help me design the structure of the test since I've never used Python tests before. This was my first time seeing how the tests work and what the results show in the terminal.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
RESPONSE: N/A

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
