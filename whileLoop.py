secret_word = "giraffe"
guess_word = ""
i=1
guess_count = 0
guess_countMax = 5

while i != 0:
    if (guess_count == guess_countMax):
        print("You have exceeded Max counts")
        break

    guess_word = input("Enter guess word:")
    if ( guess_word == secret_word ):
         i = 0
         guess_count = 0
         print("you win!")
    else:
         guess_count += 1

