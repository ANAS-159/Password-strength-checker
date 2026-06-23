password= input("Enter your password:")
has_digit=any(char.isdigit() for char in password)
has_upper=any(char.isupper() for char in password)
has_lower=any(char.islower() for char in password)
has_special=any(not char.isalnum() for char in password)

if len(password) < 8:
    print("Your password is weak,it must be at least 8 characters long.")
elif len(password)>= 8 and has_digit and (has_upper or has_lower):
    print("Medium password.")    
elif len(password) >=8 and has_digit and has_lower and has_upper and has_special:
    print("Strong password.")    
else:
    print("Weak password.")
