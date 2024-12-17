def how_old():
    print('Enter your name')
    userName = input()
    print('Enter your age')
    userAge = int(input())

    if (userAge > 100):
        
        when100 = ((2024 - userAge) + 100)
        print (f'Hello {userName}, you are {userAge} and you turned 100 in {when100}')
    
    elif (userAge < 100):

        when100 = ((2024 - userAge) + 100)
        print(f'Hello {userName}, you are {userAge} and you will turn 100 in {when100}')


how_old()