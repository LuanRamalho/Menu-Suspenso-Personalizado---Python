import tkinter as tk
from tkinter import messagebox

# Função para mostrar a opção selecionada
def select_option(option_text):
    dropdown_button.config(text=option_text)
    dropdown_menu.place_forget()  # Esconde o menu suspenso após selecionar a opção

# Função para alternar a exibição do menu suspenso
def toggle_dropdown(event):
    if dropdown_menu.winfo_ismapped():
        dropdown_menu.place_forget()  # Esconde o menu
    else:
        dropdown_menu.place(x=dropdown_button.winfo_x(), y=dropdown_button.winfo_y() + dropdown_button.winfo_height())  # Mostra o menu

# Configuração da janela principal
root = tk.Tk()
root.title("Menu Suspenso Personalizado")
root.geometry("400x500")
root.config(bg="#f4f4f9")

# Criando o botão do menu suspenso
dropdown_button = tk.Button(root, text="Selecione uma opção", font=("Poppins", 14), bg="#6200ea", fg="white", width=20, height=2, borderwidth=0, relief="solid", command=lambda: toggle_dropdown(None))
dropdown_button.pack(pady=100)

# Criando o menu suspenso
dropdown_menu = tk.Frame(root, bg="white", bd=1, relief="solid", width=200)

# Adicionando as opções ao menu
options = ["Rio de Janeiro", "Londres", "Tóquio", "Paris", "Veneza", "São Paulo", "Nova York", "Pequim"]
for option in options:
    item = tk.Button(dropdown_menu, text=option, font=("Poppins", 12), bg="#ffffff", fg="#333333", relief="flat", anchor="w", width=18, height=2, command=lambda opt=option: select_option(opt))
    item.pack(fill="x")

# Iniciar o loop principal
root.mainloop()
