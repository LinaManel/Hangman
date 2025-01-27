import random
import string
from words import words
from hangmanvisual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    lives = 7
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user letters
    while len(word_letters) > 0 and lives > 0:
        print(
            "You have",
            lives,
            " lives left and you have used these letters",
            " ".join(used_letters),
        )
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter not in the word")
                print(lives_visual_dict[lives])
        elif user_letter in used_letters:
            print("Already gessed")
        else:
            print("\nThat is not a valid letter.")
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:
        print("YAY! You guessed the word", word, "!!")


if __name__ == "__main__":
    hangman()
