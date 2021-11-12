score = 0
score = int(score)

print("Welcome to Math Police! Created by Robinhood#6198.")
d = input("Which difficulty would you like to play?")

if d == "Easy":
    print("Welcome to Math Police Easy!")
    print("Make sure you are ready to begin this quiz. Remember this quiz must be done in Python 3.")
    answer1 = int(input("Translate the word cat into a numeric value"))

    if answer1 == 24:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer2 = int(input("Translate the word dog into a numeric value"))

    if answer2 == 26:

        print("Correct!")
        score = score + 1

    else:

        print("Incorrect!")

    answer3 = int(input("Translate the word hats into a numeric value"))

    if answer3 == 48:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer4 = int(input("Translate the word lunch into a numeric value."))

    if answer4 == 58:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer5 = int(input("Boss Word! Translate the word danger into a numeric value."))

    if answer5 == 49:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")


        if score == 5:
            print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
        elif score < 5 and score > 2:
            print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
        else:
            print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")


    while score < 5:

        answer6 = input(
            "Do you want to retake this quiz? This message should only appear if you did not get a perfect score. If this message appears even with a perfect score, please report the bug at https://github.com/RobinhoodDev/MathPolice/discussions/2.")

        if answer6 == "yes":

            score = 0
            score = int(score)

            answer1 = int(input("Translate the word cat into a numeric value"))

            if answer1 == 24:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer2 = int(input("Translate the word dog into a numeric value"))

            if answer2 == 26:

                print("Correct!")
                score = score + 1

            else:

                print("Incorrect!")

            answer3 = int(input("Translate the word hats into a numeric value"))

            if answer3 == 48:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer4 = int(input("Translate the word lunch into a numeric value."))

            if answer4 == 58:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer5 = int(input("Boss Word! Translate the word danger into a numeric value."))

            if answer5 == 49:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            if score == "5":
                print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
            elif score < 5 and score >= 3:
                print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
            else:
                print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

        elif answer6 == "no":
         score = 5
        print("Please exit this quiz with exit().")
elif d == "Medium":
    print("Welcome to Math Police Medium!")
    print("Make sure you are ready to begin this quiz. Remember this quiz must be done in Python 3.")
    answer1 = int(input("Translate the word safely into a numeric value"))

    if answer1 == 68:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer2 = int(input("Translate the word privacy into a numeric value"))

    if answer2 == 94:

        print("Correct!")
        score = score + 1

    else:

        print("Incorrect!")

    answer3 = int(input("Translate the word suburban into a numeric value"))

    if answer3 == 98:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer4 = int(input("Translate the word capacity into a numeric value."))

    if answer4 == 78:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer5 = int(input("Boss Word! Translate the word microsoft into a numeric value."))

    if answer5 == 86:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")


        if score == 5:
            print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
        elif score < 5 and score > 2:
            print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
        else:
            print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")


    while score < 5:

        answer6 = input(
            "Do you want to retake this quiz? This message should only appear if you did not get a perfect score. If this message appears even with a perfect score, please report the bug at https://github.com/RobinhoodDev/MathPolice/discussions/2.")

        if answer6 == "yes":

            score = 0
            score = int(score)

            answer1 = int(input("Translate the word safely into a numeric value"))

            if answer1 == 68:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer2 = int(input("Translate the word privacy into a numeric value"))

            if answer2 == 94:

                print("Correct!")
                score = score + 1

            else:

                print("Incorrect!")

            answer3 = int(input("Translate the word suburban into a numeric value"))

            if answer3 == 98:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer4 = int(input("Translate the word capacity into a numeric value."))

            if answer4 == 78:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer5 = int(input("Boss Word! Translate the word microsoft into a numeric value."))

            if answer5 == 86:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            if score == "5":
                print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
            elif score < 5 and score >= 3:
                print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
            else:
                print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

        elif answer6 == "no":
         score = 5
        print("Please exit this quiz with exit().")
if d == "Hard":
    score = 0
    score = int(score)

    print("Welcome to Math Police Hard!")
    print("Make sure you are ready to begin this quiz. Remember this quiz must be done in Python 3.")

    answer1 = int(input("Translate the word abalienate into a numeric value"))

    if answer1 == 70:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer2 = int(input("Translate the word xenobiosis into a numeric value"))

    if answer2 == 131:

        print("Correct!")
        score = score + 1

    else:

        print("Incorrect!")

    answer3 = int(input("Translate the word voicelessly into a numeric value"))

    if answer3 == 146:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer4 = int(input("Translate the word xanthogenic into a numeric value."))

    if answer4 == 120:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer5 = int(input("Boss Word! Translate the word vaccinogenic into a numeric value."))

    if answer5 == 105:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

        if score == 5:
            print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
        elif score < 5 and score > 2:
            print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
        else:
            print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

    while score < 5:

        answer6 = input(
            "Do you want to retake this quiz? This message should only appear if you did not get a perfect score. If this message appears even with a perfect score, please report the bug at https://github.com/RobinhoodDev/MathPolice/discussions/2 .")

        if answer6 == "yes":

            score = 0
            score = int(score)

            answer1 = int(input("Translate the word abalienate into a numeric value"))

            if answer1 == 70:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer2 = int(input("Translate the word xenobiosis into a numeric value"))

            if answer2 == 131:

                print("Correct!")
                score = score + 1

            else:

                print("Incorrect!")

            answer3 = int(input("Translate the word voicelessly into a numeric value"))

            if answer3 == 146:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer4 = int(input("Translate the word xanthogenic into a numeric value."))

            if answer4 == 120:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer5 = int(input("Boss Word! Translate the word vaccinogenic into a numeric value."))

            if answer5 == 105:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            if score == "5":
                print("Your score is" + " " + str(score) + " " + "out of 5.")
            elif score < 5 and score >= 3:
                print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
            else:
                print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

        elif answer6 == "no":
            score = 5
        print("Please exit this quiz with exit().")
