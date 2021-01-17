import random
import string   

print('Welcome to Password Generator!')

length = int(input('\nEnter the length of Password: '))             #generator

lower = string.ascii_lowercase                  #lowercase letters
upper = string.ascii_uppercase                  #uppercase letters
num = string.digits                             #numbers
symbols = string.punctuation                    #symbols

all = lower + upper + num + symbols             #all variable for randomizing

temp = random.sample(all, length)               #random using the variable upper, lower, numbers, symbols
password = "".join(temp)                        #result (integer value) using randoms from the variables
print(password)                                 #display result