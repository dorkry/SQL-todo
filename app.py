import flask_wtf, funkcje
from flask import Flask, render_template, request, redirect, jsonify

heading = ["author", "title", "format", "descr"]

app = Flask(__name__)

base = funkcje.read()

@app.route('/')
def main():   
    return render_template("index.html")

@app.route('/add', methods=['GET'])
def add():
    return render_template("add.html")

@app.route('/add', methods = ['POST'])
def add_post():
    author = request.form.get("author")
    title = request.form.get("title")
    form = request.form.get("format")
    descr = request.form.get("descr")
    temp = {
        "author": author,
        "title": title,
        "format": form,
        "descr": descr
    }
    base.append(temp)
    funkcje.save(author, title, descr, form)
    return redirect("/")
 
@app.route('/find', methods=['GET'])
def find():
    return render_template("find.html")
    
@app.route('/find', methods=['POST'])
def find_out():
    new_list = []
    option = request.form.get("option")
    value = request.form.get("value")
    for i in base:
        if i[option] == value:
            new_list.append(i)
    print(new_list)
    return render_template("find.html", result = new_list)

@app.route('/find_id', methods=['GET'])
def find_id():   
    return render_template("update.html", id_list = funkcje.find_ids())

@app.route('/find_id', methods=['POST'])
def find_id_post():
    book = funkcje.get_book(request.form.get("id"))
    return render_template("update.html", id_list = funkcje.find_ids(), author = book["author"], title = book["title"], format = book["format"], descr = book["descr"], id = request.form.get("id"))

@app.route("/update", methods = ['POST'])
def update():
    print(request.form.get("id"))
    funkcje.update(request.form.get("id"), request.form.get("author"), request.form.get("title"), request.form.get("format"), request.form.get("descr"))
    return render_template("update.html")


@app.route('/delete', methods =['GET'])
def delete():
    return render_template("delete.html")

@app.route('/delete', methods=['POST'])
def delete_out():
    out = False
    author = request.form.get("author")
    title = request.form.get("title")
    funkcje.remove(author, title)
    
    return render_template("delete.html")

@app.route('/all', methods=['GET'])
def show_all():
    return render_template("all.html", result = funkcje.read())

if __name__ == "__main__":
    app.run(debug=True)

