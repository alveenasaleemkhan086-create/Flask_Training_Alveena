from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculator():

    result = None

    if request.method == 'POST':

        a = float(request.form['a'])
        b = float(request.form['b'])

        operation = request.form['operation']

        if operation == 'add':
            result = a + b

        elif operation == 'sub':
            result = a - b

        elif operation == 'mul':
            result = a * b

        elif operation == 'div':
            if b != 0:
                result = a / b
            else:
                result = "Cannot divide by zero"

    return render_template('calculator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)