from flask import Flask, render_template
import requests as r
from post import Post

posts = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_list = []
for post in posts:
    post_obj = Post(post)
    post_list.append(post_obj)
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=posts)


@app.route('/post/<int:id>')
def post(id):
    specific_post = None
    for each in post_list:
        if each.id == id:
            specific_post = each
    print(specific_post.title)
    return render_template("post.html", post=specific_post)

if __name__ == "__main__":
    app.run(debug=True)
