import tkinter as tk

abc = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K',
    'l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w', 'W',
    'x','X','y', 'Y','z', 'Z']

#Uses the Caesar encryption. It shifts the letters
def caesar (input, num):
    crypted = ""
    for letter in input:
        if letter in abc:
            ind = abc.index(letter)
            crypted = crypted + abc[(ind+(num*2) )%52]
        else:
            crypted = crypted + letter
    return crypted
