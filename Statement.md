# Reaction Time Tester

This is a simple Python script I wrote to test your reflexes in the terminal. It basically waits for a random amount of time and then tells you to press Enter as fast as you can.

## How it works

The program uses the `time` and `random` modules. Here is the basic logic:

1.  **Clear Screen:** It clears the terminal so there are no distractions.
2.  **Random Delay:** It pauses for a random time between 2 to 5 seconds. This ensures you **cant** predict when the signal will come.
3.  **Measurement:** It takes a timestamp right before the "NOW!" message and another one right after you press Enter.

## How to Run

Make sure you have Python 3 installed. You can run the script using the command **bellow**:

```bash
python reaction_test.pylt.