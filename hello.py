from flask import Flask,send_from_directory,render_template,request
import os
from maths import get_factors

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home_page():
    return render_template('index.html',text_string="HI")

@app.route('/',methods=['POST'])
def submit():
    text=request.form['text']
    
    return render_template('index.html',text_string_2="HU")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)