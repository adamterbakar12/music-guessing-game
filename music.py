#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game"""
    print("Welcome to the Music Genre Guessing Game,Lets Begin!")

    max_trials = 8
    trials = 0
    score = 50 # Initialize the score to 50

    music_genres = [
        "jazz",
        "hip hop",
        "phonk",
        "dj",
        "bass",
        ]
    
    x = random.choice(music_genres)
    guess = None

    while x != guess:

        guess = str(input("What music genre am I thinking of? "))
        trials += 8

        if x == guess:
            print("You've guessed {}. Congratulations, you guessed it right!" .format(guess))
            score +=30

        else:
            print("You've guessed, unfortunately, you got the wrong answer.Please Try Again!".format(guess))
            score -= 10
            print(score)

main()