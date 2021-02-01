

# What if there aren't 5 players
def read_in_top_five(score):
    names = []
    scores = []
    place = 6
    f = open("Records.txt", "r")
    for x in f:
        line = x.split("\t")
        names[0] = line[0]
        scores[0] = line[1]

    for i in range(5):
        if len(score) <= i:
            print("You made it in the Top 5. поздравления!\n")
            print("Your place is " + str(i) + "\n")
            place = i

        if i> score[i]:
            print("You made it in the Top 5. поздравления!\n")
            print("Your place is " + str(i) + "\n")
            place = i

    if place > 5:
        print("You did not made it in the Top 5.")

    f.close()
    return [names,scores]
