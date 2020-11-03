# import
import random

# checking input
while True:
    errors = 0
    try:
        wybor = list(map(int, input("Enter 6 numbers from 1 to 50: ").split()))

    except ValueError:
        print("Not all entered values are numbers.")
    else:
        if len(wybor) != 6:
            print("Exactly 6 numbers should be given.")
            errors += 1
        if len(list(filter(lambda x: x < 1 or x > 50, wybor))):
            print("A number or numbers were supplied out of range.")
            errors += 1
        if len(wybor) != len(set(wybor)):
            print("Duplicate values have been given.")
            errors += 1
        if not errors:
            wybor.sort()
            break

zbior_gracz = set(wybor)
print("\nThe numbers selected by the player are: {}\n".format(wybor))

# II. draw numbers by Computer

komputer = random.sample(range(1, 50), 6)
komputer.sort()
print("The computer drew the following numbers: {}\n".format(komputer))

zbior_komputer = set(komputer)

# III. draw LOTTO numbers

lotto = random.sample(range(1, 50), 6)
lotto.sort()
print("The drawing machine selected the following LOTTO numbers: {}\n".format(lotto))

zbior_lotto = set(lotto)

# IV. Comparision LOTTO numbers with Users numbers

trafienia2 = zbior_gracz.intersection(zbior_lotto)

if len(trafienia2) == 0:
    print("Unfortunately, you didn't guess any number. Try again\n")
elif len(trafienia2) == 1:
    print("You guessed " + str(len(trafienia2)) + " number and that's " + str(trafienia2) + "\n")
elif 1 < len(trafienia2) < 5:
    print("You guessed " + str(len(trafienia2)) + " numbers and these are " + str(trafienia2) + "\n")
#else:
    #print("Udało ci się trafić " + str(len(trafienia2)) + " liczb i są to " + str(trafienia2) + "\n")

# V. Comparision LOTTO numbers with Computer's numbers

trafienia = zbior_komputer.intersection(zbior_lotto)

if len(trafienia) == 0:
    print("Unfortunately, the computer failed to guess any number. Try again.\n")
elif len(trafienia) == 1:
    print("The computer managed to guess " + str(len(trafienia)) + " number and that's :" + str(trafienia) + "\n")
elif 1 < len(trafienia) < 5:
    print("The computer managed to guess" + str(len(trafienia)) + " numbers and these are :" + str(trafienia) + "\n")
#else:
    #print("Komputerowi udało się trafić " + str(len(trafienia)) + " liczb i są to :" + str(trafienia) + "\n")

# VI. Comparision results (User vs Computer)

if trafienia2 > trafienia:
    print("User wins")
elif trafienia == trafienia2:
    print("Draw")
else:
    print("Computer wins")
