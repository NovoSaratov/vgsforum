from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hjem():
    return render_template('index.html')

@app.route('/om-skolen')
def om_skolen():
    return render_template('om_skolen.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/soknad')
def soknad():
    return render_template('soknad.html')

@app.route('/fag')
def fag():
    return render_template('fag.html')

if __name__ == '__main__':
    app.run(debug=True) 