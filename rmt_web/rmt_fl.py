from flask import Flask, render_template, request
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('eror404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()