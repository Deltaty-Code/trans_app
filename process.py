from flask import Flask , render_template , request , jsonify
from googletrans import Translator

app = Flask(__name__) 
trans = Translator()
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process",methods=['POST'])
def process():
    inputText = request.form['inputText'] 
    if inputText:
        t = trans.translate(inputText ,src = 'ar' ,dest ='en')
        outputText = t.text
        return jsonify({'inputText' : inputText,'outputText': outputText})

    return jsonify({'error' : 'Missing data!'})

if __name__ == "__main__":
    # app.run(debug = True)
    app.run(debug = False, host="0.0.0.0")