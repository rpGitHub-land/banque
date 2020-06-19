from Tkinter import *
fenetre = Tk()

var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()


fenetre.mainloop()