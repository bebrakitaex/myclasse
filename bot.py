from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classmates.html')
def classmates():
    return render_template('classmates.html')

@app.route('/events.html')
def events():
  return render_template('events.html')
  
@app.route('/404.html')
def error():
  return render_template('404.html')
  

if __name__ == '__main__':
    app.run(debug=True)
