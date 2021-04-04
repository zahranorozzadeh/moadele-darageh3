def show():
    for i in range(3):
        for j in range(3):
            print(game[i][j] , end=' ')
        print()


def check():
    for i in range(3):
        if game[i][0]== 'x' and game[i][1] =='x' and game[i][2] == 'x':
            print('player1 wins')
            exit()

    

game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]


show()


while True:

    #player1
    print('player1')
    while True:
        row = int(input())
        col = int(input())

        if  0 <= row <= 2 and 0 <= col <= 2 : 
            if game[row][col] =='-':
                game[row][col] = 'x'
                break
            else:
                print('errore!this cell is not empty')
        else:
            print('error!index out of range,try again')

    show()
    check()

    #player2
    print('player2')
    while True:
        row = int(input())
        col = int(input())

        if  0 <= row <= 2 and 0 <= col <= 2 : 
            if game[row][col] =='-':
                game[row][col] = 'x'
                break
            else:
                print('errore!this cell is not empty')
        else:
            print('error!index out of range,try again')


    show()
    check()