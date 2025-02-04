from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Simple Calculator</title>
        </head>
        <body>
            <h2>Enter Numbers</h2>
            <form action="/calculate" method="get">
                <label for="a">Number 1:</label>
                <input type="number" id="a" name="a" required>
                <br>
                <label for="b">Number 2:</label>
                <input type="number" id="b" name="b" required>
                <br>
                <label for="operation">Choose operation:</label>
                <select name="operation" id="operation">
                    <option value="add">Add</option>
                    <option value="multiply">Multiply</option>
                </select>
                <br><br>
                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    '''

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        operation = request.args.get('operation')

        calc = Calculator(a, b)

        if operation == "add":
            result = calc.add()
        elif operation == "multiply":
            result = calc.multiply()
        else:
            return jsonify({"error": "Invalid operation. Use 'add' or 'multiply'"}), 400

        return f"<h2>Result: {result}</h2><br><a href='/'>Go Back</a>"

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
