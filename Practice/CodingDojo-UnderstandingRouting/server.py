from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo() -> str:
    return 'Hola Mundo!'

@app.route('/dojo')
def dojo() -> str:
    return 'dojo'

@app.route('/say/<name>')
def say_name(name) -> str:
    name = str(name)
    return f"¡Hola, {name}!"

@app.route('/repeat/<times>/<word>')
def repeat_words(times: int, word: str) -> str:
    times = int(times)
    return f"{word}\r" * times

@app.errorhandler(404)
def four_zero_four(e)  -> str:
    #return '<img src="https://pbs.twimg.com/media/E-k9xa4UcAYLbRm?format=jpg&name=small" alt="?" width="500" height="600">', 404
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez'

if __name__ == '__main__':
    app.run(debug=True)