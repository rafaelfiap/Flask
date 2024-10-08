from flask import Flask, jsonify, request
app = Flask(__name__)
# Lista de funcionários
funcionarios = [
    {'id': 1, 'nome': 'Ana', 'idade': 28, 'salario': 3500.00},
    {'id': 2, 'nome': 'Bruno', 'idade': 34, 'salario': 4200.50},
    {'id': 3, 'nome': 'Carla', 'idade': 26, 'salario': 3000.00},
    {'id': 4, 'nome': 'Diego', 'idade': 40, 'salario': 5000.00},
    {'id': 5, 'nome': 'Elisa', 'idade': 22, 'salario': 2800.75},
    {'id': 6, 'nome': 'Fabio', 'idade': 38, 'salario': 4500.00},
    {'id': 7, 'nome': 'Gabriela', 'idade': 30, 'salario': 3700.00}
]


# Rota Home
@app.route('/')
def home():
    return "API está ativa"

# Rota para consultar todos os funcionários
@app.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(funcionarios)

# Rota para consultar um funcionário pelo nome
@app.route('/funcionarios/<string:nome>', methods=['GET'])
def get_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario['nome'].lower() == nome.lower():
            return jsonify(funcionario)
    return jsonify({'erro': 'Funcionário não encontrado'}), 404

# Rota para inserir um novo funcionário
@app.route('/funcionarios', methods=['POST'])
def add_funcionario():
    novo_funcionario = request.get_json()
    funcionarios.append(novo_funcionario)
    return jsonify(funcionarios), 201

# Rota para alterar um funcionário
@app.route('/funcionarios/<string:nome>', methods=['PUT'])
def update_funcionario(nome):
    dados_atualizados = request.get_json()
    for funcionario in funcionarios:
        if funcionario['nome'].lower() == nome.lower():
            funcionario.update(dados_atualizados)
            return jsonify(funcionarios)
    return jsonify({'erro': 'Funcionário não encontrado'}), 404

# Rota para excluir um funcionário
@app.route('/funcionarios/<string:nome>', methods=['DELETE'])
def delete_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario['nome'].lower() == nome.lower():
            funcionarios.remove(funcionario)
            return jsonify(funcionarios)
    return jsonify({'erro': 'Funcionário não encontrado'}), 404


if __name__ == '__main__':
    app.run()
