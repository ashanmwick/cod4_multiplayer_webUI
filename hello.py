from flask import Flask,send_from_directory,render_template,request
import os

app = Flask(__name__,static_url_path='',static_folder='static')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home_page():
    return render_template('index.html',text_string="HI",web_map_list=map_list)

@app.route('/',methods=['POST'])
def submit():
    text=request.form['text']
    
    return render_template('index.html',text_string_2="HU")

@app.route('/kill_house',methods=['GET'])
def map_name():
    name='<img src="images/killhouse.webp" alt="Girl in a jacket">'
    return name


if __name__ == '__main__':
    map_list=["Kill House","Vacant"]
    app.run(debug=True,host='0.0.0.0', port=80)