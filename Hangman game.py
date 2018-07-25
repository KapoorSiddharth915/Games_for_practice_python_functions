def hangman():
    active=True
    list="evaporate"
    print("welcome to the Hangman game\t!, Let's play")
    attempt=[]
    mylist=[]
    count=1
    while active:
        print("guess the letter")
        user=input()
        if  user not in list:
            print("incorrect guess!,try again")
            attempt.append(user)
            if len(attempt)>5:
                print("sorry you cross the limits ! you loose the game.....better luck next time")
                break
        elif user in list:
            mylist.append(user)
            print("good guess!,try another letter to guess")
            if user in mylist:
                print("you guess same word as previous word")

            if len(mylist) > 8:
                print(mylist)
                print("\nGood job you guess all the correct letters for the word ",list)
                break
    active=False
hangman()