from flask import Flask, render_template_string, request

app = Flask(__name__)

# Improved HTML template for the calculator
calculator_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            text-align: center;
            padding: 20px;
            margin: 0;
        }
        h1 {
            color: #444;
        }
        .calculator-container {
            background: #ffffff;
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        label {
            font-weight: bold;
            display: block;
            margin-bottom: 8px;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }
        button {
            background: #007BFF;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: #e0f7fa;
            color: #00796b;
            font-size: 18px;
            font-weight: bold;
            border-radius: 5px;
        }
        footer {
            margin-top: 30px;
            font-size: 12px;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="calculator-container">
        <h1>Simple Calculator</h1>
        <form method="POST">
            <label for="num1">Number 1:</label>
            <input type="number" name="num1" id="num1" required>

            <label for="num2">Number 2:</label>
            <input type="number" name="num2" id="num2" required>

            <label for="operation">Operation:</label>
            <select name="operation" id="operation" required>
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>

            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <div class="result">
                Result: {{ result }}
            </div>
        {% endif %}
    </div>

    <footer>
        &copy; 2024 Flask Calculator App
    </footer>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Retrieve form data
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            # Perform calculation based on selected operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by 0"
        except ValueError:
            result = "Error: Invalid input"

    # Render the template with the result
    return render_template_string(calculator_template, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
