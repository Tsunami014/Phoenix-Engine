import random
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import *
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

import secrets
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

import side as s
g = s.Game()
croom = g.fc['rooms'][str(g.roomnum)]

# with Flask-WTF, each web form is represented by a class
# "Game" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
class Game(FlaskForm):
    inp = StringField('Input', validators=[DataRequired(), Length(1)])
    submit = SubmitField('Submit')

class SaveForm(FlaskForm):
    save = SubmitField('Save')
    back = SubmitField('Return to map selector')

class Selector(FlaskForm):
    myChoices = ['Forest out', 'hahahahahaAAAAA', 'making sure this works', 'by adding in more stuff'] #input SPECIFIC MAP NAMES HERE, MUST BE THE EXACT NAME OF THE MAP FILES IN THE 'maps/' FOLDER
    choice = SelectField(u'Field name', choices = myChoices, validators = [DataRequired()])
    submit = SubmitField('Submit')
    
def load_room_desc():
    out = ''
    out += "It is%s dark." % ("" if croom['dark'] else "n't") + '\n'
    
    #How this line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
    out += "You can " + ('not exit' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
            g.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]))) + '\n'
    
    #How these next 3 statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
    out += "There are these objects: " +         '['+"".join([i['identifier']+", " if i['type'] == 5 else '' for i in croom['objects']])+']' + '\n'
    out += "You can see: " +                     '['+"".join([i['identifier']+", " if i['type'] == 6 else '' for i in croom['objects']])+']' + '\n'
    out += "There are these people/monsters: " + '['+"".join([i['identifier']+", " if i['type'] == 4 else '' for i in croom['objects']])+']' + '\n'
    return out

@app.route('/fps')
def fps():
    the_answer = random.randint(25, 60)
    return (str(the_answer))

# all Flask routes below

@app.route('/', methods = ['GET', 'POST'])
def chooser():
    form = Selector()
    if form.validate_on_submit():
        name = form.choice.data
        return redirect("main/"+name+'/', 303)
    return render_template('selector.html', form=form)

@app.route('/main/<id>/', methods=['GET', 'POST'])
def index(id):
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = Game()
    form2 = SaveForm()
    name = ""
    g.log = []
    if form.validate_on_submit():
        name = g(form.inp.data)
        form.inp.data = ''
    if form2.validate_on_submit():
        if form2.save.data:
            lc = 'insertloadingcodehere'
            return redirect('save/'+lc, 307)
        if form2.back.data:
            return redirect(url_for('chooser'))
    return render_template('app.html', title=id, roomname=croom['name'].capitalize(), desc=croom['description'].strip(' \t\n'), bigdesc=load_room_desc().strip(' \t\n'), form=form, form2=form2, message=name.strip(' \t\n'), logs=str(g.log))

@app.route('/main/<id>/save/<code>', methods=['GET', 'POST'])
def save_slot(id, code):
    print(id, code)
    if id == "Unknown":
        # redirect the browser to the error template
        return render_template('404.html'), 404
    else:
        # pass all the data for the selected actor to the template
        return redirect('..')

# 2 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#use this if u want to.... I think you just copy the 404.html and rename it to 500
#@app.errorhandler(500)
#def internal_server_error(e):
#    return render_template('500.html'), 500

@app.errorhandler(400)
def internal_server_error(e):
    return render_template('400.html'), 400

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)