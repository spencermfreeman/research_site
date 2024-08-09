from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

#add a decorator and define what to return on the homepage, often html
@views.route("/")
def home():
    #we can add variables in the render template function and then accsess them in the rendered html doc using {{}}.
    return render_template('home.html') 

@views.route("/research")
def research():
    return render_template('research.html')

@views.route("/people")
def people():
    return render_template('people.html')

@views.route("/contact")
def contact():
    return render_template('contact.html')

@views.route("/publications")
def publications():
    return render_template('publications.html')
