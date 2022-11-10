from flask import Flask, render_template, request, jsonify
#from flask_ngrok import run_with_ngrok
from flask.wrappers import Response 
import git

import googlespreadsheet


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
    return render_template('index.html',  tables=googlespreadsheet.data.to_html(), titles=googlespreadsheet.data.columns.values)
                                
@app.route("/test")
def test():
    return render_template('test.html', name='greg')

@app.route("/moment")
def moment():
    
    return render_template('moment.html', name='greg')


@app.route('/testdata', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'GET':
        message = googlespreadsheet.df
        message = message.to_json()
        #return jsonify(message)  # serialize and use JSON headers    # POST request
        #jm = jsonify(message)
        return render_template('testdata.html')
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200
           

if __name__=="__main__":
    #app.run(host="localhost", port=5000, debug=True)
    app.run(debug=True)