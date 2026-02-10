import tkinter as tk
from tkinter import ttk
from logic import validate_login

class LoginApp:
    '''
    Docstring for LoginApp

        :param root: Description
    '''
    def __init__(self, root):
        self.root = root
        self.root.title('System Mars Landing')
        self.root.geometry('400x300')

        # Variáveis do Tkinter (boas práticas de sincronização) 
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        '''
        Docstring for create_widgets
        
        :param self: Description
        '''
        # Usando Grid para melhor organização dos widgets
        tk.Label(self.root, text='User:').grid(row=0, 
                                               column=0, padx=10, pady=10)
        tk.Entry(self.root, 
                 textvariable=self.user_var).grid(row=0, column=1)

        tk.Label(self.root, text='Password:').grid(row=1, 
                                                   column=0, padx=10, pady=10)
        tk.Entry(self.root, 
                 textvariable=self.pass_var, show='*').grid(row=1, column=1)

        # Botão com comando para lidar com o login
        tk.Button(self.root, text='Login', 
                  command=self.handle_login).grid(row=2, columnspan=2)

    def handle_login(self):
        '''
        Docstring for handle_login
        
        :param self: Description 
        '''
        user = self.user_var.get()
        password = self.pass_var.get()
        validate_login(user=user, password=password)