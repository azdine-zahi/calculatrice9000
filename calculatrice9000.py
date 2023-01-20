import tkinter as tk

def calculer():
    expression = input_box.get()
    try:
        resultat = eval(expression)
        input_box.delete(0,tk.END)
        input_box.insert(0,resultat)
        resultat_label.config(text=resultat)
        history_list.append(expression+"="+str(resultat))
    except:
        resultat_label.config(text="Entrée Invalide")

def ajouter_chiffre(chiffre):
    input_box.insert(tk.END, chiffre)

def ajouter_operateur(operateur):
    input_box.insert(tk.END, operateur)

def supprimer():
    input_box.delete(0, tk.END)
    resultat_label.config(text="")

def racine_carree():
    input_box.insert(tk.END, "**0.5")

def pourcentage():
    input_box.insert(tk.END, "/100")

def supprimer_dernier_caractere():
    input_box.delete(len(input_box.get())-1)

def ajouter_parenthese(parenthese):
    input_box.insert(tk.END, parenthese)

def factorial_button_clicked():
    number = input_box.get()
    try:
        resultat = 1
        for i in range(1, int(number) + 1):
            resultat *= i
        input_box.delete(0,tk.END)
        input_box.insert(0,resultat)
        resultat_label.config(text=resultat)
    except:
        resultat_label.config(text="Entrée Invalide")

def au_carre():
    input_box.insert(tk.END, "**2")

def ajouter_mod():
    input_box.insert(tk.END, "%")

def ajouter_signe():
    if input_box.get()[0] == "-":
        input_box.delete(0)
    else:
        input_box.insert(0, "-")

history_list = []
def afficher_historique():
    history_label = tk.Label(fenetre, text="Historique :")
    history_label.grid(row=8,column=0)
    for i, history in enumerate(history_list):
        history_button = tk.Button(fenetre, text=history, width=15, height=1, command=lambda: input_box.insert(0, history))
        history_button.grid(row=9+i,column=0, columnspan=5)

def clear_history():
    for widget in fenetre.grid_slaves():
        if int(widget.grid_info()["row"]) > 7:
            widget.destroy()
    history_list.clear()


def inverse():
    number = input_box.get()
    try:
        resultat = 1/float(number)
        input_box.delete(0,tk.END)
        input_box.insert(0,resultat)
        resultat_label.config(text=resultat)
    except:
        resultat_label.config(text="Entrée Invalide")





fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.configure(bg='#5E5E5E')

resultat_label = tk.Label(fenetre, text="")
resultat_label.grid(row=0, column=0)

input_box = tk.Entry(fenetre, width=60, borderwidth=5)
input_box.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=20)


# Lignes de boutons numériques
bouton_1 = tk.Button(fenetre, text="1", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(1))
bouton_2 = tk.Button(fenetre, text="2", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(2))
bouton_3 = tk.Button(fenetre, text="3", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(3))
bouton_4 = tk.Button(fenetre, text="4", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(4))
bouton_5 = tk.Button(fenetre, text="5", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(5))
bouton_6 = tk.Button(fenetre, text="6", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(6))
bouton_7 = tk.Button(fenetre, text="7", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(7))
bouton_8 = tk.Button(fenetre, text="8", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(8))
bouton_9 = tk.Button(fenetre, text="9", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(9))
bouton_0 = tk.Button(fenetre, text="0", width=10, height=3, bg='#7D7D7D', command=lambda: ajouter_chiffre(0))
bouton_point = tk.Button(fenetre, text=".", width=10, height=3, command=lambda: ajouter_chiffre("."))
bouton_supprimer = tk.Button(fenetre, text="\U0000232B", width=10, height=3, command=supprimer_dernier_caractere)
bouton_parenth_ouvrante = tk.Button(fenetre, text="(", width=10, height=3, command=lambda: ajouter_parenthese("("))
bouton_parenth_fermante = tk.Button(fenetre, text=")", width=10, height=3, command=lambda: ajouter_parenthese(")"))
bouton_factorial = tk.Button(fenetre, text="!", width=10, height=3, command=factorial_button_clicked)
bouton_pi = tk.Button(fenetre, text="π", width=10, height=3, command=lambda: ajouter_chiffre(3.14159265358979323846))
bouton_mod = tk.Button(fenetre, text="mod", width=10, height=3, command=ajouter_mod)
bouton_signe = tk.Button(fenetre, text="+/-", width=10, height=3, command=ajouter_signe)


bouton_history = tk.Button(fenetre, text="History", width=10, height=3, bg='yellow', command=afficher_historique)
clear_history_button = tk.Button(fenetre, text="Clear History", width=10, height=3, bg='red', command=clear_history)
bouton_inverse = tk.Button(fenetre, text="1/x", width=10, height=3, command=inverse)


bouton_1.grid(row=6, column=1)
bouton_2.grid(row=6, column=2)
bouton_3.grid(row=6, column=3)
bouton_4.grid(row=5, column=1)
bouton_5.grid(row=5, column=2)
bouton_6.grid(row=5, column=3)
bouton_7.grid(row=4, column=1)
bouton_8.grid(row=4, column=2)
bouton_9.grid(row=4, column=3)
bouton_0.grid(row=7, column=2)
bouton_supprimer.grid(row=5, column=3)
bouton_point.grid(row=7, column=3)




# Lignes de boutons d'opérateurs
bouton_add = tk.Button(fenetre, text="+", width=10, height=3, bg='orange', command=lambda: ajouter_operateur("+"))
bouton_sub = tk.Button(fenetre, text="-", width=10, height=3, bg='orange', command=lambda: ajouter_operateur("-"))
bouton_mul = tk.Button(fenetre, text="*", width=10, height=3, bg='orange', command=lambda: ajouter_operateur("*"))
bouton_div = tk.Button(fenetre, text="/", width=10, height=3, bg='orange', command=lambda: ajouter_operateur("/"))
bouton_equal = tk.Button(fenetre, text="=", width=10, height=3, bg='yellow', command=calculer)
bouton_clear = tk.Button(fenetre, text="C", width=10, height=3, command=supprimer)
bouton_sqrt = tk.Button(fenetre, text="√", width=10, height=3, command=racine_carree)
bouton_percent = tk.Button(fenetre, text="%", width=10, height=3, command=pourcentage)
bouton_carre = tk.Button(fenetre, text="x²", width=10, height=3, command=au_carre)

bouton_add.grid(row=6, column=4)
bouton_sub.grid(row=5, column=4)
bouton_mul.grid(row=4, column=4)
bouton_div.grid(row=3, column=4)
bouton_equal.grid(row=7, column=4)
bouton_clear.grid(row=1, column=3)
bouton_sqrt.grid(row=3, column=0)
bouton_percent.grid(row=1, column=2)
bouton_supprimer.grid(row=1, column=4)
bouton_parenth_ouvrante.grid(row=3, column=1)
bouton_parenth_fermante.grid(row=3, column=2)
bouton_factorial.grid(row=3, column=3)
bouton_carre.grid(row=1, column=0)
bouton_pi.grid(row=4, column=0)
bouton_mod.grid(row=5, column=0)
bouton_signe.grid(row=6, column=0)

bouton_history.grid(row=7, column=0)
clear_history_button.grid(row=7,column=1)

bouton_inverse.grid(row=1,column=1)


fenetre.mainloop()