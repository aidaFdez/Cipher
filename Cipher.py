import tkinter as tk

abc = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K',
    'l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w', 'W',
    'x','X','y', 'Y','z', 'Z']

#Uses the Caesar cipher. It shifts the letters the times given.
def caesar (input, num):
    ciphered = ""
    for letter in input:
        if letter in abc:
            ind = abc.index(letter)
            ciphered = ciphered + abc[(ind+(num*2) )%52]
        else:
            ciphered = ciphered + letter
    return ciphered

#Uses the Vigènere cipher. It uses a square table, which in essence is just applying Caesar a different number of times
#depending on the letter of the keyword being used at the moment.
def vigenere (input, keyword):
    ciphered = ""
    i = 0
    while i <len(input):
        for letter in input:
            if letter in abc:
                ciphered = ciphered + caesar(letter, round((abc.index(keyword[i%len(keyword)])/2)))
            else:
                ciphered = ciphered + letter
            i = i+1
    return ciphered

window = tk.Tk()

mPrinc = tk.Message(window, text = "Hi! Fill in the necessary data and then choose the kind of ciphering you want!")
mPrinc.config(font = ('times', 12), width = 1000)
mPrinc.pack()

window.mainloop()
