# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:27:42 2019

@author: misalamon
"""
print("KALKULATOR")

class cal():
def __int__(self,x,y):
    self.x=x
    self.y=y

def dodawanie(self):
   return self.x+self.y
 
def odejmowanie(self):
   return self.x-self.y
 
def mnozenie(self):
   return self.x*self.y
 
def dzielenie(self):
   return self.x/self.y
 
def potegowanie(self):
    return self.x ** self.y
 
 
wyjscie = False
while wyjscie == False:
 
    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - potegowanie")
    print("6 - wyjscie")
 
    choice = input("Wybierz (1/2/3/4/5/6):")
 
    if choice == '6':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5/6):")
 
    x= float(input("Podaj liczbe: "))
    y = float(input("Podaj liczbe: "))
 
    if choice == '1':
         print(x,"+",y,"=", dodawanie(x,y))
 
    elif choice == '2':
        print(x,"-",y,"=", odejmowanie(x,y))
 
    elif choice == '3':
         print(x,"*",y,"=", mnozenie(x,y))
 
    elif choice == '4':
         print(x,"/",y,"=", dzielenie(x,y))
 
    elif choice == '5':
        print(x,"**",y,"=", potegowanie(x,y))
 
    else:
     print("Wybraleś nieistniejącą opcje!")