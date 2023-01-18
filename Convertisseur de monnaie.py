import tkinter as tk

Liste_entree = ["Dollar US", "Euro", "Livre Sterling", "Yen", "Yuan", "Dinar Tunisien"]

Liste_vers = ["Dollar US", "Euro", "Livre Sterling", "Yen", "Yuan", "Dinar Tunisien"]

Historique = []


def conversion():

    entree = variable.get()
    vers = variable1.get()

    montant = float(e1.get())

    # Conversion avec base dollar

    if entree == 'Dollar US' and vers == 'Euro':
        total = montant * 0.92
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')

    elif entree == "Dollar US" and vers == "Livre Sterling":
        total = montant * 0.82
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    elif entree == "Dollar US" and vers == "Yen":
        total = montant * 128.90
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')

    elif entree == "Dollar US" and vers == "Yuan":
        total = montant * 6.78
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yuan')
        Historique.append('\n')

    elif entree == "Dollar US" and vers == "Dinar Tunisien":
        total = montant * 3.07
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisien')
        Historique.append('\n')

    elif entree == "Dollar US" and vers == "Dollar US":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Dollars')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollars US')
        Historique.append('\n')

    # Conversion avec base Euro

    elif entree == "Euro" and vers == "Dollar US":
        total = montant * 1.08
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollar US')
        Historique.append('\n')

    elif entree == "Euro" and vers == "Livre Sterling":
        total = montant * 0.89
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    elif entree == "Euro" and vers == "Yen":
        total = montant * 139.37
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')


    elif entree == "Euro" and vers == "Yuan":
        total = montant * 7.33
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yuan')
        Historique.append('\n')


    elif entree == "Euro" and vers == "Dinar Tunisien":
        total = montant * 3.32
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisien')
        Historique.append('\n')


    elif entree == "Euro" and vers == "Euro":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Euro')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')


    # Conversion avec base Livre Sterling

    elif entree == "Livre Sterling" and vers == "Dollar US":
        total = montant * 1.22
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollar US')
        Historique.append('\n')


    elif entree == "Livre Sterling" and vers == "Euro":
        total = montant * 1.13
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')

    elif entree == "Livre Sterling" and vers == "Yen":
        total = montant * 157.25
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')

    elif entree == "Livre Sterling" and vers == "Yuan":
        total = montant * 8.27
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yuan')
        Historique.append('\n')

    elif entree == "Livre Sterling" and vers == "Dinar Tunisien":
        total = montant * 3.75
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisien')
        Historique.append('\n')

    elif entree == "Livre Sterling" and vers == "Livre Sterling":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Livre Sterling')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    # Conversion avec base Yen

    elif entree == "Yen" and vers == "Dollar US":
        total = montant * 0.0078
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollar US')
        Historique.append('\n')

    elif entree == "Yen" and vers == "Euro":
        total = montant * 0.0072
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')

    elif entree == "Yen" and vers == "Livre Sterling":
        total = montant * 0.0064
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    elif entree == "Yen" and vers == "Yuan":
        total = montant * 0.053
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yuan')
        Historique.append('\n')

    elif entree == "Yen" and vers == "Dinar Tunisien":
        total = montant * 0.024
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisien')
        Historique.append('\n')

    elif entree == "Yen" and vers == "Yen":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Yen')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')

    # Conversion avec base Yuan

    elif entree == "Yuan" and vers == "Dollar US":
        total = montant * 0.15
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollar US')
        Historique.append('\n')

    elif entree == "Yuan" and vers == "Euro":
        total = montant * 0.14
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')

    elif entree == "Yuan" and vers == "Livre Sterling":
        total = montant * 1.12
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    elif entree == "Yuan" and vers == "Yen":
        total = montant * 19.01
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')

    elif entree == "Yuan" and vers == "Dinar Tunisien":
        total = montant * 0.45
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisinen')
        Historique.append('\n')

    elif entree == "Yuan" and vers == "Yuan":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Yuan')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisien')
        Historique.append('\n')
        
    # Conversion avec base Dinar Tunisien

    elif entree == "Dinnar Tunisien" and vers == "Dollar US":
        total = montant * 0.33
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dollard US')
        Historique.append('\n')

    elif entree == "Dinnar Tunisien" and vers == "Euro":
        total = montant * 0.30
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Euro')
        Historique.append('\n')

    elif entree == "Dinnar Tunisien" and vers == "Livre Sterling":
        total = montant * 0.27
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Livre Sterling')
        Historique.append('\n')

    elif entree == "Dinnar Tunisien" and vers == "Yen":
        total = montant * 41.99
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yen')
        Historique.append('\n')

    elif entree == "Dinnar Tunisien" and vers == "Yuan":
        total = montant * 2.21
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Yuan')
        Historique.append('\n')

    elif entree == "Dinnar Tunisien" and vers == "Dinar Tunisien":
        total = montant * 1
        Historique.append(montant)
        Historique.append('Dinar Tunisien')
        Historique.append('=')
        Historique.append(total)
        Historique.append('Dinar Tunisen')
        Historique.append('\n')

    print(Historique)
    tk.Label(fenetre, text=Historique, bg='#d8dfe3', fg='black', width=35, height=5).place(x=10, y=200)

    text.set(total)


fenetre = tk.Tk()
fenetre.geometry('300x300')
fenetre.title("Convertisseur de Monnaie")

variable = tk.StringVar(fenetre)
variable.set(Liste_entree[0])

opt = tk.OptionMenu(fenetre, variable, *Liste_entree)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")


variable1 = tk.StringVar(fenetre)
variable1.set(Liste_vers[0])

opt = tk.OptionMenu(fenetre, variable1, *Liste_vers)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")

global e1
global text
text = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 10), fg='green')
labelTest.pack(side="top")


tk.Label(fenetre, text="Entrée").place(x=10, y=10)
tk.Label(fenetre, text="Vers").place(x=10, y=40)
tk.Label(fenetre, text="Montant").place(x=10, y=80)
tk.Label(fenetre, text="Historique :").place(x=10, y=180)


tk.Label(fenetre, text="Résultat :").place(x=10, y=150)
tk.Label(fenetre, text="", font=('Helvetica', 10), fg='green', textvariable=text).place(x=100, y=150)
tk.Button(fenetre, text="Convertir", command=conversion, height=1, width=9).place(x=100, y=110)

e1 = tk.Entry(fenetre)
e1.place(x=87, y=80)


fenetre.mainloop()
