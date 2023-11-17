from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/update', methods=['POST', 'GET'])
def update():
    print("home")
    return render_template("home.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    print("home")
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)
