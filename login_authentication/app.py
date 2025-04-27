from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'

# Dictionary to store usernames and passwords
USERS = {
    'user': 'admin',
    'admin': 'admin'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password matches
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            flash("Login successful! Redirecting to your GitHub profile.", "success")
            return redirect("https://github.com/ganeshshetty-7")
        else:
            flash("Login Failed. Incorrect username or password.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # In a real-world app, you would store this data securely (e.g., hashed passwords)
        USERS[username] = password
        
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return f"Welcome to the dashboard!"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
