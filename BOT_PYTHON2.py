#BASE FLASK
from flask import Flask, request, jsonify
import subprocess  # Para rodar o programa externo

import os
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')

app = Flask(__name__)

# Comandos disponíveis
commands = {
    "/menu": "Menu principal:\n1. /pesquisa_lote - Realiza pesquisa em lote\n2. /comandos - Lista todos os comandos",
    "/comandos": "Comandos disponíveis: /menu, /pesquisa_lote"
}

# Função para a rota '/menu'
@app.route('/menu', methods=['GET'])
def menu():
    response = commands["/menu"]
    return jsonify({"reply": response})

# Função para a rota '/pesquisa_lote'
# Chamada a outro programa
@app.route('/pesquisa_lote', methods=['POST'])
def pesquisa_lote():
    try:
        # Simula a execução de outro programa Python
        # Rodando outro script Python via subprocess
        result = subprocess.run(['python3', 'outro_programa.py'], capture_output=True, text=True)
        
        # Retorna o resultado da execução
        if result.returncode == 0:
            response = f"Execução concluída: {result.stdout}"
        else:
            response = f"Erro na execução: {result.stderr}"
    except Exception as e:
        response = f"Ocorreu um erro: {str(e)}"
    
    return jsonify({"reply": response})

# Função para lidar com comandos desconhecidos ou inválidos
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message')

    # Verifica se o comando é válido
    if message in commands:
        response = commands[message]
    else:
        response = "Comando inválido ou não reconhecido."
    
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)






##############################################################
# TO DO
# IMPLEMENTAR AS FUNÇÕES
# outro_programa.py

def pesquisa_em_lote():
    # Simulação de uma tarefa complexa ou longa
    print("Iniciando pesquisa em lote...")
    # Alguma lógica de processamento aqui...
    print("Pesquisa em lote concluída com sucesso!")

if __name__ == '__main__':
    pesquisa_em_lote()
