from flask import Flask, render_template, request
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('eror404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/arduino/", methods=['POST'])
def go_arduino():
    return render_template('arduino_run.html')

@app.route("/python/", methods=['POST'])
def go_python():
    return render_template('python_run.html')

@app.route("/lego/", methods=['POST'])
def go_lego():
    return render_template('lego_run.html')

if __name__ == '__main__':
    app.debug = True
    app.run()