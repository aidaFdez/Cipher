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
window.geometry("500x200")

mPrinc = tk.Message(window, text = "Hi! Fill in the necessary data and then choose the kind of ciphering you want! \n")
mPrinc.config(width = 200)
mPrinc.grid()

msg = tk.Message(window, text = "Text to cipher ")
msg.config(width = 100)
msg.grid()
toCip = tk.Entry(window)
toCip.grid(sticky = "w", row = 1, column = 1)

msgC = tk.Message(window, text = "Number (only Caesar) ")
msgC.grid(row = 2, column = 0)
caesarN = tk.Entry(window)
caesarN.grid(row = 2, column = 1)

msgV = tk.Message(window, text = "Key (only Vigenere) ")
msgV.grid(row = 3)
vigKey = tk.Entry(window)
vigKey.grid(row = 3, column = 1)


window.mainloop()
