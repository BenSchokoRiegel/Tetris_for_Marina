import textwrap

import pygame


def draw_top_list(surface,names,score,place, list_of_window_stuff):
    top_left_x = list_of_window_stuff[0]
    top_left_y = list_of_window_stuff[1]
    play_width = list_of_window_stuff[2]
    play_hight = list_of_window_stuff[3]

    pygame.font.init()
    surface.fill((255,255,255))
    bg = pygame.image.load("pictures/Endkart Bilder/kissing.jpg")
    surface.blit(bg,(0,0))
    heading = pygame.font.SysFont('comicsans', 60)
    if place == 0:
       label = heading.render("No Highscore. жалость",1, (255, 255, 255))
       surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / 1.2)))
       for i in range(1, 6):
           name = names[i - 1];
           for _ in range((len(name)), 15):
               name = name + " "

           text = str(i) + " : " + name + " = " + str(score[i - 1])
           new_label = heading.render(text, 1, (255, 0, 0))
           surface.blit(new_label, (
           top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / (1.8 + (0.1 * i * i)))))
       pygame.display.update()
       return

    pl_name = ''
    done = False
    while not done:
        surface.fill((255, 255, 255))
        surface.blit(bg, (0, 0))
        label = heading.render("You made it to place " + str(place) + ". Хорошо!",1, (0, 0, 0))
        surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / 1.2)))
        label2 = heading.render("Enter your name :" + str(pl_name),1, (0, 0, 0))
        surface.blit(label2, (top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / 1.4)))
        names[place - 1 ] = pl_name

        label_highscore = heading.render("HighscoreList :" ,1, (255, 0, 0))
        surface.blit(label_highscore, (top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / 1.6)))


        for i in range(1,6):
            name = names[i - 1];
            for _ in range((len(name)),15):
                name = name + " "

            text = str(i) + " : " + name + " = " + str(score[i-1])
            new_label = heading.render(text,1,(255, 0, 0))
            surface.blit(new_label,(top_left_x + play_width / 2 - (label.get_width() / 2), play_hight - (play_hight / (1.8 + (0.1 *i * i )))))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break;

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    print("enter")
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    pl_name = pl_name[0:len(pl_name)-1]
                else:
                    pl_name = pl_name + event.unicode
    pygame.display.update()

def create_highscore_cheat():
    pass


def read_in_top_five(surface, pts,list_of_window_stuff):
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
        draw_top_list(surface,names,score,place,list_of_window_stuff)

    f.close()
   # return [names,scores]
