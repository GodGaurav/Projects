import random
import string

#things we need to do, input number of characters from the user, for starters just take 5 characters. use random to jumble them up
#give user the random generated password 


def passwordgen(N):
    jumbled = random.choices(["a","b","c","d","e","f","g","H","I","J"], k = N)
    jumbled1 = "".join(jumbled)
    return jumbled1


user1 = passwordgen(int(input("Please type how many characters do you need in your new password, the pass can be between 1 and 20")))
print("The generated password is:", user1)
