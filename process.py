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
# def index():
#     if request.method == 'POST':
#         input_text = request.form['ar_input']  
#         if input_text != '':
#             t = trans.translate(input_text ,src = 'ar' ,dest ='en')
#             output_text = t.text
#     return render_template('index.html',output_text = output_text,input_text = input_text)

if __name__ == "__main__":
    app.run(debug = True)