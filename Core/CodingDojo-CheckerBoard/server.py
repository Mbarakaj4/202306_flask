from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def default() -> object:
    return render_template('index.html', color1 = 'black' , color2 = 'darkred', i = 7, j = 7)

@app.route('/<x>/<y>/')
def position(x,y) -> object:
    return render_template('index.html',color1 = 'black' , color2 = 'darkred', i = int(x), j = int(y))

@app.route('/<x>/<y>/<c1>/<c2>/')
def position_and_color(x,y,c1,c2) -> object:
    return render_template('index.html',color1 = c1 , color2 = c2, i = int(x), j = int(y))
if __name__ == '__main__':
    app.run(debug=True)