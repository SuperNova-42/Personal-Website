from flask import Flask, request, render_template
import markdown

app = Flask(__name__, template_folder='templates')

PROJECTS = {
    "kettleflip": {
        "name": "KettleFlip",
        "category": "Coding",
        "tech": "Python, Requests, REST API",
        "summary_file": "static/content/kettleflip.md",
        "details": [
            "Implemented logic to identify potentially profitable item flips by comparing current market prices against expected values.",
            "Parsed JSON API responses and calculated potential profit to present market opportunities to users."
        ],
        "link": "https://github.com/SuperNova-42/KettleFlip"
    },
    "code-judge": {
        "name": "Full-Stack Learning Platform with Code Judge",
        "category": "Coding",
        "tech": "Python, Flask, SQLAlchemy, HTML/CSS",
        "summary_file": "static/content/code-judge.md",
        "details": [
            "Implemented a backend evaluation process to execute user submissions against predefined test cases.",
            "Designed a relational database using SQLAlchemy to manage users, classrooms, coding problems, and submissions.",
            "Implemented role-based access control and secure session-based authentication using password hashing."
        ],
        "link": "https://github.com/SuperNova-42/Code-Judge"
    },
    "Proposal": {
        "name": "Proposal",
        "category": "Technical Writing",
        "summary_file": "static/content/proposal.md",
        "embed_pdf": "docs/Proposal_Revision.pdf"
    },
    "Instructions" : {
        "name": "Instructions",
        "category": "Technical Writing",
        "summary_file": "static/content/instructions.md",
        "embed_pdf": "docs/GitHub_Instructions.pdf"
    }
}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about_me')
def about():
    return render_template("about_me.html")

@app.route('/projects')
def projects():
    return render_template("projects.html", projects = PROJECTS)

@app.route('/projects/<project>')
def project_details(project):
    project = PROJECTS.get(project)
    summary_html = None
    if "summary_file" in project:
        with open(project["summary_file"], "r", encoding="utf-8") as f:
            summary_html = markdown.markdown(f.read())
    return render_template("project_details.html", project = project, summary_html = summary_html)

@app.route('/resume')
def resume():
    with open("static/content/resume.md", "r", encoding="utf-8") as f:
        summary_html = markdown.markdown(f.read())
    return render_template("resume.html", summary_html = summary_html)

@app.route('/cover-letter')
def cover_letter():
    with open("static/content/cover-letter.md", "r", encoding="utf-8") as f:
        summary_html = markdown.markdown(f.read())
    return render_template("cover-letter.html", summary_html = summary_html)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)