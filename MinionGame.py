def minion_game(S):
    vowels = ['A','E','I','O','U']
    player1 = 0
    player2 = 0
    
    for i in range(len(S)):
        if S[i] in vowels:
            player1 += (len(S) - i)
        else:
            player2 += (len(S) - i)

    if player1 > player2:
        print('Kevin', player1)
    elif player1 == player2:
        print('Draw')
    else:print('Stuart',player2)
