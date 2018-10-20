from flask import Flask, request, render_template
app = Flask(__name__)

class Person:
    def __init__(self, name, role, year):
        self.name = name
        self.role = role
        self.year = year

people = [ Person("Jeremy", "Web", 1), Person("Adriano", "Recurring Events", 1), Person("Anthony", "President", 4) ]
@app.route('/')
def index():
    return render_template("index.html", people = people)
@app.route('/profile/<name>')
def profile(name):
    person = None
    for p in people:
        if p.name == name:
            person = p
            break
    return render_template("profile.html", person = person)

if __name__ == "__main__":
    app.run(debug=True)
