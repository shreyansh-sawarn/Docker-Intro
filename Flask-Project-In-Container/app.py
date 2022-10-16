from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/about')
def about():
    return 'About Page '

@app.route('/help')
def help():
    return 'Help Page 24/7'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
