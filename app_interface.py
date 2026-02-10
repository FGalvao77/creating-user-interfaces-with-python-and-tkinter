import tkinter as tk
from tkinter import ttk
from logic import validate_login

class LoginApp:
    '''
    Class responsible for managing the graphical login interface.

    Attributes:
        root (tk.Tk): The main application window.
        user_var (tk.StringVar): Control variable for the username field.
        pass_var (tk.StringVar): Control variable for the password field.
    '''
    def __init__(self, root):
        '''
        Initializes the login interface and configures the widgets.

        Args:
            root (tk.Tk): Instance of the Tk interpreter.
        '''
        self.root = root
        self.root.title('System Mars Landing')
        self.root.geometry('400x300')

        # Variáveis do Tkinter (boas práticas de sincronização) 
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        '''
        It builds and positions visual elements in the window using Grid.
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
        username = self.user_var.get()
        password = self.pass_var.get()
        validate_login(username=username, password=password)