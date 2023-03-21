# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sam"
    age = "16" 

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():
    name = "Shamender"
    age = "47" 
    return render_template('father.html', name = name , age = age)

@app.route("/mother")
def mother():
    name = "Poonam"
    age = "45" 
    return render_template('father.html', name = name , age = age)

@app.route("/friend")
def friend():
    name = "Raj"
    age = "15" 
    return render_template('father.html', name = name , age = age)

app.run(debug=True)

if __name__  ==  '__main__':
    app.run(debug=True)
