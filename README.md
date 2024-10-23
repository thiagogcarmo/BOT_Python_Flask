# BOT_Python_Flask
Construção de modulo para criação de BOT, baseado em Python, django, Flask, PHP

BOT para chat, que atende a determinados comandos
Explicação:
Rota /menu:

Retorna um menu de opções com a lista de comandos que podem ser utilizados.
Rota /pesquisa_lote:

Utiliza o módulo subprocess para executar um script externo chamado outro_programa.py. Isso simula a execução de uma tarefa em lote. O resultado da execução, seja sucesso ou erro, é capturado e enviado como resposta.
subprocess.run() é uma maneira segura de executar comandos externos. Ele captura a saída (stdout) e erros (stderr).
Webhook para lidar com comandos via POST:

Usa um endpoint /webhook que pode receber comandos e responder com a mensagem correspondente.
Arquivo Externo: outro_programa.py
Aqui está um exemplo simples de um script Python que poderia ser executado quando a rota /pesquisa_lote for acionada:
