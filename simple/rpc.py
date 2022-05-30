import random
y = int(input("press 1 to play rock ,paper and scissor game:"))
while y==1 :
    p='''
          press  1 for rock
          press 2 for peper
          press 3 for scissor 
          
          press 0 for exit the game'''
    point=0
    l=['rock','peper','scissor']
    print('user points:',point,p)
    uchoise = int(input("enter your choise:"))

    if uchoise == 0:
        y = 0
    elif uchoise==1:
        uchoise='rock'
    elif uchoise==2:
       uchoise='peper'
    elif uchoise==3:
        uchoise='scissor'
    else:
       print("invalid choise")

    cchoise=random.choice(l)
    print('your choise:', uchoise)
    print('computers choise :', cchoise)

    if uchoise == cchoise:
       print('its Draw')
    elif (uchoise=='rock' and cchoise=='scissor') or (uchoise=='paper' and cchoise=='rock') or (uchoise=='scissor' and cchoise =='paper'):
       print('You Win')
       point+=1
    else:
       print('You Loose')