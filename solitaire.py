#Jeu de cartes Solitaire sans interface graphique

import random



#----------------------------
#----------------------------
#------Initialisation--------
#----------------------------

#remplir les tas de cartes au début
def init(pioche, row_1, row_2, row_3, row_4, row_5, row_6):
    #remplissage de la pioche
    pioche = fill_pioche(pioche)
    #print_pioche(pioche, len(pioche))

    #remplissage des tas avec les cartes de la pioche
    pioche, row_1 = fill_row(pioche, row_1, 1)
    pioche, row_2 = fill_row(pioche, row_2, 2)
    pioche, row_3 = fill_row(pioche, row_3, 3)
    pioche, row_4 = fill_row(pioche, row_4, 4)
    pioche, row_5 = fill_row(pioche, row_5, 5)
    pioche, row_6 = fill_row(pioche, row_6, 6)

    return pioche, row_1, row_2, row_3, row_4, row_5, row_6


#créer chaque cartes, et remplir la pioche
def fill_pioche(pioche):
    card = '' #nb + space + fam

    nb = 0
    space = ''
    fam = ''
    
    for i in range(10):
        nb = i + 1
        if (nb == 10) :
            space = ''
        else :
            space = ' '

        fam = 'cR'
        card += space + str(nb) + fam
        pioche.append(card)
        card = ''

        fam = 'kR'
        card += space + str(nb) + fam
        pioche.append(card)
        card = ''

        fam = 'tN'
        card += space + str(nb) + fam
        pioche.append(card)
        card = ''

        fam = 'pN'
        card += space + str(nb) + fam
        pioche.append(card)
        card = ''

        i += 1

    random.shuffle(pioche)
    return pioche

#remplir un tas de la zone couleur
def fill_row(pioche, stack, length):
    for i in range(length):
        stack.append(pioche[0])
        pioche.pop(0)
    
    return pioche, stack


#----------------------------
#-----------FIN--------------
#------Initialisation--------
#----------------------------

#----------------------------------------------------------

#----------------------------
#----------------------------
#---------Affichage----------
#----------------------------


def print_game(pioche, bin, row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6, fam_c, fam_k, fam_t, fam_p):
    remain_cards = len(pioche)
    if (len(bin) == 0) :
        card = '____'
    else :
        card = bin[-1]

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("   -----------------              -------------------------------------------")
    print("  | Pioche    Carte |            | Coeur      Carreau      Trefle      Pique |")

    print("  |  (", end="")
    if(remain_cards < 10) :
        print(" " + str(remain_cards), end="")
    else :
        print(str(remain_cards), end="")
    print(")      ", end="")
    print(card, end="")
    
    print(" |            |  ", end="")
    print_fam_stack(fam_c, len(fam_c), 'c', 'R')
    print("        ", end="")
    print_fam_stack(fam_k, len(fam_k), 'k', 'R')
    print("        ", end="")
    print_fam_stack(fam_t, len(fam_t), 't', 'N')
    print("        ", end="")
    print_fam_stack(fam_p, len(fam_p), 'p', 'N')
    print(" |")

    print("   -----------------              -------------------------------------------")

    print(" -------------------------------------------------------------------------------")
    print("|      A    B    C    D    E    F    G    H    I    J    K    L    M    N    O  |")
    '''
    print("| 0- ", end="")
    print_stack(pioche, len(pioche))
    print("|")
    '''
    print("|                                                                               |")
    print("| 1- ", end="")
    print_stack(row_1, len(row_1), hide_1)
    print_space(15 - len(row_1))
    print("|")
    print("|                                                                               |")
    print("| 2- ", end="")
    print_stack(row_2, len(row_2), hide_2)
    print_space(15 - len(row_2))
    print("|")
    print("|                                                                               |")
    print("| 3- ", end="")
    print_stack(row_3, len(row_3), hide_3)
    print_space(15 - len(row_3))
    print("|")
    print("|                                                                               |")
    print("| 4- ", end="")
    print_stack(row_4, len(row_4), hide_4)
    print_space(15 - len(row_4))
    print("|")
    print("|                                                                               |")
    print("| 5- ", end="")
    print_stack(row_5, len(row_5), hide_5)
    print_space(15 - len(row_5))
    print("|")
    print("|                                                                               |")
    print("| 6- ", end="")
    print_stack(row_6, len(row_6), hide_6)
    print_space(15 - len(row_6))
    print("|")
    print(" -------------------------------------------------------------------------------")

    '''
    print_stack(row_1, length_row_1)
    print_stack(row_2, length_row_2)
    print_stack(row_3, length_row_3)
    print_stack(row_4, length_row_4)
    print_stack(row_5, length_row_5)
    print_stack(row_6, length_row_6)
    '''

#affichage de la pioche (debug)
def print_pioche(stack, length):
    for i in range(length):
        print(stack[i], end="")

        if ((i + 1) % 4 == 0) :
            print("")
        else :
            print(" ", end ="")
    
    print("")

