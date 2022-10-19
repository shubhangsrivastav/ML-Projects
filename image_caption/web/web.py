import re
from flask import Flask,request,render_template
from image_caption import generate_caption

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        id = request.form['id']
        id = id + ".jpg"
        # Function Call
        output = generate_caption(id)
        return render_template('predict.html',prediction_text=output,id=id)

if __name__ == '__main__':
    app.run(debug=True)