# your code goes here!

def countdown(number):
    counter = 1
    while counter <= number:
        print(f'{number} SECOND(S)!')
        number -= 1
        # counter +=1
    else:
        print("HAPPY NEW YEAR!")
        
    
import time

def countdown_with_sleep(number):
    counter = 1
    while counter <= number:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Introduce a 1-second delay
        number -= 1
        # counter +=1
    else:
        print("HAPPY NEW YEAR!")
    