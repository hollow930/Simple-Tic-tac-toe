import os

def print_board():
    print(b[0]+' | '+b[1]+' | '+b[2])
    print('---------')
    print(b[3]+' | '+b[4]+' | '+b[5])
    print('---------')
    print(b[6]+' | '+b[7]+' | '+b[8])

def player_marker():
    p1_mark='z'

    while p1_mark not in ['x','o']:
        p1_mark=input("Player one, select 'x' or 'o'to be your mark \n").lower()

    os.system('cls')
    
    if p1_mark== 'x':
        return ('x','o')
    else:
        return ('o', 'x')




def player_input():
    p_input='z'

    while p_input not in ['0','1','2','3','4','5','6','7','8']:
        p_input=input('ENTER A NUMBER FROM 0-8 TO PICK YOUR POSITION \n').lower()
    
    os.system('cls')
    p_input=int(p_input)
    return p_input

def update_board():
    if counter % 2 == 0:
        b[player_input()]=p1_mark
    else:
        b[player_input()]=p2_mark

def game_on():

    game_on=True

    if (b[0]==b[1]==b[2]):   
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[0]+ ' WON THE GAME')
    
    if (b[3]==b[4]==b[5]):
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[3]+ ' WON THE GAME')
    
    if (b[6]==b[7]==b[8]):
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[6]+ ' WON THE GAME')

    if (b[0]==b[3]==b[6]): 
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[0]+ ' WON THE GAME')

    if (b[1]==b[4]==b[7]):
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[1]+ ' WON THE GAME')

    if (b[2]==b[5]==b[8]):
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[2]+ ' WON THE GAME')
    
    if (b[0]==b[4]==b[8]): 
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[0]+ ' WON THE GAME')
    
    if (b[6]==b[4]==b[2]):
        game_on=False
        print('CONGRADULATIONS PLAYER '+b[6]+ ' WON THE GAME')
    
    return game_on



b=['0','1','2','3','4','5','6','7','8']

counter=0

print_board()

p1_mark, p2_mark =player_marker()


while(game_on() == True):
    if counter ==9:
        print('THE GAME IS DRAW!')
        break

    print_board()
    update_board()
    counter+=1
    
    
    
print_board()

