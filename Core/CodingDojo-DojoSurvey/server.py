from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="Esto no es una referencia al profesor Fransisco Boisier"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    print(request)
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['lenguajes'] = request.form['lenguajes']
    session['comentario'] = request.form['comentario']
    return redirect('/result')

@app.route('/clear')
def clearsession() -> None:
    session.clear()
    return redirect('/')

@app.route('/result')
def success():
    return render_template('result.html')
    
if __name__=="__main__":
    app.run(debug=True)