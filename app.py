from flask import Flask, render_template, redirect, url_for
from models import db, Pet, Pet_Type
from forms import PetForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = '9b1b0e5f93904a15c5824416f9a0a8b6'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
 form = PetForm()
 if form.validate_on_submit():
  pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
  pet_type = Pet_Type(name=form.name.data, type=form.type.data)
  db.session.add(pet)
  db.session.add(pet_type)
  db.session.commit()
  return redirect(url_for('index'))
 pets = Pet.query.all()
 pet_type = Pet_Type.query.all()
 return render_template('view_pets.html', form=form, pets=pets, pet_type=pet_type)
if __name__ == '__main__':
 app.run(debug=True)