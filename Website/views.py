from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Post, User, Comment, Like
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():    
    posts = Post.query.all()
    return render_template("index.html", user=current_user, posts=posts)

@views.route("about")
def about():
    aboutContent = "Hi Folks, Madhav Here From India. This is my Final Project For CS50. This is basically a blog website using Flask, Python, SQL, HTML, CSS, JS, Bulma library, and Bootstrap. Any changes/improvements are welcome."
    return render_template("about.html", aboutContent=aboutContent, user=current_user)

@views.route("contact")
def contact():
    contactContent = "Hi Everyone, Madhav Here. You can contact me through my social media handles , gmail id (present in the footer), and on my office landline number. For Business Queries, contact me @+91-9999988888."
    return render_template("contact.html", contactContent=contactContent, user=current_user)

@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')
        title = request.form.get('title')
        if not text:
            flash("Post cannot be empty" , category='error')
        else:
            post = Post(text=text, title=title, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post Created", category='success')
            return redirect(url_for('views.home'))
    

    return render_template("create_post.html", user=current_user)

@views.route("/delete-post/<int:id>") # dynamic routing is done by angle brackets
@login_required
def delete_post(id):
    post_to_delete = Post.query.get_or_404(id)
    id = current_user.id
    if not post_to_delete:
        flash("Post does not exist", category='error')
    elif id != post_to_delete.author:
        flash("You do not have the permission to delete this post", category='error')
    else:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash("Post Deleted", category='success')

    return redirect(url_for('views.home'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user exists with that username", category='error')
        return redirect(url_for('views.home'))
    
    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)

@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    comment = request.form.get('comment')
    
    if not comment:
        flash('Comment Cannot Be Empty!', category='error')
    else:
        post = Post.query.filter_by(id=post_id)

        if post:
            comment_created = Comment(text=comment, author=current_user.id, post_id=post_id)
            db.session.add(comment_created)
            db.session.commit()
        else:
            flash('Post does not exist', category='error')

    return redirect(url_for('views.home'))

@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("Comment does not exist", category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash("You do not have the permission to delete this comment", category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))

@views.route("/like-post/<post_id>", methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(author=current_user.id , post_id =post_id).first()

    if not post:
        return jsonify({'error': 'Post Does Not Exist'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
    
    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})
