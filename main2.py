from flask import Flask, render_template
from liveserver import LiveServer
#from flask_ngrok import run_with_ngrok

app=Flask(__name__)
#run_with_ngrok(app)
ls = LiveServer(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html', name='greg')

#if __name__=="__main__":
    #app.run(host="localhost", port=5000, debug=True)
    #pp.run()

ls.run("0.0.0.0", 5000)