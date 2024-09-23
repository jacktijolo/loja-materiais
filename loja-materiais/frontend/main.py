import tkinter as tk
from tkinter import messagebox
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Loja de Materiais")
        
        # Fornecedores
        self.label_fornecedor = tk.Label(root, text="Nome do Fornecedor:")
        self.label_fornecedor.pack()
        self.entry_fornecedor = tk.Entry(root)
        self.entry_fornecedor.pack()
        
        self.button_add_fornecedor = tk.Button(root, text="Adicionar Fornecedor", command=self.add_fornecedor)
        self.button_add_fornecedor.pack()

        # Produtos
        self.label_produto = tk.Label(root, text="Nome do Produto:")
        self.label_produto.pack()
        self.entry_produto = tk.Entry(root)
        self.entry_produto.pack()

        self.label_preco = tk.Label(root, text="Preço do Produto:")
        self.label_preco.pack()
        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        self.button_add_produto = tk.Button(root, text="Adicionar Produto", command=self.add_produto)
        self.button_add_produto.pack()

    def add_fornecedor(self):
        nome = self.entry_fornecedor.get()
        if nome:
            response = requests.post("http://localhost:5000/fornecedores", json={"nome": nome})
            if response.status_code == 201:
                messagebox.showinfo("Sucesso", "Fornecedor adicionado!")
            else:
                messagebox.showerror("Erro", "Falha ao adicionar fornecedor.")
        else:
            messagebox.showwarning("Atenção", "Preencha o nome do fornecedor.")

    def add_produto(self):
        nome = self.entry_produto.get()
        preco = self.entry_preco.get()
        if nome and preco:
            try:
                preco = float(preco)
                response = requests.post("http://localhost:5000/produtos", json={"nome": nome, "preco": preco, "quantidade_estoque": 50, "categoria": "Material", "unidade_medida": "kg"})
                if response.status_code == 201:
                    messagebox.showinfo("Sucesso", "Produto adicionado!")
                else:
                    messagebox.showerror("Erro", "Falha ao adicionar produto.")
            except ValueError:
                messagebox.showwarning("Atenção", "Preço deve ser um número.")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
