#!/usr/bin/env python3
round = 0            #integer round initiated to 0
while(True):    #sets up infinite loop condition
    round - round + 1  #increses the round counter
    print('Finish the movie title, "Monty Python\'s The Life of _________________"')
    answer = input() #string answer collected from user
    if (answer.casefold() == 'brian'): #logic to check if user gave the correct answer
       print('Correct')
       break   #break statement escapes the while loop
    elif (answer.casefold() == 'shrubbery'):
       print('You gave the super secret answer')
       break
    elif (round ==3):   #logic to endure round has not yet rached 3
       print('Sorry, the answer was Brian')
       break
    else:    #if answer was wrong, and round is not yet equal to 3
       print('Sorry, try again')
