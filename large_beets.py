import random

f = open("player0ll.txt", "w")
g = open("player1ll.txt", "w")
k = open("player2ll.txt", "w")

for i in range(4500):
    n = random.randint(50,100)
    f.write('100 ' + str(n) + " ")
    n = random.randint(50,100)
    g.write('100 ' + str(n) + " ")
    n = random.randint(100,350)
    k.write('100 ' + str(n) + " ")

for i in range(4500):
    b = random.randint(70,150)
    f.write('200 ' + str(b) + " ")
    b = random.randint(70,150)
    g.write('200 ' + str(b) + " ")
    b = random.randint(130,300)
    k.write('200 ' + str(b) + " ")

for i in range(4500):
    c = random.randint(100,200)
    f.write('300 ' + str(c) + " ")
    c = random.randint(100,200)
    g.write('300 ' + str(c) + " ")
    c = random.randint(50,150)
    k.write('300 ' + str(c) + " ")