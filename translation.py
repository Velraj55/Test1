def translateLetter(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.islower():
                translation = translation + "g"
            else:
                translation = translation + "G"
        else:
            translation = translation + letter

    print("Final translated letter is " + translation)

fromuser = input("enter any valid string: ")
translateLetter(fromuser)