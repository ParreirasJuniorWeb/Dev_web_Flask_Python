from flask import Flask, render_template, request

import mysql.connector as conector
from mysql.connector import Error
import random

# class AppBD:
#        def __init__(self):
#            self.conn = None
#            self.cur = None
#            self.createDataTable("lojadb", "PRODUTOS")
#            self.connect_to_db("lojadb")
           
#        def createDataTable(self, db, table):
#             try:
#                 # Abertura de conexão e aquisição de cursor
#                 self.conn = conector.connect(
#                    database=db,
#                    host="localhost",
#                    user="root",
#                    password="886744@Jo"
#                    )
#                 self.cur = self.conn.cursor()
#                 # Execução de um comando: SELECT... CREATE ...
#                 comando = '''CREATE TABLE ''' + table + '''(
#                                 id_prod INTEGER NOT NULL AUTO_INCREMENT,
#                                 nome_prod varchar(150) NOT NULL,
#                                 preco_prod FLOAT NOT NULL,
#                                 PRIMARY KEY (id_prod)
#                                 );'''
#                 self.cur.execute(comando)
#                 # Efetivação do comando
#                 self.conn.commit()
#             except conector.DatabaseError as err:
#                 print(f"Erro de banco de dados ao criar a tabela no banco de dados", err)
#             finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close()   
#        def connect_to_db(self, db):
#            try:
#                self.conn = conector.connect(
#                    database= db,
#                    host="localhost",
#                    user="root",
#                    password="886744@Jo"
#                )
#                self.cur = self.conn.cursor()
#                print("Conexão com o Banco de Dados aberta com sucesso!")
#            except (Exception, Error) as error:
#                print("Falha ao se conectar ao Banco de Dados", error)
#            finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close()         
#        def selecionar_dados(self, table):
#            try:
#                comando_SELECAO_TABLE_BD = "SELECT * FROM " + table
#                self.cur = self.conn.cursor()
#                self.cur.execute(comando_SELECAO_TABLE_BD)
#                registros = self.cur.fetchall()
#                return registros
#            except (Exception, Error) as error:
#                print("Erro ao selecionar dados", error)
#                return []
#            finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close() 
#        def inserir_dados(self, table, nome, preco):
#            try:
#                comando_INSERT_INTO_TABLE_BD = "INSERT INTO " + table + " (nome_prod, preco_prod) VALUES ('" + nome + "', " + str(preco) + ")"
#                self.cur = self.conn.cursor()
#                self.cur.execute(comando_INSERT_INTO_TABLE_BD)
#                self.conn.commit()
#                print("Inserção realizada com sucesso!")
#            except (Exception, Error) as error:
#                print("Erro ao inserir dados", error)
#            finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close()     
#        def atualizar_dados(self, table, codigo, nome, preco):
#            try:
#                comando_UPDATE_TABLE_BD = "UPDATE " + table + " SET nome_prod = '" + nome + "', preco_prod = " + str(preco) + " WHERE id_prod = " + str(codigo)
#                self.cur = self.conn.cursor()
#                self.cur.execute(comando_UPDATE_TABLE_BD)
#                self.conn.commit()
#                print("Atualização realizada com sucesso!")
#            except (Exception, Error) as error:
#                print("Erro ao atualizar dados", error)
#            finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close()     
#        def excluir_dados(self, table, codigo):
#            try:
#                comando_DELETE_TABLE_BD = "DELETE FROM " + table + " WHERE id_prod = " + str(codigo)
#                self.cur = self.conn.cursor()
#                self.cur.execute(comando_DELETE_TABLE_BD)
#                self.conn.commit()
#                print("Exclusão realizada com sucesso!")
#            except (Exception, Error) as error:
#                print("Erro ao excluir dados", error)
#            finally:
#                 # Fechamento das conexões
#                 if self.conn:
#                     self.cur.close()
#                     self.conn.close()
                    
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("teste.html")

@app.route("/teste.html")
def teste():
    return render_template("teste.html")

@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/enviarformulario", methods=["POST"]) 
def enviarformulario():
    if request.method == 'POST':
        return render_template("formulario_resultado.html", nome=request.form.get("nome"), email=request.form.get("email"))

@app.route("/enviarformulario_mysql", methods=["POST"])
def enviarformulario_mysql():
    if request.method == 'POST':
        nome = request.form.get("nome")
        email = request.form.get("email")
    
#     try:
#         app_bd = AppBD()
#         app_bd.inserir_dados("Clientes", nome, email)
#         registros_table = app_bd.selecionar_dados("Clientes")
#         return render_template("formulario_resultado.html", registros=registros_table) 
            
#     except Error as error:    
#         return f"Erro ao conectar ao banco de dados: {error}"
        
# @app.route("/enviarformulario_atualizado", methods=["POST"])        
# def AlterarDados():
#     if request.method == 'POST':
#         nome = request.form.get("nome")
#         email = request.form.get("email")
#         id = request.form.get("id")
        
#     try:
#         app_bd = AppBD()
                
#         app_bd.atualizar_dados("PRODUTOS", 1, "PRODUTO_ATUALIZADO", 45986.00)
            
#     except Error as error:    
#         return f"Erro ao conectar ao banco de dados: {error}"     
                
if __name__ == '__main__':
    app.run(debug=True)

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World! Sistema E-LIXO"

# @app.route("/e-LIXO")
# def index_2():
#     return render_template("teste.html")

# @app.route("/formulario")
# def formulario():
#     return render_template('formulario.html')

# @app.route("/enviarformulario", methods=["POST"]) #  Exemplificação de rotas para tratar formulário. 
# def enviarformulario():
#     if request.method == 'POST':
#         return render_template("formulario_resultado.html", nome=request.form.get("nome"), email=request.form.get("email"))

# # Mandar esses dados da requição para o banco de dados MySQL
# @app.route("/enviarformulario_mysql", methods=["POST"])
# def enviarformulario_mysql():
#     if request.method == 'POST':
#         nome = request.form.get("nome"),
#         email = request.form.get("email"),
    
#     #  Exemplo de conexão com banco de dados MySQL
    
#         try:
#             # Criando uma instância da classe AppBD e inserindo dados aleatórios
#             app_bd = AppBD()
#             app_bd.inserir_dados("Clientes", nome, email)
#             registros_table = app_bd.selecionar_dados("Clientes")
#             for reg in registros_table:
#                 print(reg)
#                 list_regs = reg
#             return render_template("formulario_resultado.html", list(list_regs)) 
            
#         except (Exception, Error) as error:    
#             return f"Erro ao conectar ao banco de dados: {error}"
        
# @app.route("/enviarformulario_atualizado", methods=["POST"])        
# def AlterarDados():
#     if request.method == 'POST':
#         nome = request.form.get("nome"),
#         email = request.form.get("email"),
#         id = request.form.get("id"),
        
#     try:
#         app_bd = AppBD()
                
#         app_bd.atualizar_dados("PRODUTOS", 1, "PRODUTO_ATUALIZADO", 45986.00)
            
#     except (Exception, Error) as error:    
#             return f"Erro ao conectar ao banco de dados: {error}"     
                
# if __name__ == '__main__':
#     app.run(debug=True)