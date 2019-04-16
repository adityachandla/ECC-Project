from flask import render_template,redirect, url_for, session, flash
from auth import authentication, db
from auth.models import UserModel
from auth.forms import LoginForm, SignupForm


@authentication.route("/login",methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = UserModel.query.filter_by(username=form.username.data).first()
		if not user:
			flash("Username does not exist")
			return redirect(url_for("authenticate.login"))
		if user.password == form.password.data:
			session["username"] = form.username.data
			return redirect("/made")
		else:
			flash("Invalid Authentication")
			return redirect(url_for('authenticate.login'))
	return render_template("login.html",form=form)


@authentication.route("/signup",methods=["GET","POST"])
def signup():
	signup = SignupForm()
	if signup.validate_on_submit():
		if signup.password.data == signup.password_again.data:
			existing = UserModel.query.filter_by(username=signup.username.data).first()
			if existing:
				flash("This username is already taken.")
				return redirect(url_for('authenticate.signup'))

			new_person = UserModel(username=signup.username.data,password=signup.password.data,
				email=signup.email.data)
			db.session.add(new_person)
			db.session.commit()

			return redirect(url_for('authenticate.login'))
		else:

			flash("Passwords do not match")
			return redirect(url_for('authenticate.signup'))
	return render_template("signup.html",form=signup)


@authentication.route("/logout")
def logout():
	if 'username' in session:
		del session['username']
	return redirect(url_for("authenticate.login"))