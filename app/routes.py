from flask import render_template, redirect, url_for, flash
from app import app 
from app.forms import Contact
from app.models import Address_Book


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def add_contact():
    form = Contact()
    if form.validate_on_submit():
        first_name = form.first.data
        last_name = form.last.data
        phone_num = form.phone.data
        home = form.home.data
        print(first_name,last_name,phone_num,home)
        
        check_contact = Address_Book.query.filter( (Address_Book.first_name == first_name) and (Address_Book.last_name==last_name)).first()
        if check_contact is not None:
            flash("This person is already in your addressbook.", 'danger')
            return redirect(url_for('contacts'))
        new_contact = Address_Book(first_name=first_name,last_name=last_name,phone_num=phone_num,home=home)
        flash(f"{new_contact} was uploaded to your contacts.", "success")
        return redirect(url_for('index'))
    
    return render_template('contacts.html', form=form)