#affichage pour les tas des couleurs
def print_stack(stack, length, hide):
    for i in range(length):
        if (hide != 0):
            print('____', end=" ")
            hide -= 1
        else:
            print(stack[i], end=" ")

#affichage pour les tas des familles
def print_fam_stack(stack, length, fam, color):
    if (len(stack) == 0):
        print("  " + fam + color, end="")
    else:
        print(stack[-1], end="")

#affiche nb empty area after each row
def print_space(nb):
    for i in range(nb):
        print("     ", end="")

#----------------------------
#------------FIN-------------
#---------Affichage----------
#----------------------------






#----------------------------
#----------------------------
#-----------Game-------------
#----------------------------

#choisi la première action à faire (entre "deposer", "prendre" (pour déplacer une carte du terrain), ou "repiocher")
def choix():
    choix = ''
    print("Que faire ? (0: repiocher, 1: poser, 2: prendre)")

    while(choix != '0' and choix != '1' and choix != '2'):
        choix = input(">")
    
    return choix


def choix_poser():
    choix = 0

    print("Où poser ? (soit un ligne (ex: 5), soit une famille (ex: trefle))")

    while(choix != '1' and choix != '2' and choix != '3' and choix != '4' and choix != '5' and choix != '6' and choix != 'coeur' and choix != 'carreau' and choix != 'trefle' and choix != 'pique'):
        choix = input(">").lower()
    
    return choix

def choix_prendre():
    choix = '  '
    
    print("Quelle carte prendre ? (donner des coordonner (ex: '4D', pour la carte D (et E, F...si elles existe) sur la 4éme colonne))")

    while((choix[0] != '1' and choix[0] != '2' and choix[0] != '3' and choix[0] != '4' and choix[0] != '5' and choix[0] != '6') or (choix[1] != 'a' and choix[1] != 'b' and choix[1] != 'c' and choix[1] != 'd' and choix[1] != 'e' and choix[1] != 'f' and choix[1] != 'g' and choix[1] != 'h' and choix[1] != 'i' and choix[1] != 'j' and choix[1] != 'k' and choix[1] != 'l' and choix[1] != 'm' and choix[1] != 'n' and choix[1] != 'o')):
        choix = input(">").lower()
        print(choix[0], choix[1])

    return choix


#verifie si la carte est posable, et la pose si oui
def poser(choice, bin, row_1, row_2, row_3, row_4, row_5, row_6, fam_c, fam_k, fam_t, fam_p) :
    if (choice == '1'):
        if (posable_on_color(bin[-1], row_1) == True):
            row_1.append(bin[-1])
            bin.pop(-1)
    if (choice == '2'):
        if (posable_on_color(bin[-1], row_2)):
            row_2.append(bin[-1])
            bin.pop(-1)
    if (choice == '3'):
        if (posable_on_color(bin[-1], row_3)):
            row_3.append(bin[-1])
            bin.pop(-1)
    if (choice == '4'):
        if (posable_on_color(bin[-1], row_4)):
            row_4.append(bin[-1])
            bin.pop(-1)
    if (choice == '5'):
        if (posable_on_color(bin[-1], row_5)):
            row_5.append(bin[-1])
            bin.pop(-1)
    if (choice == '6'):
        if (posable_on_color(bin[-1], row_6)):
            row_6.append(bin[-1])
            bin.pop(-1)
    
    if (choice == 'coeur'):
        if (posable_on_family(bin[-1], fam_c, 'c')):
            fam_c.append(bin[-1])
            bin.pop(-1)
    if (choice == 'carreau'):
        if (posable_on_family(bin[-1], fam_k, 'k')):
            fam_k.append(bin[-1])
            bin.pop(-1)
    if (choice == 'trefle'):
        if (posable_on_family(bin[-1], fam_t, 't')):
            fam_t.append(bin[-1])
            bin.pop(-1)
    if (choice == 'pique'):
        if (posable_on_family(bin[-1], fam_p, 'p')):
            fam_p.append(bin[-1])
            bin.pop(-1)


#verifie si on peux poser la carte
def posable_on_color(card, stack):
    if (len(stack) == 0):
        print("posable")
        return True

    else:
        number_card = int(card[1])    #numéro de la carte
        if (card[0] == 1):
            number_card = 10
        else:
            number_card = int(card[1])

        if (stack[-1][0] == 1):     #numéro de la dernière carte du tas
            number_stack = 10
        else:
            number_stack = int(stack[-1][1])
            
        
        color_card = card[-1]       #couleur de la carte ('R' ou 'N')
        color_stack = stack[-1][-1] #couleur de la dernière carte du tas

        
        print("number card =", number_card, "| number stack =", number_stack)
        print("color card =", color_card, "| color stack =", color_stack)
        

        if(number_stack == 1):
            print("non posable")
            return False


        if(color_card != color_stack):
            if(number_card == number_stack - 1):
                print("posable")
                return True
    

    print("non posable")
    return False

