from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize a simple in-memory database
def init_db():
    connection = sqlite3.connect('test.db')  # Persistent database for demonstration
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "password123")')
    cursor.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (2, "user", "userpass")')
    connection.commit()
    connection.close()

init_db()

# Vulnerable login page
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SQL Injection Demo</title>
        </head>
        <body>
            <h2>Login</h2>
            <form action="/login" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <button type="submit">Login</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vulnerable query
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"<h3>Welcome, {user[1]}!</h3>"
        else:
            return "<h3>Invalid credentials!</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
    finally:
        connection.close()

# Secure login page
@app.route('/secure_login', methods=['POST'])
def secure_login():
    username = request.form['username']
    password = request.form['password']

    # Secure query using parameterized statements
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    try:
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            return f"<h3>Welcome, {user[1]}!</h3>"
        else:
            return "<h3>Invalid credentials!</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
