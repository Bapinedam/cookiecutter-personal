import random
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
#subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


frases = ["1% per day is 37 times more in a year", 
        "Try don't fuck it",
        "Don't ask the people to invest in you if you are not investing in you",
        "Fake it until you make it",
        "Do run, Do right, Do fast!"]

random_sentence = random.choice(frases)

print(f"{MESSAGE_COLOR} {random_sentence} {RESET_ALL}")