import sqlite3  # Importa o módulo sqlite3 para se conectar e manipular o banco de dados SQLite
from main import DB_FILE, TABLE_NAME  # Importa as variáveis DB_FILE (caminho do arquivo do banco de dados) e TABLE_NAME (nome da tabela) do módulo main

# Estabelece a conexão com o banco de dados SQLite usando o arquivo especificado por DB_FILE
connection = sqlite3.connect(DB_FILE)

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

# Executa uma consulta SQL para selecionar todos os registros da tabela especificada por TABLE_NAME
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# Itera sobre todos os registros retornados pela consulta anterior
for row in cursor.fetchall():
    _id, name, weight = row  # Desempacota os valores de cada linha (id, nome, peso) em variáveis
    print(_id, name, weight)  # Exibe os valores de cada registro (id, nome, peso) no console
print()  # Imprime uma linha em branco para separar os blocos de saída

# Executa outra consulta SQL para selecionar o registro da tabela onde o id é igual a 3
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

# Busca a primeira linha que atende à condição especificada (id = 3)
row = cursor.fetchone()

# Desempacota os valores do registro selecionado em variáveis
_id, name, weight = row

# Exibe os valores do registro selecionado (id, nome, peso) no console
print(_id, name, weight)

# Fecha o cursor para liberar os recursos
cursor.close()

# Fecha a conexão com o banco de dados
connection.close()
