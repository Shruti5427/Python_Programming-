import random
import string

# adjectives and nouns
adjectives = ['Asthetic', 'Sparkly', 'Graceful', "Cool", "Happy", "Fast", "Brave", "Clever", "Witty", "Wild", "Fierce", "Mighty", "Sneaky"]
nouns = ['vibes', "Panda", "Eagle", "Phoenix", "wizard","blessed" ,"queen","bossy"]

# Function to make a random username
def make_username(add_numbers, add_special_chars, max_length=99):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    # Option to add numbers
    if add_numbers:
        num = random.randint(1,99)
        username = f"{adj}{noun}{num}"
    else:
        username = f"{adj}{noun}"

    # Option to add special characters
    if add_special_chars:
        special_char = random.choice(string.punctuation)
        username = f"{username}{special_char}"

    # Apply length limit if given
    if max_length and len(username) > max_length:
        username = username[:max_length]

    return username

# Function to save usernames to a file
def save_usernames(usernames):
    with open("usernames.txt", "w") as file:
        for uname in usernames:
            file.write(uname + "\n")
    print("Usernames saved to 'usernames.txt'!")

# Main function to start the program
def main():
    print("Welcome to the Username Generator! Let's make something fun!")
    
    numbers = input("Do you want numbers in your username? (y/n): ").strip().lower() == 'y'
    special_chars = input("Do you want special characters in your username? (y/n): ").strip().lower() == 'y'
    max_len = input("What's the max length for your username? (press Enter to skip): ").strip()

    if max_len:
        max_len = int(max_len)
    else:
        max_len = None

    # Generate some usernames based on the choices
    usernames = [make_username(numbers, special_chars, max_len) for _ in range(10)]

    print("\nHere are your usernames:")
    for username in usernames:
        print(username)

    save = input("\nDo you want to save these usernames to a file? (y/n): ").strip().lower()
    if save == 'y':
        save_usernames(usernames)

if __name__ == "__main__":
    main()
