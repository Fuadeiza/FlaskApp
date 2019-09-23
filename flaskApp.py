from flask import Flask
app= Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"

@app.route('/what')
def what():
    return "What bro!"


if __name__=='__main__':
    app.run(debug=True)