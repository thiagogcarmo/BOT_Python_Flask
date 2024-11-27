from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3  # Ou qualquer outro banco de dados que desejar
import requests  # Para chamadas de API externas, se necessário

app = Flask(__name__)

# Exemplo de banco de dados SQLite
def criar_banco_de_dados():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS telefones (orgao TEXT, telefone TEXT)''')
    cursor.execute('''INSERT INTO telefones (orgao, telefone) VALUES ('Prefeitura', '1234-5678')''')
    conn.commit()
    conn.close()

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.form.get('Body').strip().lower()
    response = MessagingResponse()
    msg = response.message()
    
    if incoming_msg == '/comandos':
        msg.body("Aqui estão os comandos disponíveis:\n"
                 "/comandos - Lista os comandos\n"
                 "/telefone - Pesquisa número de telefone de um órgão\n"
                 "/pesquisa - Executa uma função do programa\n"
                 "Por favor, use '/telefone <nome_do_orgao>' ou '/pesquisa <parametros>'")
    
    elif incoming_msg.startswith('/telefone'):
        orgao = incoming_msg.replace('/telefone', '').strip()
        telefone = pesquisar_telefone(orgao)
        if telefone:
            msg.body(f"O telefone do órgão '{orgao}' é: {telefone}")
        else:
            msg.body(f"Não encontramos nenhum telefone para '{orgao}'.")

    elif incoming_msg.startswith('/pesquisa'):
        parametros = incoming_msg.replace('/pesquisa', '').strip()
        resultado = executar_pesquisa(parametros)
        msg.body(f"Resultado da pesquisa: {resultado}")
        
    else:
        msg.body("Comando não reconhecido. Envie '/comandos' para ver os comandos disponíveis.")
    
    return str(response)

def pesquisar_telefone(orgao):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT telefone FROM telefones WHERE orgao LIKE ?", (f"%{orgao}%",))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def executar_pesquisa(parametros):
    # Simulação de alguma lógica que você tenha no programa Python
    return f"Pesquisa realizada com os parâmetros: {parametros}"

if __name__ == "__main__":
    criar_banco_de_dados()  # Inicializa o banco de dados na primeira execução
    app.run(debug=True)
