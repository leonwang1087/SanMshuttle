from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World."
    
@app.route("/shuttletime")
def shuttle():
    dirpath = os.path.abspath(os.path.curdir)
    with open(os.path.join(dirpath, "result.txt"), "r") as f:
        nexttime = f.read()
        return "Next Shuttle to go home is: {}".format(str(nexttime))
    
    
if __name__ == "__main__":
    
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))