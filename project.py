from flask import Flask, request, jsonify

app = Flask(__name__)

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

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

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
