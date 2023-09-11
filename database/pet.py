"""from sanic import Sanic, response
from sanic.exceptions import NotFound
from pymongo import MongoClient
from bson import ObjectId
import asyncio

if __name__ == "__main__":
    app = Sanic(__name__)

# Configuração da conexão com o MongoDB
async def configure_db():
    client = MongoClient("mongodb://localhost:27017")  # Use a URL de conexão correta
    app.config.db = client.my_petshop_database  # Substitua pelo nome do seu banco de dados

# Middleware para conectar-se ao MongoDB antes de cada solicitação
@app.listener('before_server_start')
async def setup_db(app, loop):
    await configure_db()

# Modelo de dados para animais de estimação
class Pet:
    def __init__(self, nome, tipo, data_nascimento, status_vacinacao, bairro):
        self.nome = nome
        self.tipo = tipo
        self.data_nascimento = data_nascimento
        self.status_vacinacao = status_vacinacao
        self.bairro = bairro

# Rota para criar um novo pet
@app.route('/pets', methods=['POST'])
async def criar_pet(request):
    data = request.json
    db = app.config.db
    novo_pet = Pet(**data)
    result = await db.pets.insert_one(novo_pet.__dict__)
    return response.json({'mensagem': 'Pet criado com sucesso!', 'id': str(result.inserted_id)}, status=201)

# Rota para listar todos os pets
@app.route('/pets', methods=['GET'])
async def listar_pets(request):
    db = app.config.db
    pets = await db.pets.find().to_list(None)
    lista_pets = []
    for pet in pets:
        lista_pets.append({
            'id': str(pet['_id']),
            'nome': pet['nome'],
            'tipo': pet['tipo'],
            'data_nascimento': pet['data_nascimento'],
            'status_vacinacao': pet['status_vacinacao'],
            'bairro': pet['bairro']
        })
    return response.json(lista_pets)

# Rota para buscar um pet por ID
@app.route('/pets/<string:id>', methods=['GET'])
async def buscar_pet(request, id):
    db = app.config.db
    pet = await db.pets.find_one({'_id': ObjectId(id)})
    if not pet:
        raise NotFound('Pet não encontrado')
    return response.json({
        'id': str(pet['_id']),
        'nome': pet['nome'],
        'tipo': pet['tipo'],
        'data_nascimento': pet['data_nascimento'],
        'status_vacinacao': pet['status_vacinacao'],
        'bairro': pet['bairro']
    })

# Rota para atualizar um pet por ID
@app.route('/pets/<string:id>', methods=['PUT'])
async def atualizar_pet(request, id):
    data = request.json
    db = app.config.db
    pet = await db.pets.find_one({'_id': ObjectId(id)})
    if not pet:
        raise NotFound('Pet não encontrado')
    await db.pets.replace_one({'_id': ObjectId(id)}, data)
    return response.json({'mensagem': 'Pet atualizado com sucesso!'})

# Rota para deletar um pet por ID
@app.route('/pets/<string:id>', methods=['DELETE'])
async def deletar_pet(request, id):
    db = app.config.db
    pet = await db.pets.find_one({'_id': ObjectId(id)})
    if not pet:
        raise NotFound('Pet não encontrado')
    await db.pets.delete_one({'_id': ObjectId(id)})
    return response.json({'mensagem': 'Pet deletado com sucesso!'})

if __name__ == '__main__':
    app.run(host='localhost', port=27017)

"""