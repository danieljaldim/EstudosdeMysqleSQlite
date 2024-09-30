# Importa o módulo sqlite3, que permite interagir com o banco de dados SQLite
import sqlite3

# Importa a classe Path da biblioteca pathlib, que facilita a manipulação de caminhos de arquivos
from pathlib import Path

# Define o diretório raiz do projeto como o local onde o arquivo atual está
ROOT_DIR = Path(__file__).parent

# Nome do banco de dados SQLite que será criado ou utilizado
DB_NAME = 'db.sqlite3'

# Caminho completo do arquivo do banco de dados (ROOT_DIR + DB_NAME)
DB_FILE = ROOT_DIR / DB_NAME

# Nome da tabela a ser criada ou manipulada
TABLE_NAME = 'customers'

# Cria uma conexão com o banco de dados (ou cria o banco de dados se ele não existir)
connection = sqlite3.connect(DB_FILE)

# Cria um cursor, que será utilizado para executar comandos SQL no banco de dados
cursor = connection.cursor()

# ALERTA: Executando um DELETE sem cláusula WHERE, o que pode remover todos os dados da tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Reseta o autoincremento da coluna "id" para 1, limpando a sequência do banco de dados
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# Aplica as mudanças feitas até agora no banco de dados
connection.commit()

# Cria a tabela se ela ainda não existir, com as colunas 'id', 'name' e 'weight'
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # 'id' como chave primária, que auto-incrementa
    'name TEXT,'  # Coluna 'name' do tipo texto
    'weight REAL'  # Coluna 'weight' do tipo número real (flutuante)
    ')'
)

# Aplica as mudanças ao banco de dados (criação da tabela)
connection.commit()

# ALERTA: Código suscetível a SQL Injection, ao usar a interpolação de strings diretamente
cursor.execute(
    sql = (
        f'INSERT INTO {TABLE_NAME} '  # Insere dados na tabela 'customers'
        '(id, name, weight) '  # Especifica as colunas 'id', 'name' e 'weight'
        '(name, weight) '  # Aqui há um erro de sintaxe: repetição de colunas
        'VALUES '  # Início da declaração de valores
        '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'  # Insere valores estáticos para 'Helena' e 'Eduardo'
        '(?, ?)'  # Insere valores parametrizados para evitar SQL Injection
    )
)

# Executa o SQL com valores seguros para 'Joana' e '4' usando parâmetros ao invés de interpolação direta
cursor.execute(sql, ['Joana', 4])

# Aplica as mudanças ao banco de dados (inserção dos dados)
connection.commit()

# Imprime a string SQL para ver o comando que foi executado
print(sql)

# Fecha o cursor, que é usado para interagir com o banco de dados
cursor.close()

# Fecha a conexão com o banco de dados para liberar os recursos
connection.close()
