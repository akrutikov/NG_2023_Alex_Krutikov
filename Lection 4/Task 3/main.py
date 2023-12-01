from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def first_ph():
    return render_template('photo1.html')

@app.route('/second')
def second_ph():
    return render_template('photo2.html')

@app.route('/third')
def third_ph():
    return render_template('photo3.html')

@app.route('/fourth')
def fourth_ph():
    return render_template('photo4.html')

@app.route('/fifth')
def fifth_ph():
    return render_template('photo5.html')

if __name__ == '__main__':
    app.run(debug = True)