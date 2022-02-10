#Write a Python program to find those 
# numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).

#for i in range(1500,2701):
#    if (i%7) == 0 and (i%5) == 0:
#        print (i)

#DONE!!!


#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5

#for i in range(6):
#    if (i == 3) or (i == 6):
#        continue
#    print(i)

#DONE!!!

#Write a Python program that accepts a word from the user and reverses it

#def reversal(input_word):
#    return input_word [::-1]
#
#word = reversal(input("Write your word here: "))
#print("This word backwards is: " + word)

#DONE!!!

#Write a Python program to count the number of even and odd numbers from a series of numbers. 
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

#numbers = (1, 5, 34, 41, 5, 63, 76, 83, 99) 
#even_count = 0
#odd_count = 0
#
#for number in numbers:
#    if number%2 == 0:
#        even_count += 1
#    else:
#        odd_count += 1
#
#print("Number of evens = " + str(even_count))
#print("Number of odds = " + str(odd_count)) 


#DONE!!!

#Write a Python program which iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
#Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

#for i in range (51):
#    if i%3 == 0 and i%5 == 0:
#        print("FizzBuzz")
#    elif i%5 == 0:
#        print("Buzz")
#    elif i%3 == 0:
#        print("Fizz")
#    else:
#        print(i) 
#DONE!!!

#Write a Python program to guess a number between 1 to 9. Go to the editor
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt 
# appears again until the guess is correct, on successful guess, user will get a 
# "Well guessed!" message, and the program will exit.


#from random import randint
#
#
#number = randint(1,9)
#guess = 0
#
#while guess != number:
#    guess = int(input("Guess the number: "))
#
#print("Well guessed!")

#DONE!!!    