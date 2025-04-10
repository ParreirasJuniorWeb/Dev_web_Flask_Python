import sqlite3
 
# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("aula.db")
 
print("Banco de dados 'aula.db' criado com sucesso!")

# Comando SQL para criar uma tabela chamada 'alunos'
comando_criar_tabela = """
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT UNIQUE NOT NULL,
    curso TEXT
);
"""
 
# Execute o comando SQL usando o cursor
try:
   cursor = conn.cursor()
   cursor.execute(comando_criar_tabela)
   conn.commit()
   print("Tabela 'alunos' criada com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao criar a tabela: {e}")   
   
# Dados para inserir na tabela 'alunos'
dados_alunos = [
    ('Carlos Drumond', '2023001', 'Engenharia de Software'),
    ('Cecília Meireles', '2023002', 'Letras'),
    ('Machado de Assis', '2023003', 'Direito')
]
 
# Comando SQL para inserir dados na tabela 'alunos'
comando_inserir_dados = "INSERT INTO alunos (nome, matricula, curso) VALUES (?, ?, ?)"
 
# Insira os dados usando o método executemany 
try:
    cursor.executemany(comando_inserir_dados, dados_alunos)
    conn.commit()
    print(f"{cursor.rowcount} registros inseridos na tabela 'alunos' com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao inserir dados: {e}")       

try:
    comando_selecao = "SELECT * FROM alunos"
    cursor.execute(comando_selecao)
    resultado = cursor.fetchall()
    print("Registros da tabela 'alunos':")
    for registro in resultado:
       print(registro)
except sqlite3.Error as e:
   print(f"Erro ao selecionar os registros na tabela 'alunos': {e}") 
    
# Comando para atualização de dados na tabela 'alunos'
comando_atualizar = "UPDATE alunos SET curso = 'Artes e Dança' WHERE matricula = '2023001'"

try:
   cursor.execute(comando_atualizar)
   conn.commit()
   print("Registro atualizado com sucesso!")
except sqlite3.Error as e:
   print(f"Erro ao atualizar um registro: {e}")
   
try:
    comando_selecao = "SELECT * FROM alunos"
    cursor.execute(comando_selecao)
    resultado = cursor.fetchall()
    print("Registros da tabela 'alunos':")
    for registro in resultado:
       print(registro)
except sqlite3.Error as e:
   print(f"Erro ao selecionar os registros na tabela 'alunos': {e}")      

# Comando para excluir registros em um banco de dados SQLite
try:
   comando_excluir = "DELETE FROM alunos WHERE matricula = '2023002'"
   cursor.execute(comando_excluir)
   conn.commit()
   print("Registro excluído com sucesso!")
except sqlite3.Error as e:
   print(f"Erro ao excluir um registro: {e}")
   
try:
    comando_selecao = "SELECT * FROM alunos"
    cursor.execute(comando_selecao)
    resultado = cursor.fetchall()
    print("Registros da tabela 'alunos':")
    for registro in resultado:
       print(registro)
except sqlite3.Error as e:
   print(f"Erro ao selecionar os registros na tabela 'alunos': {e}")       