if d == "Insane":
    score = 0
    score = int(score)

    print("Welcome to Math Police Insane!")
    print("Make sure you are ready to begin this quiz. Remember this quiz must be done in Python 3.")

    answer1 = int(input("Translate the word acetylglycine into a numeric value"))

    if answer1 == 141:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer2 = int(input("Translate the word vitreodentinal into a numeric value"))

    if answer2 == 168:

        print("Correct!")
        score = score + 1

    else:

        print("Incorrect!")

    answer3 = int(input("Translate the word vitrifications into a numeric value"))

    if answer3 == 174:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

        if score == 3:
            print("Your score is" + " " + str(score) + " " + "out of 3.Perfect!")
        elif score < 3 and score > 1:
            print("Your score is" + " " + str(score) + " " + "out of 3. That's pretty good!")
        else:
            print("Your score is" + " " + str(score) + " " + "out of 3. Better luck next time!")

    while score < 5:

        answer6 = input(
            "Do you want to retake this quiz? This message should only appear if you did not get a perfect score. If this message appears even with a perfect score, please report the bug at https://github.com/RobinhoodDev/MathPolice/discussions/2.")

        if answer6 == "yes":
            answer1 = int(input("Translate the word acetylglycine into a numeric value"))

            if answer1 == 141:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer2 = int(input("Translate the word vitreodentinal into a numeric value"))

            if answer2 == 168:

                print("Correct!")
                score = score + 1

            else:

                print("Incorrect!")

            answer3 = int(input("Translate the word vitrifications into a numeric value"))

            if answer3 == 174:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")
            if score == "3":
                print("Your score is" + " " + str(score) + " " + "out of 3.Perfect!")
            elif score < 3 and score >= 1:
                print("Your score is" + " " + str(score) + " " + "out of 3. That's pretty good!")
            else:
                print("Your score is" + " " + str(score) + " " + "out of 3. Better luck next time!")

        elif answer6 == "no":
         score = 5
        print("Please exit this quiz with exit().")
if d == "Godlike":
    score = 0
    score = int(score)

    print("Welcome to Math Police Godlike!")
    print("Make sure you are ready to begin this quiz. Remember this quiz must be done in Python 3.")

    answer1 = int(input("Translate the word floccinaucinihilipilification into a numeric value"))

    if answer1 == 280:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer2 = int(input("Translate the word pseudopseudohypoparathyroidism into a numeric value"))

    if answer2 == 400:

        print("Correct!")
        score = score + 1

    else:

        print("Incorrect!")

    answer3 = int(input("Translate the word supercalifragilisticexpialidocious into a numeric value"))

    if answer3 == 379:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer4 = int(input("Translate the word hippopotomonstrosesquippedaliophobia into a numeric value."))

    if answer4 == 463:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

    answer5 = int(
        input("Boss Word! Translate the word pneumonoultramicroscopicsilicovolcanoconiosis into a numeric value."))

    if answer5 == 560:

        print("Correct!")
        score = score + 1
    else:

        print("Incorrect!")

        if score == 5:
            print("Your score is" + " " + str(score) + " " + "out of 5.Perfect!")
        elif score < 5 and score > 2:
            print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
        else:
            print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

    while score < 5:

        answer6 = input(
            "Do you want to retake this quiz? This message should only appear if you did not get a perfect score. If this message appears even with a perfect score, please report the bug at https://github.com/RobinhoodDev/MathPolice/discussions/2.")

        if answer6 == "yes":

            score = 0
            score = int(score)

            answer1 = int(input("Translate the word floccinaucinihilipilification into a numeric value"))

            if answer1 == 280:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer2 = int(input("Translate the word pseudopseudohypoparathyroidism into a numeric value"))

            if answer2 == 400:

                print("Correct!")
                score = score + 1

            else:

                print("Incorrect!")

            answer3 = int(input("Translate the word supercalifragilisticexpialidocious into a numeric value"))

            if answer3 == 379:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer4 = int(input("Translate the word hippopotomonstrosesquippedaliophobia into a numeric value."))

            if answer4 == 463:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            answer5 = int(
                input(
                    "Boss Word! Translate the word pneumonoultramicroscopicsilicovolcanoconiosis into a numeric value."))

            if answer5 == 560:

                print("Correct!")
                score = score + 1
            else:

                print("Incorrect!")

            if score == "5":
                print("Your score is" + " " + str(score) + " " + "out of 5.")
            elif score < 5 and score >= 3:
                print("Your score is" + " " + str(score) + " " + "out of 5. That's pretty good!")
            else:
                print("Your score is" + " " + str(score) + " " + "out of 5. Better luck next time!")

        elif answer6 == "no":
            score = 5
        print("Please exit this quiz with exit().")

if d == "Boss Word 1":
    answer5 = int(input(
        "Boss Word! Translate the word lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphiokarabomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoiosiraiobaphetraganopterygon into a numeric value."))

    if (answer5 == 2091):

        print("Correct!")

    else:
        print("Incorrect!")






