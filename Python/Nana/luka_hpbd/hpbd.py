import time
import random
import os


def clear_screen():
    # Clears the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')


def animate_text(text, delay=0.05, color_code='\033[96m'): # Cyan color
    # Prints text with a typing animation and an optional color.
    for char in text:
        print(color_code + char + '\033[0m', end='', flush=True) # Reset color after each char
        time.sleep(delay)
    print() # Newline at the end


def generate_sparkle(length=50):
    # Generates a string of random sparkles.
    sparkles = ['*', '.', 'o', '✨', '🌟']
    return ''.join(random.choice(sparkles) for _ in range(length))


def happy_birthday_script():
    """
    A visual and animated Happy Birthday script.
    """
    clear_screen()

    # --- Opening Animation ---
    print("\n" * 5) # Some top padding
    animate_text("Loading birthday magic...", delay=0.08, color_code='\033[93m') # Yellow
    time.sleep(1)
    clear_screen()

    # --- Cake and Candles ---
    print("\n" * 3)
    cake = [
        "                       .|                      ",
        "                       /\                      ",
        "                      //\                      ",
        "                     ,,///                     ",
        "                     /////                     ",
        "                     /*/(/       .             ",
        "    ...              //(((      ##/((   ...    ",
        "    .....                             *****    ",
        "    ..........      (((( ..      **********    ",
        "    %..%#..........         **********%%**&    ",
        "    %%%###..##.........**********%%**&&%%%&    ",
        "    %##########...%....*****%***%%%%%%%%%%&    ",
        "       %%%########%##.,//*%%%%%%%%%%%%%%       ",
        "            %%%######%%&&%%%%%%%%%%            ",
        "                 %%%##%&&%%%%%                 ",
        "                      %&&                      "
    ]
                                                  
                                                  


    flame = "  🔥  "  # Yellow flame emoji

    for line in cake:
        if ".|" in line:  # Add candles to the cake
            print("                     " + flame)
        else:
            print(line)
        time.sleep(0.05)
    print("\n" * 2)

    animate_text("Look! A cake!", delay=0.07, color_code='\033[92m') # Green
    time.sleep(3)
    clear_screen()

    # --- Confetti Burst ---
    print("\n" * 5)
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    confetti_chars = ['*', 'o', '.', '+', '#', ' ']

    print(" " * 10 + "🎉" * 5) # Top row of party poppers
    for i in range(15):
        line = ""
        for _ in range(70):
            line += random.choice(colors) + random.choice(confetti_chars) + '\033[0m'
        print(line)
        time.sleep(0.02)
    print("\n" * 2)

    animate_text("It's a celebration!", delay=0.06, color_code='\033[94m') # Blue
    time.sleep(1.5)
    clear_screen()

    # --- Main Birthday Message ---
    print("\n" * 5)
    message_lines = [
        "   ✨🌟⭐💫\n\n",
        "    _ _                                      ",
        "   | | | ___  ___  ___  _ _                  ",
        "   |   |<_> || . \| . \| | |                 ",
        "   |_|_|<___||  _/|  _/`_. |                 ",
        "             |_|  |_|  <___'                 ",
        "    _    _        _    _      _              ",
        "   | |_ <_> _ _ _| |_ | |_  _| | ___  _ _    ",
        "   | . \| || '_> | |  | . |/ . |<_> || | |   ",
        "   |___/|_||_|   |_|  |_|_|\___|<___|`_. |   ",
        "                                     <___'   ",
        "    _         _         _                    ",
        "   | |   _ _ | |__ ___ | |                   ",
        "   | |_ | | || / /<_> ||_/                   ",
        "   |___|`___||_\_\<___|<_>                   \n\n",
        "   ✨🌟⭐💫"
    ]


    for line in message_lines:
        animate_text(line, delay=0.001, color_code='\033[95m') # Magenta
        time.sleep(0.2)
    time.sleep(1)

    # --- Final Farewell ---
    clear_screen()
    print("\n" * 3)
    for i in range(10):
        print(" " * random.randint(0, 60) + random.choice(colors) + "*" * random.randint(1, 3) + "\033[0m")
        time.sleep(0.1)
    print("\n" * 2)
    animate_text("Have a truly wonderful birthday!\n\nMay your day be filled with joy, laughter, and all your favorite things!", delay=0.08, color_code='\033[91m') # Red
    print()
    animate_text("Jure & Polona", delay=0.05, color_code='\033[90m') # Dark Grey
    time.sleep(3)
    clear_screen()
    print("\n" * 10)
    print(" " * 20 + "🎉🎂🎁🎊" + " " * 20)
    print("\n" * 10)

if __name__ == "__main__":
    happy_birthday_script()