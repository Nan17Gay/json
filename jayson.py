import json

json_dados = '{ "nome": "Ana",  "idade": 25,  "estudante": true }'

dados_py = json.loads(json_dados)

print(dados_py["nome"])
print(dados_py["idade"])
print(dados_py["estudante"])