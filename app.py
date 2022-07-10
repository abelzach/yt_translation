import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from googletrans import Translator

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Translation API   </h1>
<p>Another prototype API for my mini project</p>'''

@app.route('/api', methods=['GET'])
def api_id():
    if 'text' in request.args:
        dest = str(request.args['dest'])
        text = str(request.args['text'])
        
        trans = Translator()
        a = dest
        out = trans.translate(text,  dest = a)
        print(out.text)
        result = {
            "Tranlated" : out.text,
            #"METHOD" : GET
        }
        return jsonify(result)
    else:
        result = {
            "Message" : "Error"
            #"METHOD" : GET
        }
        return jsonify(result)

if __name__ == "__main__":
    app.run()