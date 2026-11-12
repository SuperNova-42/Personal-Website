from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about_me')
def about():
    return render_template("about_me.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == '__main__':
    app.run(debug=True)