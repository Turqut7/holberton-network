from flask import Flask, render_template, request, redirect, url_for
from models import init_db, get_posts, add_post

app = Flask(__name__)


@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route('/create', methods=['POST'])
def create_post():
    username = request.form.get('username')
    content = request.form.get('content')

    if username and content:
        add_post(username, content)

    return redirect(url_for('index'))


@app.route('/init-db')
def create_database():
    init_db()
    return 'Database created successfully!'


if __name__ == '__main__':
    app.run(debug=True)