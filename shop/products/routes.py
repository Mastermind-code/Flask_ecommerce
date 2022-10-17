# from flask import render_template, session, request, redirect, url_for, flash, current_app

# from shop.admin.forms import RegistrationForm


# from shop import app,db,photos, search
# from .models import Category,Brand,Addproduct
# from .forms import Addproducts
# import secrets
# import os

# @app.route('/register', methods=['Post', 'Get'])
# def registration():
#     form = RegistrationForm(request.form)
#     if request.method == 'Post' and form.validate():
#         # user = User(form.username.data, form.email.data, form.password.data)
#         flash('Registration Successful')
#         return redirect(url_for('login'))
#     return render_template('admin/Register.html', form=form, title='Registration page')
