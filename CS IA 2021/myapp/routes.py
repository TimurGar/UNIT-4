from datetime import datetime

from myapp import app, db
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, current_user, logout_user, login_required
from myapp.forms import LoginForm, RegistrationForm, NewProjectForm, EditProjectForm, NewItemForm
from myapp.models import User, Project, Item


@app.route('/')
@app.route('/index')
@login_required
def index():
    projects = Project.query.order_by(Project.timestamp.desc()).filter_by(
        author=current_user)

    return render_template('index.html', title='Home', projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check to prevent logged-in users to login again
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # If the form is filled out completely(all required fields are completed) = True
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # Creating a flash messages

            flash('Invalid username or password')
            return redirect(url_for('login'))

        # Function that will remember user id from flask-login feature(read __init.py)
        login_user(user, remember=form.remember_me.data)

        # Redirect a user to a page that he wanted to access before logging in
        # And make sure that user doesn't put malicious command into the url(after next)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    print(current_user.get_id())
    return render_template('login.html',title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check to prevent logged-in users to login again
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/user/<name>')
@login_required
def project_profile(name):
    project = Project.query.filter_by(name=name).first_or_404()

    page = request.args.get('page', 1, type=int)

    # Fix
    # items = project.order_by(Item.timestamp.desc()).paginate(
    #     page, app.config['POSTS_PER_PAGE'], False)
    # next_url = url_for('index', page=items.next_num) \
    #     if items.has_next else None
    # prev_url = url_for('index', page=items.prev_num) \
    #     if items.has_prev else None

    return render_template('project_profile.html', project=project, )
    # items = items.items

@app.route('/new_project', methods=['GET', 'POST'])
@login_required
def new_project():
    form = NewProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, description=form.description.data,
                          author=current_user)
        current_project_name = form.name.data

        db.session.add(project)
        db.session.commit()
        flash('Congratulations, you successfully created a new project!')
        return redirect(url_for('index'))

    return render_template('new_project.html', title='New Project', form=form)

@app.route('/edit_project', methods=['GET', 'POST'])
@login_required
def edit_project():
    form = EditProjectForm()
    if form.validate_on_submit():
        # query doesn't work
        project = Project.query.filter_by(name=form.name.data)
        print(project)
        project.name = form.name.data
        project.description = form.description.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_project'))

    # Auto paste the initial data
    # elif request.method == 'GET':
    #     project = Project.query.filter_by(name=form.name.data)
    #     form.name.data = project.name
    #     form.description.data = project.description

    return render_template('edit_project.html', title='Edit Project', form=form)


@app.route('/new_item', methods=['GET', 'POST'])
@login_required
def new_item():
    form = NewItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, description=form.description.data,
                    model_or_type=form.model_or_type.data, size=form.size.data,
                    quantity=form.quantity.data, weight=form.weight.data,
                    cost=form.cost.data)
        db.session.add(item)
        db.session.commit()
        flash('Item has been successfully added')

        return redirect(url_for('project_profile', name=current_user.project.name))  # <-- PROBLEM: USER has no project
    return render_template('new_item.html', title='New Item', form=form)

# current_user.id

# project = Project.query.filter_by(user_id=current_user.id).first()
# project.name