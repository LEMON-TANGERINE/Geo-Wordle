import random

def load_words():
    file = open("countries.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    words = []
    for line in lines:
        word = line.strip().lower()
        words.append(word)

    return words
words = load_words()
valid_words = set(words)
secret_country = random.choice(words)
print(r"""
 _______  _______  _______    _  _  _  _______  _______  ______  _      _______ 
|  _____|| ______||  ___  |  | || || ||  ___  ||  ___  ||  __  \| |    |  _____|
| | ____ | |_____ | |   | |  | || || || |   | || |___| || |  | || |    | |_____ 
| ||__  ||  _____|| |   | |  | || || || |   | ||  _  __|| |  | || |    |  _____|
| |___| || |_____ | |___| |  | || || || |___| || | \ \  | |__| || |___ | |_____ 
|_______||_______||_______|  |_______||_______||_|  \_\ |______/|_____||_______|
""")
print("-------------------------------------------------------------------------------")
print("-------------------------I've chosen a secret country.-------------------------")
print("-----------------------------It's got ", len(secret_country), 'letters.-----------------------------')
print("-------------------------------------------------------------------------------")

def evaluate_attempt(secret_country, attempt):

    result = ["absent"] * len(secret_country)
    remaining_letters = {}
    for a in range(len(secret_country)):
        if attempt[a] == secret_country[a]:
            result[a] = "correct"
        else:
            letter = secret_country[a]
            if letter not in remaining_letters:
                remaining_letters[letter] = 0
            remaining_letters[letter] += 1

    for a in range(len(secret_country)):
        if result[a] == "correct":
            continue
        letter = attempt[a]
        if letter in remaining_letters and remaining_letters[letter] > 0:
            result[a] = "present"
            remaining_letters[letter] -= 1
        else:
            result[a] = "absent"

    return result

GREEN = "\033[32m"
YELLOW = "\033[33m"
GRAY = "\033[90m"
RESET = "\033[0m"
def show_attempt(attempt, states):
    output = ""
    for a in range(len(attempt)):
        letter = attempt[a].upper()
        state = states[a]
        if state == "correct":
            output += GREEN + letter + RESET + " "
        elif state == "present":
            output += YELLOW + letter + RESET + " "
        else:
            output += GRAY + letter + RESET + " "
    print(output)

max_attempts = 7
for attempts in range(1, max_attempts + 1): 
    print('attempt', attempts, 'of', max_attempts)
    while True:
        attempt = input('Country: ').strip().lower()
        if len(attempt) != len(secret_country):
            print('The country has to have ', len(secret_country), 'letters.')
            continue
        if attempt not in valid_words:
            print("Not in the country list.")
            continue
        break
    if attempt == secret_country:
        print("You're right! The country was: ", secret_country.title())
        break

    states = evaluate_attempt(secret_country, attempt)
    show_attempt(attempt, states)
else:
    print("You've run out of attempts. The country was: ", secret_country.title())