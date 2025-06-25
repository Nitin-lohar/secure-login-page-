from flask import Flask, render_template, request, redirect, url_for, flash
import bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Simulated database (use SQLite or Mongo later)
users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        users[username] = hashed
        flash("Registered Successfully! Now log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        stored_hash = users.get(username)

        if stored_hash and bcrypt.checkpw(password, stored_hash):
            flash("Login Successful!")
        else:
            flash("Invalid Credentials")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)