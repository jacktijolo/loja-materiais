from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<Fornecedor {self.nome}>'

class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False)
    unidade_medida = db.Column(db.String(20))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))

    fornecedor = db.relationship('Fornecedor', backref='produtos')

    def __repr__(self):
        return f'<Produto {self.nome}>'

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<Cliente {self.nome}>'

class Venda(db.Model):
    __tablename__ = 'vendas'
    
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    data_venda = db.Column(db.DateTime, default=db.func.current_timestamp())
    total = db.Column(db.Numeric(10, 2), nullable=False)

    cliente = db.relationship('Cliente', backref='vendas')

    def __repr__(self):
        return f'<Venda {self.id}>'

class ItemVenda(db.Model):
    __tablename__ = 'itens_venda'
    
    id = db.Column(db.Integer, primary_key=True)
    venda_id = db.Column(db.Integer, db.ForeignKey('vendas.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    venda = db.relationship('Venda', backref='itens')
    produto = db.relationship('Produto', backref='itens_venda')

    def __repr__(self):
        return f'<ItemVenda {self.id}>'
