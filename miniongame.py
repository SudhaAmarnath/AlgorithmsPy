def minion_game(s):

    vowels = 'AEIOU'
    player1,player2 = 0,0
    for i in range(len(s)):
        if s[i] in vowels:
            player1 += (len(s)-i)
        else:
            player2 += (len(s)-i)

    if player1 > player2:
        print("player1 score:", player1)
    elif player1 < player2:
        print("player2 score:", player2)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)