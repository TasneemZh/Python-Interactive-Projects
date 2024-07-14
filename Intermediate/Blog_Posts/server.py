from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()


@app.route('/')
def get_homepage():
    blog_posts = post.fetch_posts()
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    post_details = post.fetch_post(post_id)
    return render_template("blog-details.html", post_details=post_details)


@app.route('/contacts')
def get_contact_info():
    return render_template("contact.html")


@app.route('/about_us')
def get_about_us_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
