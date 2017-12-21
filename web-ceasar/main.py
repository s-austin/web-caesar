from flask import Flask, request
from ceasar import rotate_string

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
        <form action="/ceasar" method="post">
         
            <label for="rot">Rotate by: </label>
            <input type="text" id="rot" name="rot" value=0 /><br />
            <textarea name="text"></textarea><br />
            <button type="submit" value="submit">Submit Query</button>
           
        </form>
    </body>
</html>

"""
@app.route("/")
def index():
    return form

@app.route("/ceasar", methods=['POST'])
def encrypt():
        text = request.form['text']
        rot = int(request.form['rot'])
        return rotate_string(text, rot)

app.run()