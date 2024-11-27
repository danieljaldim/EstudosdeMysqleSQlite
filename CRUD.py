import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# DELETE: Remove todos os dados da tabela e reseta a sequência de IDs
cursor.execute(f'DELETE FROM {TABLE_NAME}')
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

# CREATE: Criação da tabela 'customers' se não existir
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# CREATE: Insere dados na tabela
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
cursor.executemany(sql, [('Joana', 4), ('Luiz', 5)])
cursor.execute(sql, ('Sem nome', 3))
cursor.executemany(sql, [
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
])
connection.commit()

# READ: Leitura de todos os dados
cursor.execute(f'SELECT * FROM {TABLE_NAME}')
records = cursor.fetchall()
for record in records:
    print(record)

# UPDATE: Atualiza o peso de Joana para 6
cursor.execute(f'UPDATE {TABLE_NAME} SET weight = ? WHERE name = ?', (6, 'Joana'))
connection.commit()

# Confirma e fecha a conexão
cursor.close()
connection.close()
