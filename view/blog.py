from flask import Blueprint, render_template, redirect, url_for, request,session
from forms.add_post_form import AddPost
from forms.update_post_form import UpdatePost
from models.post import Posts
from config import db
import os
import re
import unicodedata


blog = Blueprint('blog', __name__)


def generate_slug(title):
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('utf-8')
    title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    title = re.sub(r'[\s-]+', '-', title).strip().lower()
    return title

@blog.route('/create', methods = ['GET', 'POST'])
def create():
    form = AddPost()
    if 'login' in session: 
        if request.method == 'POST':
            if form.validate_on_submit():
                title = request.form['title']
                title_slug = generate_slug(title)

                description = request.form['description']

                image = form.image.data
                image_path = os.path.join('static\\assets\\img', image.filename)
                image.save(image_path)
                post = Posts(slug = title_slug, title = title, description = description, image_path = image.filename, user_id = session['login'])
                db.session.add(post)
                db.session.commit()
                return redirect(url_for('blog.show', slug=title_slug))
            else:
                return render_template('blog/create.html', title = "Add Post", form = form, image_path = 'static/assets/img/home-bg.jpg')
        else:
            return render_template('blog/create.html', title = "Add Post", form = form, image_path = 'static/assets/img/home-bg.jpg')
    else:
        return redirect(url_for('home.index', image_path = 'static/assets/img/home-bg.jpg'))
        

@blog.route('/show/<slug>')
def show(slug):
    post = Posts.query.filter_by(slug=slug).first_or_404()
    print(post.id)
    return render_template('blog/show.html', post=post, image_path = f'static/assets/img/{post.image_path}', current_url=request.path, title = 'Show')


@blog.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = UpdatePost()
    post = Posts.query.get_or_404(id)
    form.title.data = post.title
    form.description.data = post.description
    if 'login' in session: 
        if request.method == 'POST':
            if form.validate_on_submit():
                post.title = request.form['title']
                post.description = request.form['description']
                if request.files['image']:
                    image = form.image.data
                    image_path = os.path.join('static\\assets\\img', image.filename)
                    image.save(image_path)
                    post.image_path = image.filename
                db.session.commit()
                return redirect(url_for('blog.show', slug = post.slug))
            else:
                return render_template('blog/update.html', post = post, form = form, current_url=request.path, image_path = f'static/assets/img/{post.image_path}', title = 'Update')
        else:
            return render_template('blog/update.html', post = post, form = form, current_url=request.path, image_path = f'static/assets/img/{post.image_path}', title = 'Update')
    else:
        return redirect(url_for('home.index', image_path = 'static/assets/img/home-bg.jpg'))
    

@blog.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    if 'login' in session:
        if request.method == 'POST' or request.method == 'GET':
            post = Posts.query.filter_by(id = id).first_or_404()
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for('home.index'))
    else:
            return redirect(url_for('home.index'))
