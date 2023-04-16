from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import *
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# with Flask-WTF, each web form is represented by a class
# "NameForm" can change; "(FlaskForm)" cannot
# see the route for "/" and "index.html" to see how this is used
class NameForm(FlaskForm):
    inp = StringField('Input', validators=[DataRequired(), Length(1)])
    submit = SubmitField('Submit')

class Inputs(FlaskForm):
    myChoices = ['Forest out', 'hahahahahaAAAAA', 'making sure this works', 'by adding in more stuff'] #input SPECIFIC MAP NAMES HERE, MUST BE THE EXACT NAME OF THE MAP FILES IN THE 'maps/' FOLDER
    myField = SelectField(u'Field name', choices = myChoices, validators = [DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below

@app.route('/', methods = ['GET', 'POST'])
def chooser():
    form = Inputs()
    if form.validate_on_submit():
        name = form.myField.data
        return redirect("main/"+name, 303)
    return render_template('selector.html', form=form)

@app.route('/main/<id>', methods=['GET', 'POST'])
def index(id):
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    if form.validate_on_submit():
        name = form.inp.data
    try:
        message = name.lower()
    except:
        message = ""
    return render_template('app.html', title=id, form=form, message=message)

@app.route('/main/<id>/save/<code>')
def save_slot(id, code):
    print(id, code)
    if id == "Unknown":
        # redirect the browser to the error template
        return render_template('404.html'), 404
    else:
        # pass all the data for the selected actor to the template
        return index(id)

# 2 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#use this if u want to.... I think you just copy the 404.html and rename it to 500
#@app.errorhandler(500)
#def internal_server_error(e):
#    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)