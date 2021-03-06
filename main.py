from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot"/><br>
            <textarea name="text">{0}</textarea><br>
            <input type="submit" value="Encrypt"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    if request.form['rot'] == '':
        rot = 0
    else:
        rot = int(request.form['rot'])
    text = request.form['text']
    rotated = rotate_string(text, rot)

    return form.format(rotated)

app.run()