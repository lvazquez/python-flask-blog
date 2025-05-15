from flask import Flask, render_template
from sqlite3 import connect, Row, Connection
from werkzeug.exceptions import abort

def get_db_connection() -> Connection:
    conn = connect('database.db')
    conn.row_factory = Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post_info = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post_info is None:
        abort(404)
    return post_info

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# Dynamic route well call post with the post_id integer used for the route
@app.route('/<int:post_id>')
def post(post_id):
    post_info = get_post(post_id)
    return render_template('post.html', post=post_info)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
