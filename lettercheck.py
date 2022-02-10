#check if a letter is a vowel or a consonant

#class Lettercheck:
#    vowels = "aeiouAEIOU"
#
#letter_input = input("Write a vowel here: ")
#if letter_input in Lettercheck.vowels:
#        print("True")
#else:
#        print("False")


#check how many vowels and consonants are in a word

print("Let's find out how many vowels and consonants are in a word.")
input_word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
cons_count = 0

for letter in input_word:
    if letter in vowels:
        vowel_count += 1
        
    else:
        cons_count += 1
        
print("It has " + str(vowel_count) + " vowel(s) in this word.")
print("And it has " + str(cons_count) + " consonant(s) in this word.")      