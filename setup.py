import tkinter as tk
import uuid
import webbrowser

menu_inicial = tk.Tk()
menu_inicial.title("By:FilipePagodeiro")
menu_inicial.geometry('300x150')
menu_inicial.resizable(False, False)
menu_inicial.iconbitmap("imgs/icon2.ico")

def senha_aleatoria(string_length=10):
    """Retorna um string aleatoria em string_length."""
    random = str(uuid.uuid4())  
    random = random.replace("-","") 
    return random[0:string_length] 

def abrir_img():
    site = 'https://prnt.sc/' + senha_aleatoria(6)
    abrir_site = webbrowser.open(site, new=0, autoraise=True)
    return abrir_site

cmd = tk.Button(menu_inicial, text='Clique aqui para abrir uma imagem aleatoria', command=abrir_img, bg='black', fg='#00FF00', width= 150, height= 75)
cmd.pack()

menu_inicial.mainloop()

input("Pressione enter")
