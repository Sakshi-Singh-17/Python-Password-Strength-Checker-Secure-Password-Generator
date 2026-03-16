import random

def password_generator():
    

    lower_letter=['a','b' , 'c','d','e','f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_letter=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    numbers=[1,2,3,4,5,6,7,8,9,0]
    symbols=['!', '@','#','$', '%','^','&','*','(',')','?']

    password=[]

    for i in range(4):        
        choice_l=random.choice(upper_letter)
        password.append(choice_l)

    for i in range(7):       
        choice_l=random.choice(lower_letter)
        password.append(choice_l)
             
    for i in range(2):
        choice_n=random.choice(symbols)
        password.append(choice_n)

    for i in range(3):
        choice_s=str(random.choice(numbers))
        password.append(choice_s)   


    random.shuffle(password)

    password_str="".join(password)

    print(password_str)


