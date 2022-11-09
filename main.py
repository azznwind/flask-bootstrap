from flask import Flask, render_template
#from flask_ngrok import run_with_ngrok
from flask.wrappers import Response 
import git

app=Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
  repo = git.Repo('./flask-bootstrap')
  origin = repo.remote.origin
  repo.create_head('main', 
  origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  orign.pull()
  return '', 200

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html', name='greg')

#if __name__=="__main__":
    #app.run(host="localhost", port=5000, debug=True)
    app.run()