import random

movie_dialogues = {
    "kitne aadmi the?": "sholay",
    "Aaj mere pas bungla hain, gadi hain, bank balance hain, tumhare pas kya hain? mere paas maa hai.": "deewar",
    "it's all about loving your parents.": "kabhi khushi kabhie gham",
    "aal izz well.": "3 idiots",
    "rishte mein toh hum tumhare baap lagte hain, naam hai shahenshah.": "shahenshah",
    "don ko pakadna mushkil hi nahin, namumkin hai.": "don",
    "mhari chhoriyaan chhoro se kam hai ke!": "dangal",
    "swagat nahi karoge aap hamara?": "dabang",
    "jaadu ki jhappi.": "munna bhai mbbs",
    "Mogambo khush hua": "mr india",
    "Ja Simran ja jee le apni zindagi": "ddlj",
    "Utha le re baba": "hera pheri",
    "Parampara. Pratishtha. Anushasan. Yehi is gurukul ke teen stambh hain.": "mohabbatein",
    "Ek chutki sindoor ki keemat tum kya jano Ramesh babu": "om shanti om",
    "Don’t underestimate the power of a common man.": "chennai express",
    "Basanti in kutto ke samne mat naachna": "sholay",
    "Filmein sirf teen cheezon ki wajah se chalti hain entertainment, entertainment, entertainment aur main entertainment hu.": "dirty picture",
    "Pushpa I hate tears": "amar prem",
}


def main():
    global user_name
    user_name = input("Please enter your name: ").capitalize()
    user_ready = input("Are you ready for a fun round? (yes/no)").lower()
    try:
        if user_ready == "yes" or user_ready == "no":
            if user_ready == "yes":
                game()
            else:
                print("Okay, have a great time ahead.")
    except:
        print("Invalid choice. Try again")


def game():
    score = 0
    for i in range(5):
        list_movie_dialogues = list(movie_dialogues.keys())
        game_guess = random.choice(list_movie_dialogues)
        print(f"{game_guess}")
        list_movie_dialogues.remove(game_guess)
        user_guess = input(f"Guess the movie : ").lower().strip()
        if movie_dialogues.get(game_guess) == user_guess:
            print("Congratulations. You guessed it right.\n")
            score += 1
        else:
            print(f"Oops, wrong guess. It's {movie_dialogues.get(game_guess)}.\n")
    total_score(score)


def total_score(score):
    print(f"Congratulations! {user_name} 🎉🎉🎉 You scored {score} out of 5🏆🏅")
    ask = input("Do you want to play again? (yes/no)").lower()
    try:
        if ask == "yes" or ask == "no":
            if ask == "yes":
                game()
            elif ask == "no":
                print(f"It was nice seeing you, {user_name}. Have a great day ahead.")
    except:
        print("Oops, wrong input. Try again.")


main()
