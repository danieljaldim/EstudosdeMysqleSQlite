import sqlite3  # Importa o módulo sqlite3 para interagir com bancos de dados SQLite
from pathlib import Path  # Importa Path para trabalhar com caminhos de arquivos

# Define o diretório raiz e o nome do arquivo do banco de dados
ROOT_DIR = Path(__file__).parent  # Diretório raiz do projeto
DB_NAME = 'db.sqlite3'  # Nome do arquivo do banco de dados
DB_FILE = ROOT_DIR / DB_NAME  # Caminho completo do banco de dados
TABLE_NAME = 'customers'  # Nome da tabela que será usada no banco de dados

# Cria uma conexão com o banco de dados SQLite
connection = sqlite3.connect(DB_FILE)  # Conecta ao banco de dados, criando-o se não existir
cursor = connection.cursor()  # Cria um cursor para executar comandos SQL

# CUIDADO: deletando registros sem uma condição WHERE (perigoso)
# Remove todos os dados da tabela sem filtrar (perigo para perda de dados)
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
# Reseta a sequência de IDs autoincrementados
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
# Confirma as operações de DELETE no banco de dados
connection.commit()

# Cria a tabela 'customers' se ela ainda não existir
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'  # Criação da tabela
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # Coluna id com incremento automático
    'name TEXT,'  # Coluna name do tipo texto
    'weight REAL'  # Coluna weight do tipo real (para números com casas decimais)
    ')'
)
# Confirma a criação da tabela
connection.commit()

# Prepara o SQL para inserir dados na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '  # Insere valores na tabela customers
    '(name, weight) '  # Especifica as colunas onde os valores serão inseridos
    'VALUES '  # Valores que serão inseridos
    '(?, ?)'  # Placeholder para valores a serem passados por parâmetros
    '(:nome, :peso)'  # Outro placeholder usando dicionários nomeados (mistura de placeholders)
)

# Insere os dados usando tuplas
# Descomente esta linha para inserir valores com uma lista
# cursor.execute(sql, ['Joana', 4])

# Executa a inserção de múltiplos valores usando o método executemany
cursor.executemany(
    sql,  # Usa a query SQL definida anteriormente
    (
        ('Joana', 4), ('Luiz', 5)  # Insere valores de duas pessoas
    )
)

# Executa um INSERT usando dicionário de parâmetros (com nomes)
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})

# Executa múltiplas inserções usando dicionários com valores nomeados
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},  # Insere um registro
    {'nome': 'Maria', 'peso': 2},  # Insere outro registro
    {'nome': 'Helena', 'peso': 4},  # Mais um registro
    {'nome': 'Joana', 'peso': 5},  # E outro registro
))

# Confirma todas as inserções feitas até agora
connection.commit()

# Imprime a query SQL para conferência (a query com placeholders)
print(sql)

# Fecha o cursor após concluir as operações
cursor.close()

# Fecha a conexão com o banco de dados
connection.close()
