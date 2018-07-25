def game():
    player1=""
    choose=input("whick player you want to be? 1 or 2\n")
    if choose==1:
        print("Player choose:",choose)
    elif choose==2:
        print("Player choose:",choose)
    choose==player1
    while player1!="Rock" and player1!="paper" and player1!="scissor":
        player1=input("which thing you want to take?\t, Rock/paper/scissor\n")
    if player1=="Rock":
        player2="paper" and "scissor"
    else:
        player2="Rock"
    print("player1 is",player1,"\nplayer 2 is ",player2)

    if (player1=="Rock" and player2=="scissor"):
        print (player1,"--","Player1 win the game")
    if (player1=="scissor" and player2=="paper"):
        print (player1,"--","Player1 win the game")
    if (player1=="paper" and player2=="scissor"):
        print(player1,"--"," Player1 win the game")
    if (player1 == "paper" and player2 == "Rock"):
        print(player2, "--", " Player2 win the game")
    if (player2=="Rock" and player1=="scissor"):
        print (player2,"--"," Player2 win the game")
    if (player2=="scissor" and player1=="paper"):
        print (player2,"--"," Player2 win the game")
    if (player2=="paper" and player1=="scissor"):
        print(player2,"--"," Player1 win the game")
game()
