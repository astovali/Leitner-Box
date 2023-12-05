from random import shuffle
import json

box = []

def load_box():
    global box
    with open("box.json", "r") as read_it:
        box = json.load(read_it)

def save_box():
    with open("box.json", "w") as p:
        json.dump(box, p)

def new_words(words):
    print(f"Input {words} new words then associated information: ")
    new = []
    for i in range(words):
        new.append([input(""), input("")])
    box[0] += new

def compartment(day, i):
    if (day % (2**i)) == 0:
        print(f"Box No. {i+1}")
        j = 0
        while j < len(box[i]):
            print(box[i][j][0])
            correct = False
            if input("") == box[i][j][1]: correct = True
            else:
                print(box[i][j][1])
                correct = (input("Did you get it right? (y/n) ").lower() == "y")
            if correct:
                if len(box)-1 == i:
                    box.append([box[i].pop(j)])
                else:
                    box[i+1] += [box[i].pop(j)]
                j -= 2
            else:
                if i == 0:
                    shuffle(box[i])
                    j = -1
                else:
                    box[i-1] += [box[i].pop(j)]
                    j -= 2
            j += 1

def memorise(day):
    i = 0
    while i < len(box):
        compartment(day, i)
        i += 1
    compartment(day, 0)

load_box()
day = box.pop(0) + 1
new_words(5)
memorise(day)
box = [day] + box
save_box()