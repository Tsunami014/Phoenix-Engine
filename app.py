# This is the web app that uses game.py to run the game
import sys

sys.dont_write_bytecode = True

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import *
from wtforms.validators import DataRequired, Length

import pickle as pkl

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/save slots'

import secrets
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

import game as s
g = s.Game()

from random import choice
messages = ['imagine dying', 'skill issue', 'get dunked on', 'el bozo', 'you have health potions for a reason', '[insert bad game tip here]', '[insert random insult here]']

# with Flask-WTF, each web form is represented by a class
# "Game" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
class Game(FlaskForm):
    inp = StringField('Input', validators=[DataRequired(), Length(1)], render_kw={'autofocus': True})
    submit = SubmitField('Submit')

class SaveForm(FlaskForm):
    myChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    slot = SelectField(u'Save slot', choices=myChoices, validators=[DataRequired()])
    save = SubmitField('Save')
    load = SubmitField('Load')
    back = SubmitField('Return to map selector')

class Selector(FlaskForm):
    myChoices = ['Forest Of Wonder', 'Tech Labs', 'Ancient Egypt'] #input SPECIFIC MAP NAMES HERE, MUST BE THE EXACT NAME OF THE MAP FILES IN THE 'maps/' FOLDER
    choice = SelectField(u'Field name', choices = myChoices, validators = [DataRequired()])
    submit = SubmitField('Submit')
    
def load_room_desc(g):
    croom = g.fc['rooms'][str(g.roomnum)]
    objs = g.all_non_inventory_items()
    out = ''
    out += "It is%s dark." % ("" if croom['dark'] else "n't") + '\n'
    
    #How this line works is it says you can not exit if there are no exits otherwise it states all the exits and the direction of exit.
    out += "You can " + ('not exit' if len(croom['exits']) == 0 else ('exit ' + ", ".join(["%s towards %s" % (s.pos[int(i)], \
            g.fc["rooms"][str(croom['exits'][i])]["name"]) for i in croom['exits']]))) + '\n'
    
    #How these next 3 statements work: they basically make a string: "[item1, item2, item3]" for each item in the room's items that are of a certain type.
    out += "You have in your inventory: " +      '['+", ".join(['%i %ss' % (g.inventory[i][0], i) for i in g.inventory.keys()])+']' + '\n'
    out += "There are these objects: " +         '['+", ".join([i['identifier'] for i in objs if i['type'] == 5])+']' + '\n'
    out += "There are these people/monsters: " + '['+", ".join([i['identifier'] for i in objs if i['type'] == 4])+']' + '\n'
    out += "You can see: " +                     '['+", ".join([i['identifier'] for i in objs if i['type'] == 6])+']' + '\n'
    return out

# all Flask routes below

@app.route('/', methods = ['GET', 'POST'])
def chooser():
    global g
    form = Selector()
    if form.validate_on_submit():
        name = form.choice.data
        g.redirect = ''
        return redirect("main/"+name+'/', 303)
    return render_template('selector.html', form=form)

@app.route('/main/<id>/', methods = ['GET', 'POST'])
def index(id):
    global g
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = Game()
    form2 = SaveForm()
    name = ""
    savemsg = ""
    g.log = []
    if g.redirect:
            r = redirect(url_for(g.redirect))
            return r
    if form.submit.data and form.validate():
        name = g(form.inp.data)
        form.inp.data = ''
    if (form2.back.data or form2.save.data or form2.load.data) and form2.validate():
        if form2.back.data:
            return redirect(url_for('chooser'))
        elif form2.save.data:
            with open('saves/%s.save' % form2.slot.data, 'wb+') as f:
                f.write(pkl.dumps(g))
                f.close()
                savemsg = 'SUCESSFULLY SAVED FILE!!'
        elif form2.load.data:
            try:
                with open('saves/%s.save' % form2.slot.data, 'rb') as f:
                    g = pkl.loads(f.read())
                    f.close()
                    savemsg = 'SUCESSFULLY LOADED FILE!!'
            except Exception as e:
                savemsg = 'UNABLE TO LOAD FILE BECAUSE: %s' % e
    croom = g.fc['rooms'][str(g.roomnum)]
    gameinfo = ' HP: %s\nMonster health: ' % str(g.hp)
    gameinfo += str({i.name: i.hp for i in g.curmonsters})
    return render_template('app.html', title=id, roomname=croom['name'].capitalize(), desc=croom['description'].strip(' \t\n'), bigdesc=load_room_desc(g).strip(' \t\n'), form=form, form2=form2, message=name.strip(' \t\n'), logs=str(g.log), savemsg=savemsg, gameinfo=gameinfo)

@app.route('/death')
def death():
    return render_template('death.html', message=choice(messages), error='You appeared to have fallen during your adventure. Your grave was just a stick, rising into the cold, unforgiving air. No one will be around to mourn for your death.')

# 3 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500

@app.errorhandler(400)
def internal_server_error(e):
    return render_template('400.html', error=e), 400

# keep this as is
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)