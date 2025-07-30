import json

pessoa = { 
    "nome":"Carlos", 
    "idade":"30", 
    "estudante": False
}

with open ("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)