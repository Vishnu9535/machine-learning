from flask import Flask
app=Flask(__name__)
def hello_world():
    return "<p>hello world<p>"
if __name__=='main':
    app.run()