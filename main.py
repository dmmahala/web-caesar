from flask import Flask

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
        <form action="" method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot"/><br>
            <textarea name="text"/><br>
            <input type="submit" value="Encode"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()