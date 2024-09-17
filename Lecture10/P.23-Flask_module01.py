from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allo</title>
    <style>
        body{
            height: 90vh;
            display: flex;
            flex-direction: column;
            width: 300px;
            justify-content: center;
            margin: 0 auto;
            box-sizing: border-box;
        }
        h1{
            background-color: gray;
            color: white;
            border-radius: 1rem;
            text-align: center;
            padding: 1rem;
            box-shadow: 3px 3px 3px black;
        }
    </style>
</head>
<body>
    <h1>Hello, {{ name }}! <br> This is my website</h1>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, name="World")

@app.route('/greet/<name>')
def greet(name):
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(debug=True)