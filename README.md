# Reaction-tester
🧠 Reaction Time Tester: How Fast is Your Brain!? ⚡
Reaction Time Tester is an ultra-simple, command-line Python application that measures your visual
reaction time. It's a fun and low-friction way to see how fast you can respond to an unexpected prompt
in your terminal.
🚀Quick start guide
Prerequisites
You need a Python interpreter installed:
Python 3.x
Installation & Run
Set up and running this quick test takes less than one minute:
1. Save the file: reaction_tester.py
2. Open your terminal to the location of the file
3. Run the program:
python reaction_tester.py

🕹️Game Play: How to Play/Rules
The object of the game is to hit ENTER the exact moment you see green letters that say NOW!
Readiness: Hit ENTER to prepare to play
Set Position & Delay: The screen shows red letters saying "Get Set; Do not move until you see
GREEN! 🚦". The system randomly pauses (2.0-5.0 seconds) so users do not try to estimate when
they should react.
GO!: Hit ENTER the exact moment you see "NOW! ENTER!". Your time starts as soon as this
message appears.
Results review: Your time in milliseconds appears on the screen with feedback. You are also able
to hit ENTER to immediately play again.

🎯 Main Features
The features of the script are designed for fair and repeatable testing:
Random delay: Ensures the integrity of the reaction time measure
Average 1000ms resolution: Measures based on time.time()
Humanized feedback: Offers comments based on your time classification (e.g., Lightning Fast: <
150 ms, Good Average: 250-400 ms).
Invalid Scores: Automatically considers invalid scores (below 100 ms) are false starts.
