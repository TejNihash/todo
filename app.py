from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def sayhello():
    return "Hello there, obi wan kenobi"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello there {name}"
    return render_template('form.html')


if __name__=='__main__':
    app.run(debug=True)