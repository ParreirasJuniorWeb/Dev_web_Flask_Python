from flask import Flask, render_template, request
# Conexão com o banco de dados MySQL
import sqlite3
from sqlite3 import Error
    
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/enviarformulario", methods=["POST"]) 
def enviarformulario():
   if request.method == 'POST':
    request_user = {
        'nome': request.form.get("nome"),
        'email': request.form.get("email"),
        'telefone': request.form.get("telefone"),
        'cep': request.form.get("cep"),
        'endereco': request.form.get("endereco")
    }
    return render_template("formulario_resultado.html", **request_user)

@app.route("/enviarformulario_bd_mysql", methods=["POST"])
def enviarformulario_mysql():
    if request.method == 'POST':
        request_user = {
            'nome': request.form.get("nome"),
            'email': request.form.get("email"),
            'telefone': request.form.get("telefone"),
            'cep': request.form.get("cep"),
            'endereco': request.form.get("endereco")
        }
            
        try:
            connection = sqlite3.connect('aula.db')
            
            print("Banco de dados 'aula.db' criado com sucesso!")
            
            # Comando SQL para criar uma tabela chamada 'alunos'
            comando_criar_tabela = """
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                telefone TEXT NOT NULL,
                cep TEXT NOT NULL,
                endereco TEXT NOT NULL
            );
            """
            # Execute o comando SQL usando o cursor
            try:
                cursor = connection.cursor()
                cursor.execute(comando_criar_tabela)
                connection.commit()
                print("Tabela 'alunos' criada com sucesso!")
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela: {e}")  
            
            if connection:
                print("Conectado ao servidor:", connection)
                cursor = connection.cursor()
                sql = "INSERT INTO usuarios (nome, email, telefone, cep, endereco) VALUES (?, ?, ?, ?, ?)"
                val = (request_user['nome'], request_user['email'], request_user['telefone'], request_user['cep'], request_user['endereco'])
                cursor.execute(sql, (val.nome, val.email, val.telefone, val.cep, val.endereco))
                connection.commit()
                print("Dados inseridos com sucesso")
                
                try:
                    comando_selecao = "SELECT * FROM alunos"
                    cursor.execute(comando_selecao)
                    resultado = cursor.fetchall()
                    print("Registros da tabela 'alunos':")
                    for registro in resultado:
                        print(registro)
                except sqlite3.Error as e:
                    print(f"Erro ao selecionar os registros na tabela 'alunos': {e}") 
                    
                return render_template("formulario_resultado.html", **request_user)
            else:
                print("Não foi possível conectar ao servidor")
                cursor.close()
                connection.close()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return render_template("formulario_resultado.html", error="Erro ao conectar ao banco de dados")
        finally:
            cursor.close()
            connection.close()
            print("Conexão ao banco de dados fechada")
            return render_template("formulario_resultado.html", **request_user) 
    else:
        return render_template("formulario.html")
if __name__ == "__main__":
    app.run(debug=True)