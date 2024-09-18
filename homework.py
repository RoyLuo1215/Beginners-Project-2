import random

def sigma(word_list):
    return random.choice(word_list)

def answer():

    while True:
        guess = input("Enter your 5-letter guess: ").lower()
        if len(guess) != 5:
            print("Enter a 5-letter word”)
        elif not guess.isalpha():
            print("letters")
        else:
            return guess

def check(guess, word):
    feedback = []
    for i in range(5):
        if guess[i] == word[i]:
            feedback.append("🟩")
        elif guess[i] in word:
            feedback.append("🟨")
        else:
            feedback.append("⬛️")
    return feedback

def play_wordle():
    print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.")
    word_list = [
        "abode", "acute", "alien", "angel", "argue",
"asset", "beach", "bench", "binge", "blame",
"brave", "bring", "camel", "catch", "chase",
"claim", "clear", "climb", "craft", "crane",
"crave", "creek", "curve", "dance", "dealt",
"dream", "drift", "drive", "eager", "early",
"earth", "elite", "enter", "equal", "faith",
"feast", "field", "flame", "flare", "focus",
"found", "fresh", "front", "glare", "globe",
"grace", "grand", "grant", "grave", "great",
"green", "grove", "guard", "happy", "heart",
"honey", "horse", "human", "ideal", "image",
"index", "inner", "input", "joint", "judge",
"large", "laser", "learn", "light", "limit",
"lodge", "loose", "lucky", "magic", "major",
"march", "media", "metal", "money", "music",
"nerve", "noble", "north", "ocean", "orbit",
"other", "panel", "peace", "phone", "plant",
"press", "pride", "prove", "reach", "relax",
"right", "scale", "scene", "scope", "share"
    ]

    word = sigma(word_list)
    guesses = 0

    while guesses < 6:
        guess = answer()
        feedback = check(guess, word)
        print("".join(feedback))

        if feedback == ["🟩"] * 5:
            print("Congratulations! You guessed the word correctly. (")
            return
        guesses += 1


    print("womp womp. the word was", word)

if __name__ == "__main__":
    play_wordle()
