from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mywork')
def mywork():
    return render_template('mywork.html')

@app.route('/adrenaline')
def adrenaline():
    return render_template('adrenaline.html')

@app.route('/underdog')
def underdog():
    return render_template('underdog.html')

@app.route('/lfl')
def lfl():
    return render_template('lfl.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
   app.run(debug= True)
