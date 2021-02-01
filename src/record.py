import pygame

from src.main import top_left_y,top_left_x,play_width


def draw_top_list(surface,names,score,place):
    pygame.font.init()
    heading = pygame.font.SysFont('comicsans', 60)
    if place == 0:
       label = heading.render("No Highscore. жалость")
    else:
        label = heading.render("You made it to place " + str(place) + "Хорошо!")

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 0))
    pygame.display.update()


def read_in_top_five(surface,pts):
    names = []
    score = []
    place = 0
    f = open("Records/level1.txt", "r")
    for x in f:
        #print(x)
        line = x.split()
        names.append(line[0])
        score.append(int(line[1]))

    for i in range(5):
        if len(score) <= i:
            print("You made it in the Top 5. поздравления!\n")
            print("Your place is " + str(i+1) + "\n")
            place = i +1
            break

        if pts > score[i]:
            print("You made it in the Top 5. поздравления!\n")
            print("Your place is " + str(i+1) + "\n")
            place = i+1
            break

    if place == 0:
        print("You did not made it in the Top 5.")
        draw_top_list(surface, names, score, place)
    else:
        names.insert(place-1,"new")
        score.insert(place-1,pts)
        #nur liste bis 5 maximal oder weniger übergeben
        for i in range(len(names),5):
            names.append("-")
            score.append(0)
        draw_top_list(surface,names,score,place)

    f.close()
   # return [names,scores]
