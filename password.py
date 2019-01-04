import random
def password_generator(length):
    my_password = ""
    for i in range(length):
        num_or_letter = random.randint(0,100)
        switch = random.randint(0,100)
        starting_number = random.randint(0,26)
        number = starting_number - 3
        if num_or_letter < switch:
            if number > 26:
                number = number - 26
            elif number < 0:
                number = number + 26
            number = number + 65
            upper_or_lower = random.randint(0,4)
            if upper_or_lower > 1:
                number = number + 32
            to_add = chr(number)
        else: 
            number = number + switch - num_or_letter
            number = number // 3
            number = number ** 2
            to_add = str(number)
        
        my_password = my_password + to_add

    return my_password 

#starter code 

print(password_generator(5))