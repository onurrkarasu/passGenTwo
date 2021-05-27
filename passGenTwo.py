import random

lower="abcdefghijklmnoprqstuvwxyz"
upper="ABCDEFGHIJKLMNOQRSTUVWXYZ"
numbers="012345678"
symbols="[]{}()*;/,._-"

all=lower+upper+numbers+symbols
password="".join(random.sample(all,16)) #If you want your password to have characters, enter the 2nd parameter that number.
print(password)
