import time
import random
import sys

# Function to clear the terminal output for a cleaner look
def clear_screen():
    # Clears the console screen, works for most terminals
    print("\033[H\033[J", end="")

def run_reaction_test():
    """
    Runs a simple reaction time test in the command line.
    """
    clear_screen()
    print("🚀 Reaction Time Tester 🚀")
    print("Press ENTER as fast as you can when you see the word 'NOW!'")
    print("Press ENTER to begin...")
    
    # Wait for the user to press Enter to start the preparation phase
    try:
        input()
    except EOFError:
        # Handles cases where input() might fail in some environments
        print("\nTest cancelled.")
        return

    clear_screen()
    print("🔴 Get Ready... The test will start soon.")

    # 1. Random Wait Time
    # Wait for a random duration between 2 and 5 seconds to prevent anticipation
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    # 2. Test Start and Time Recording
    clear_screen()
    
    # Record the precise moment the prompt appears
    start_time = time.time() 
    
    # The prompt to react to
    print("🟢 NOW! Press ENTER!")

    try:
        input_start = time.time()
        input() 
        end_time = time.time()
    except EOFError:
        print("\nTest interrupted. Try again.")
        return
    
    reaction_time = end_time - start_time
    
    if reaction_time < 0.1:
        print("\n🚨 TOO FAST! You reacted before the prompt or the input() started.")
        print("Wait for the 'NOW!' signal next time.")
    else:
        # Format the result to a clean number of milliseconds
        reaction_ms = reaction_time * 1000
        print("\n-------------------------------------------")
        print(f"✅ Your Reaction Time: {reaction_ms:.3f} milliseconds")
        print("-------------------------------------------")

# Run the test when the script is executed
if __name__ == "__main__":
    run_reaction_test()