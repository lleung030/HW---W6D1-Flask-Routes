from . import bp as app
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprint.blog.models import Post
from flask_login import current_user, login_required

@app.route('/posts')
@login_required
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html', posts=all_posts)

#create a route that allows us to get a single post based on its id 

@app.route('/post/<id>')
@login_required
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('post_single.html', post=post)

@app.route('/create_post', methods=["POST"])
@login_required
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    make = request.form['inputMake']
    model = request.form['inputModel']
    year = request.form['inputYear']
    color = request.form['inputColor']
    price = request.form['inputPrice']
    new_post = Post(title = title, body = body, make = make, model = model, year = year, color = color, price = price, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash('Post created successfully', 'success')
    return redirect(url_for('blog.posts')) 
