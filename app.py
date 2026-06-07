from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "DB.json")


# -------------------------
# Load Data
# -------------------------
def load_data():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


# -------------------------
# Save Data
# -------------------------
def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------
# HOME
# -------------------------
@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)


# -------------------------
# ADD
# -------------------------
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        data = load_data()

        new_user = {
            "id": len(data) + 1,
            "name": request.form['name'],
            "age": request.form['age'],
            "gender": request.form['gender']
        }

        data.append(new_user)

        save_data(data)

        print("Added User:", new_user)

        return redirect('/')

    return render_template('add.html')


# -------------------------
# EDIT
# -------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    data = load_data()

    user = next((x for x in data if x["id"] == id), None)

    if user is None:
        return "User Not Found"

    if request.method == 'POST':

        user["name"] = request.form['name']
        user["age"] = request.form['age']
        user["gender"] = request.form['gender']

        save_data(data)

        print("Updated User:", user)

        return redirect('/')

    return render_template('edit.html', user=user)


# -------------------------
# DELETE
# -------------------------
@app.route('/delete/<int:id>')
def delete(id):

    data = load_data()

    data = [x for x in data if x["id"] != id]

    save_data(data)

    print("Deleted User ID:", id)

    return redirect('/')


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)