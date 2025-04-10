from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
    
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/ifmg")
def ifmg():
    return "IFMG - Instituto Federal de Minas Gerais | Curso do +IFMG"

@app.route("/Arquivo_html")
def Arquivo_html():
    return render_template('teste.html') # Retornando arquivo com extensão html. 
#  Renderização do exemplo utilizando arquivo com extensão html.

@app.route("/teste_template_layout_html")
def teste_template_layout_html():
    return render_template('teste2.html') # Retornando arquivo com extensão html. --->  Arquivo python da aplicação do modelo.

@app.route("/teste_codigo_python_na_web")
def testeLinguagemPython():
    return render_template('teste3.html')

@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/enviarformulario", methods=["POST"]) #  Exemplificação de rotas para tratar formulário. 
def enviarformulario():
    if request.method == 'POST':
        return render_template("formulario_resultado.html", nome=request.form.get("nome"), email=request.form.get("email"))

# Mandar esses dados da requição para o banco de dados MySQL
@app.route("/enviarformulario_mysql", methods=["POST"])
def enviarformulario_mysql():
    if request.method == 'POST':
        nome = request.form.get("nome"),
        email = request.form.get("email"),
    
    #  Exemplo de conexão com banco de dados MySQL
    
        try:
            connection = mysql.connector.connect(host='localhost', database='signupreactapp', user='root', password='886744@Jo')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Conectado ao banco de dados MySQL", db_Info)
                cursor = connection.cursor(prepared=True)
                query = "INSERT INTO teste_flask (nome, email) VALUES (%s, %s)"
                cursor.execute(query, (nome[0], email[0]))
                connection.commit()
                print("Dados inseridos com sucesso!")
                return render_template("formulario_resultado.html", nome=nome[0], email=email[0])
        except mysql.connector.Error as err:
            print(err)
            return render_template("formulario_resultado.html")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Conexão com o banco de dados MySQL encerrada!")
                   
if __name__ == '__main__':
    app.run(debug=True)