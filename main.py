from flask import Flask, render_template, request

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
    username_credentials = None
    userpassword_credentials = None
    if request.method == "POST":
        username_credentials = request.form['username']
        userpassword_credentials = request.form['userpassword']
    print(username_credentials, userpassword_credentials)
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)
