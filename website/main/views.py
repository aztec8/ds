from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, flash
from flask.ext.login import login_required, current_user
from .. import db
from ..models import User, Article
from ..email import send_email
from . import main
from .forms import NameForm, ProfileForm


@main.route('/', methods=['GET', 'POST'])
def index():
    articles = Article.query.order_by(Article.post_date.desc())
    latest_post = articles.first()
    recent_posts = articles[1:5]

    return render_template('ds/index.html',
        title = 'DS',
        description = 'Your source for the CONCACAF',
        page_id = 'homepage',
        data_page = 'homepage',
        latest_post=latest_post,
        recent_posts=recent_posts
        )


# about
@main.route('/about')
def about_ds():
    return render_template('ds/about.html')


# privacy
@main.route('/privacy-policy')
def privacy_policy():
    return 'DS privacy policy'



@main.route('/u/<username>', methods=['GET','POST'])
def view_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.fullname = form.fullname.data
        current_user.twitter = form.twitter.data
        current_user.instagram = form.instagram.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user)
        flash('Your profile has been updated!')
        return redirect(url_for('.view_profile', username=current_user.username))
    form.fullname.data = current_user.fullname
    form.twitter.data = current_user.twitter
    form.instagram.data = current_user.instagram
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    form.fullname.data = current_user.fullname

    return render_template('ds/profile.html', user=user, form=form)


@main.route('/u/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.fullname = form.fullname.data
        current_user.twitter = form.twitter.data
        current_user.instagram = form.instagram.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user)
        flash('Your profile has been updated!')
        return redirect(url_for('.view_profile', username=current_user.username))
    form.fullname.data = current_user.fullname
    form.twitter.data = current_user.twitter
    form.instagram.data = current_user.instagram
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    form.fullname.data = current_user.fullname
