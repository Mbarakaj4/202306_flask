from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_flask ():
    return 'Hola Flask!'

@app.route('/success')
def success():
    return 'success'

@app.route('/hola/<name>')
def hola (name):
    return 'hola, ' + name

@app.route('/users/<username>/<id>')
def mostrar_perfil_usuario(username, id):
    print(username)
    print(id)
    return f'username: {username} id: {id}'

if __name__ == "__main__":
    app.run(debug=True)