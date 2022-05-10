import random

f = open("player0.txt", "w")
g = open("player1.txt", "w")
k = open("player2.txt", "w")

for i in range(150):
    n = random.randint(50,100)
    f.write('100 ' + str(n) + " ")
    n = random.randint(50,100)
    g.write('100 ' + str(n) + " ")
    n = random.randint(100,350)
    k.write('100 ' + str(n) + " ")

for i in range(150):
    b = random.randint(70,150)
    f.write('200 ' + str(b) + " ")
    b = random.randint(70,150)
    g.write('200 ' + str(b) + " ")
    b = random.randint(130,300)
    k.write('200 ' + str(b) + " ")

for i in range(150):
    c = random.randint(100,200)
    f.write('300 ' + str(c) + " ")
    c = random.randint(100,200)
    g.write('300 ' + str(c) + " ")
    c = random.randint(50,150)
    k.write('300 ' + str(c) + " ")