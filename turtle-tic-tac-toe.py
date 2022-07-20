from turtle import *

side = 50
def field():
    for counter in range(4):
        fd(side) #fd = forward
        left(90)

def board():
    for counter in range(3):
        for counter2 in range(3):
            pd() #opuść pisak
            field()
            pu() #podnieś pisak
            fd(side) #przesuwa się rysik o długość boku bo inaczej kwadrat skończyłby w punkcie wyjścia
        bk(3*side) #back 3 długości boku
        left(90)
        fd(side)
        right(90)  
board()

    #x - kolumny
    #y - wiersze

def X(a,b):
    #stawianie krzyzyka, a-kolumna planszy (może być 0,1,2 dla kolumn 1,2,3 : z lewa do prawej), b-wiersz planszy (może być 0,1,2 dla wierszy 1,2,3 - ale one ida do gory jak w ukl wspolrzednynch)
    pu() #podnosimy pisak
    setx(a*side + side/2) #wspolrzedne na osi x (0/1/2 * 200 (tutaj, jw) + 200/2 = 100, czyli środek daszku kwadratu wychodzącego z punktu planszy 0,0)
    sety(b*side + side/2) #wspolrzedne na osi y (to samo, ale z kolumnami)
    pd() #opuszczaqmy pisak
    #rysujemy X, jako pętla for x4 z centralnego punktu danego kwadratu
    left(45) #kąt 45st w lewo obraca sie zolw/pisak
    for i in range(4):
        fd(side/4) #/4 żeby ten X cały się mieścił w kwadracie
        bk(side/4)
        left(90)
    right(45)
    pu()
X(1,2) #przykładowa pozycja krzyżyka gdzie ma się zaznaczyć

def O(a,b):
    #stawianie krzyzyka, a-kolumna planszy (może być 0,1,2 dla kolumn 1,2,3 : z lewa do prawej), b-wiersz planszy (może być 0,1,2 dla wierszy 1,2,3 - ale one ida do gory jak w ukl wspolrzednynch)
    pu() #podnosimy pisak
    setx(a*side + side/2) #wspolrzedne na osi x (0/1/2 * 200 (tutaj, jw) + 200/2 = 100, czyli środek daszku kwadratu wychodzącego z punktu planszy 0,0)
    sety(b*side + side/2 - 15) #wspolrzedne na osi y (to samo, ale z kolumnami) #odjęłam 15 na czuja, bo zaczyna rysować kółko nie z centralnego punktu tylko ten punkt jest na obwodzie, więc obniżyłam skąd zaczyna rysować kółko
    pd() #opuszczaqmy pisak
    circle(15,360,30)
    pu()
    
O(2,0)
    
exitonclick()
