from flask import Flask, render_template
from sqlite3 import connect, Row, Connection

def get_db_connection() -> Connection:
    conn = connect('database.db')
    conn.row_factory = Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
