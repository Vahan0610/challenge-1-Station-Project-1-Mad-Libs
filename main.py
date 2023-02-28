def game():
    import random

    index = [0, 1, 2]
    temp = random.choice(index)

    print(f"random choice is: {temp}"),  #####

    if temp == 0:

        number_1 = input("Number /1: ")
        mot_time = input("Measure of time: ")
        mot_trans = input("Mode of Transportation: ")
        adjective_1 = input("Adjective /1: ")
        adjective_2 = input("Adjective /2: ")
        noun_1 = input("Noun /1: ")
        color = input("Color: ")
        pob_1 = input("Part of the Body /1: ")
        verb = input("Verb: ")
        number_2 = input("Number /2: ")
        noun_2 = input("Noun /2: ")
        noun_3 = input("Noun /3: ")
        pob_2 = input("Part of the Body /2: ")
        noun_4 = input("Noun /4: ")
        adjective_3 = input("Adjective /3: ")
        sw = input("Silly Word: ")

        if adjective_1[0].lower() in ('a', 'e', 'i', 'o', 'u'):
            a_an = "an"

        elif adjective_1[0].lower() in (
        'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y'):
            a_an = "a"

        else:
            a_an = ""  ###

        output = f"It was about {number_1} {mot_time} ago when I arrived at the hospital in a {mot_trans}. The hospital is {a_an} {adjective_1} place, there are a lot of {adjective_2} {noun_1} here. There are nurses here who have {color} {pob_1}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number_2}{noun_2}. Today I talked to a doctor and they were wearing a {noun_3} on their {pob_2}. I heard that all doctors {verb} {noun_4} every day for breakfast. The most {adjective_3} thing about being in the hospital is the {sw}{noun_1}!"

        print(output)




    elif temp == 1:

        pn = input("Proper Noun (Person’s Name): ")
        noun_1 = input("Noun /1: ")
        adjective_1 = input("Adjective (Feeling) /1: ")
        verb_1 = input("Verb /1: ")
        adjective_2 = input("Adjective (Feeling) /2: ")
        animal = input("Animal: ")
        verb_2 = input("Verb /2: ")
        color = input("Color: ")
        verb_ing = input("Verb (ending in ing): ")
        adverb = input("Adverb (ending in ly): ")
        number = input("Number:")
        mot_time = input("Measure of time: ")
        sw = input("Silly Word: ")
        noun_2 = input("Noun /2: ")

        if animal[0].lower() in ('a', 'e', 'i', 'o', 'u'):
            a_an = "an"

        elif animal[0].lower() in (
        'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y'):
            a_an = "a"

        else:
            a_an = ""  ###

        output = f"This weekend I am going camping with {pn}. I packed my lantern, sleeping bag, and {noun_1}. I am so {adjective_1} to {verb_1} in a tent. I am {adjective_2} we might see {a_an} {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb_2}. I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number} (Measure of Time). If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {sw} stories and roast {noun_2} around the campfire!!"

        print(output)






    else:

        pn = input("Proper Noun (Person’s Name): ")
        adjective_1 = input("Adjective /1: ")
        color = input("Color: ")
        animal = input("Animal: ")
        place = input("Place: ")
        adjective_2 = input("Adjective /2: ")
        mc_1 = input("Magical Creature (Plural) /1: ")
        adjective_3 = input("Adjective /3: ")
        mc_2 = input("Magical Creature (Plural) /2: ")
        rh = input("Room in a House: ")
        noun_1 = input("Noun /1: ")
        noun_2 = input("Noun /2: ")
        noun_3 = input("Noun(Plural) /1: ")
        adjective_4 = input("Adjective /4: ")
        noun_4 = input("Noun(Plural) /2: ")
        number = input("Number:")
        mot_time = input("Measure of time: ")
        verb_ing = input("Verb (ending in ing): ")
        adjective_5 = input("Adjective /5: ")
        noun_5 = input("Noun /5: ")

        output = f"Dear {pn}, I am writing to you from a {adjective_1} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective_2} {mc_1} and {adjective_3} {mc_2} here! In the {rh} there is a pool full of {noun_1}. I fall asleep each night on a {noun_2} of {noun_3} and dream of {adjective_4} {noun_4}. It feels as though I have lived here for {number}{mot_time}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective_5} {noun_5}!!"

        print(output)

    print("FINISH")

def play():
    answer = input('Hello. You have the chance to play a very interesting game. Do you want to start (Y/N)?: ')

    if answer.lower() == "y":
        game()

    elif answer.lower() == "n":
        print("Hope you will have other chance")

    else:
        con = input("Incorrect anwer. If you wnat to continue click on 'ENTER'")
        if con == "":
            play()

play()

# fix issue with - "empty var. error (article check")
# remove 