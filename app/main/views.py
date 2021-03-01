from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import Pitches,Role,User,Comments
from . import main
from flask import render_template
from .. import db,photos
from .forms import PitchForm,CommentForm,UpdateProfile


@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Welcome to Pitch Application!!"
    title= 'Pitch-app!'
    return render_template('index.html', message=message,title=title)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        title=form.title.data

        # Updated pitchinstance
        new_pitch = Pitches(title=title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form= form)

@main.route('/categories/<cate>')
def category(cate):
    '''
    function to return the pitches by category
    '''
    category = Pitches.get_pitches(cate)
    # print(category)
    title = f'{cate}'
    return render_template('categories.html',title = title, category = category)
