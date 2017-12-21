from flask import Flask, render_template, request
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color"#eee;
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
        <form action="/ceasar" method="post">
         
            <label for="rot">Rotate by: </label>
            <input type="text" id="rot" name="rot" value=0 /><br />
            <textarea name="text">{0}</textarea><br />
            <button type="submit" value="submit">Submit Query</button>
           
        </form>
    </body>
</html>

"""

@app.route("/ceasar")
def index():
    return form.format("")
    #return form without above knocks out css

@app.route("/ceasar", methods=['POST'])
def encrypt():
        text = request.form['text']
        rot = int(request.form['rot'])
        answer =  rotate_string(text, rot)
        return render_template('/index.html', answer=answer)
        #return answer


app.run()