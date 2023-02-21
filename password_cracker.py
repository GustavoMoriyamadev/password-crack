from random import *
import os

your_pwd=input("Enter a Password:")

pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','1','2','3','4','5','6']

pw=""

while(pw!=your_pwd):
    pw=""
    for letter in range(len(your_pwd)):
        guess_pwd=pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password ... Please Wait !")
        os.system("cls")

print("Your Password is:",pw)
