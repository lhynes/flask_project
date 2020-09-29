import os
#importing the Flask class 
from flask import Flask, render_template

#instance of this class
#in Flask, the convention is that our variable is called app.
app = Flask(__name__)

@app.route("/")
#def index():
  #return "<h1>Hello,</h1> World"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

#route
@app.route('/contact')
#view
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)#will allow to dubug easier
