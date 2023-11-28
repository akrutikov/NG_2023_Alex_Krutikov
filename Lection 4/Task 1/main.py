from flask import Flask, render_template, request

servak = Flask(__name__)

@servak.route('/')
def home():
    return render_template('index.html')

@servak.route("/answer")
def answer():
    first = float(request.args.get("valuea"))
    second= float(request.args.get("valueb"))
    math = str(request.args.get("math"))
    answer = ''
    if math == 'plus':
        answer = str(first + second)
    elif math == 'minus':
        answer = str(first - second)
    elif math == 'multiply':
        answer = str(first * second)
    elif math == 'split':
        if second != 0:
            answer = str(first / second)
        else:
            answer = "When dividing, the second number must be greater than 0"
    return answer
    
if __name__ == "__main__":
    servak.run(debug=True)