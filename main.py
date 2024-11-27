import sqlite3  # Importa a biblioteca SQLite3 para interagir com o banco de dados SQLite
from pathlib import Path  # Importa Path para trabalhar com caminhos de arquivos

# Define o diretório raiz (ROOT_DIR) como o diretório pai do arquivo atual
ROOT_DIR = Path(__file__).parent

# Define o nome do arquivo de banco de dados e o caminho completo para ele
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

# Nome da tabela que será usada no banco de dados
TABLE_NAME = 'customers'

# Conecta ao banco de dados (ou cria, se não existir) e obtém um cursor para executar comandos SQL
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create, Read, Update, Delete
# SQL - Comandos de inserção, leitura, atualização e deleção

# CUIDADO: delete sem WHERE. Remove todos os dados da tabela 'customers'
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso: Remove o registro de auto incremento (sqlite_sequence) relacionado à tabela
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
# Confirma as mudanças no banco de dados
connection.commit()

# Cria a tabela 'customers' com as colunas 'id', 'name' e 'weight', se não existir
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # id autoincrementado
    'name TEXT,'  # Nome do cliente
    'weight REAL'  # Peso do cliente
    ')'
)
connection.commit()  # Confirma a criação da tabela

# Prepara a instrução SQL para inserir dados na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '  # Define as colunas 'name' e 'weight' para inserção
    'VALUES '
    '(:nome, :peso)'  # Valores serão passados como dicionário (nome e peso)
)

# Insere um único registro na tabela usando o método 'execute' com um dicionário de valores
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})

# Insere múltiplos registros de uma só vez usando 'executemany'
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},  # Insere 'Joãozinho' com peso 3
    {'nome': 'Maria', 'peso': 2},  # Insere 'Maria' com peso 2
    {'nome': 'Helena', 'peso': 4},  # Insere 'Helena' com peso 4
    {'nome': 'Joana', 'peso': 5},  # Insere 'Joana' com peso 5
))
connection.commit()  # Confirma as inserções

# Ponto de entrada principal do script
if __name__ == '__main__':
    print(sql)  # Exibe a instrução SQL

    # Deleta o registro da tabela onde o 'id' é 3
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )

    # Deleta o registro da tabela onde o 'id' é 1
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()  # Confirma as deleções

    # Atualiza o registro com 'id' 2, mudando 'name' e 'weight'
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=67.89 '  # Define novos valores para 'name' e 'weight'
        'WHERE id = 2'  # Atualiza onde o 'id' é 2
    )
    connection.commit()  # Confirma a atualização

    # Seleciona todos os registros da tabela
    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    # Itera sobre os registros e exibe 'id', 'name', e 'weight' para cada um
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)  # Exibe os dados de cada linha

    # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    connection.close()