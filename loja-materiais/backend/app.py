from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Fornecedor, Produto, Cliente, Venda, ItemVenda  # Importando os modelos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/loja_materiais'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Inicializando o db

with app.app_context():
    db.create_all()  # Cria as tabelas
QLAlchemy(app)
CORS(app)

# Modelos
class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False)
    unidade_medida = db.Column(db.String(20))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))

# Rotas
@app.route('/fornecedores', methods=['GET', 'POST'])
def manage_fornecedores():
    if request.method == 'POST':
        data = request.json
        novo_fornecedor = Fornecedor(**data)
        db.session.add(novo_fornecedor)
        db.session.commit()
        return jsonify(novo_fornecedor.id), 201
    fornecedores = Fornecedor.query.all()
    return jsonify([{ 'id': f.id, 'nome': f.nome } for f in fornecedores])

@app.route('/produtos', methods=['GET', 'POST'])
def manage_produtos():
    if request.method == 'POST':
        data = request.json
        novo_produto = Produto(**data)
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify(novo_produto.id), 201
    produtos = Produto.query.all()
    return jsonify([{ 'id': p.id, 'nome': p.nome, 'preco': str(p.preco) } for p in produtos])

if __name__ == '__main__':
    db.create_all()  # Cria as tabelas
    app.run(debug=True)
