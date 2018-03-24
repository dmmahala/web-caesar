from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/test" method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot"/><br>
            <textarea name="text"></textarea><br>
            <input type="submit" value="Encrypt"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/test", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    rotated = rotate_string(text, rot)
    content = """
    <!doctype html>
    <html>
        <head>
            <title>Encrypted</title>
        </head>
        <body>
            <h1>""" + rotated + """</h1>
        </body>
    </html>
    """

    return content

app.run()