#verifie si on peux poser la carte
def posable_on_family(card, stack, fam):
    if (len(stack) == 10):
        print("non posable")
        return False

    elif (len(stack) == 0):
        '''
        print("famille card = ", card[-2], " | famille stack = ", fam)
        print("number_card = ", card[1], " | number stack = ", 1)
        '''
        if (card[-2] == fam and card[1] == '1'):
            print("posable")
            return True
        

    else:
        number_card = int(card[1])    #numéro de la carte
        if (card[0] == 1):
            number_card = 10
        else:
            number_card = int(card[1])

        if (stack[-1][0] == 1):     #numéro de la dernière carte du tas
            number_stack = 10
        else:
            number_stack = int(stack[-1][1])
        
        
        fam_card = card[-2]       #famille de la carte ('c' ou 'k' ou 't' ou 'p')
        fam_stack = stack[-1][-2] #famille de la dernière carte du tas

        '''
        print("number card = ", number_card, " | number stack = ", number_stack)
        print("famille card = ", fam_card, " | famille stack = ", fam_stack)
        '''




        if(fam_card == fam_stack):
            if(number_card == number_stack + 1):
                print("posable")
                return True
        


    print("non posable")
    return False




def prendre():
    pass









#reveal new card non has visible
def reveal_new_card(row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6):
    if (hide_1 >= len(row_1)) :
        hide_1 = len(row_1) - 1
    if (hide_2 >= len(row_2)) :
        hide_2 = len(row_2) - 1
    if (hide_3 >= len(row_3)) :
        hide_3 = len(row_3) - 1
    if (hide_4 >= len(row_4)) :
        hide_4 = len(row_4) - 1
    if (hide_5 >= len(row_5)) :
        hide_5 = len(row_5) - 1
    if (hide_6 >= len(row_6)) :
        hide_6 = len(row_6) - 1

    return hide_1, hide_2, hide_3, hide_4, hide_5, hide_6

#verifie si les tas des familles sont pleines
def verif_victory(fam_c, fam_k, fam_t, fam_p):
    c = len(fam_c)
    k = len(fam_k)
    t = len(fam_t)
    p = len(fam_p)

    if(c == 10 and k == 10 and t == 10 and p == 10):
        return True
    else:
        return False

#----------------------------
#------------FIN-------------
#-----------Game-------------
#----------------------------













#----------------------------
#----------------------------
#-----------MAIN-------------
#----------------------------


def main():
    #pioche
    pioche = [] #stock les cartes qui ne sont pas sur le terrain
    #defausse
    bin = [] #stock les carte défaussée (la dernière est la carte à jouer)

    #le tas à déplacer
    to_move = []

    #tas de cartes de la zone couleurs
    row_1 = []       #stock les cartes du xieme tas couleur
    hide_1 = 0   #indique le nombre de cartes à ne pas afficher

    row_2 = []
    hide_2 = 1

    row_3 = []
    hide_3 = 2

    row_4 = []
    hide_4 = 3

    row_5 = []
    hide_5 = 4

    row_6 = []
    hide_6 = 5

    #tas de cartes de la zone famille
    fam_c = []  #coeur
    
    fam_k = []  #carreau
    
    fam_t = []  #trefle
    
    fam_p = []  #pique


    victory = False

    card = '    ' #carte actuelle à poser

    choice = ''  #choix du joueur, contient d'abord un entier entre 0 et 2, puis si besoin, plusieurs charactères (représentant des coordonnées)



    #initialisation
    pioche, row_1, row_2, row_3, row_4, row_5, row_6 = init(pioche, row_1, row_2, row_3, row_4, row_5, row_6)


    


    #game

    while(not victory):
        remaining_card = len(bin) + len(pioche)

        print_game(pioche, bin, row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6, fam_c, fam_k, fam_t, fam_p)

        choice = choix()
        #repiocher
        if (choice == '0'):
            if (remaining_card != 0):
                if (len(pioche) == 0):
                    pioche = bin
                    bin = []

                bin.append(pioche[0])
                pioche.pop(0)
        #poser
        elif (choice == '1' and len(bin) != 0):
            print_game(pioche, bin, row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6, fam_c, fam_k, fam_t, fam_p)
            choice = choix_poser()
            poser(choice, bin, row_1, row_2, row_3, row_4, row_5, row_6, fam_c, fam_k, fam_t, fam_p)
        #prendre
        elif (choice == '2'):
            print_game(pioche, bin, row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6, fam_c, fam_k, fam_t, fam_p)
            choice = choix_prendre()
        






        

    
        #reveal the next card of a row if the last visible has moved
        hide_1, hide_2, hide_3, hide_4, hide_5, hide_6 = reveal_new_card(row_1, hide_1, row_2, hide_2, row_3, hide_3, row_4, hide_4, row_5, hide_5, row_6, hide_6)

        victory = verif_victory(fam_c, fam_k, fam_t, fam_p)


        #if(len(pioche) == 0):
        #    victory = True
    

    print("Partie terminée")


if __name__ == "__main__":
    main()
