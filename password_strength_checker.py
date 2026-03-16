#Password strength checker
from password import password_generator
        
def password_strength_checker(password):

    symbols=['!','@','#','$','%','^','&','*','(',')','_','+','<','>','?','/']
    score=0
    count=len(password)

    has_letter = False
    has_number = False
    has_symbol = False
    has_upper = False
    has_lower = False

    for ch in password:
        
        if ch.isalpha():
            has_letter = True
            
            
        if ch.isdigit():
            has_number = True
            
            
        if ch in symbols:
            has_symbol = True
            

        if ch.isupper():
            has_upper=True
            

        if ch.islower():
            has_lower=True
           

    if has_letter  and has_number and has_symbol and has_upper and has_lower  :
        if count< 8:
            print("Weak Password")            
        elif count<=12:
            print("Moderate Password")
            
        else:
            print("Strong Password")

    elif has_letter  and has_number and has_symbol:
        if count<8:
            print("Weak Password")
        elif count<=12:
            print("Moderate Password")
            
        else:
            print("Highly Moderate but not so strong Password")
        
    else:
        print("Your password is very very easy and its easy to guess, try to add upper or lowercase or numbers or symbols")


    if has_letter:
        score+=3
    if has_number:
        score+=2
    if has_symbol:
        score+=2
    if has_upper:
        score+=1
    if has_lower:
        score+=2
            
    if score<=2:
        print(f"Your password score is {score}")

    elif score<=4:
        print(f"Your password score is {score}")

    elif score<=6:
        print(f"Your password score is {score}")

    elif score<=8:
        print(f"Your password score is {score}")

    else:
        print(f"Your password score is {score}")
    

    suggestions = []
    if not has_upper:
        suggestions.append("Add an uppercase letter")

    if not has_lower:
        suggestions.append("Add a lowercase letter")

    if not has_number:
        suggestions.append("Add a number")

    if not has_symbol:
        suggestions.append("Add a symbol like @ or #")

    if count < 8:
        suggestions.append("Use at least 8 characters")


    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print("-", s)
            
    if suggestions:
        print("\nGenerating a strong password for you...")
        password_generator()
        
            
        
password_check=input("Enter your password to check the level of your password")   
password_strength_checker(password_check)
