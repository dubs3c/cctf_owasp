import os
from flask import render_template, session, request, escape, redirect, flash, url_for, abort
import config
import queries as qry
import util
from time import gmtime, strftime

app = config.app

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    error = None
    if 'logged_in' in request.cookies and 'username' in request.cookies:
        if request.cookies.get('logged_in') == 1:
            return redirect(url_for('hello'))

    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])
        hashed = util.secure_md5_hashing(password)
        results = config.query_db("select username from users where \
                                    email='{email}' and password='{hashed}' limit 1"
                                    .format(email=email, hashed=hashed), one=True)
        if results:
            flash('You were successfully logged in', 'success')
            resp = app.make_response(redirect(url_for('hello')))
            resp.set_cookie('username',value=results['username'])
            resp.set_cookie('logged_in',value='1')
            return resp
        else:
            error = 'Invalid credentials'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    if 'logged_in' in request.cookies and 'username' in request.cookies:
        if request.cookies.get('logged_in') == 1:
            return redirect(url_for('hello'))

    flash('You were successfully logged out', 'success')
    resp = app.make_response(redirect(url_for('hello')))
    resp.set_cookie('username', expires=0)
    resp.set_cookie('logged_in', expires=0)
    return resp


@app.route("/blog")
def blog():
    cur = qry.get_all_posts()
    return render_template('blog.html', posts=cur)


@app.route("/blog/<slug>")
def view_post(slug):
    cur = qry.get_post(slug)
    if not cur:
        return abort(404)
    return render_template('post.html', post=cur)


@app.route("/profile")
def profile():
    if 'logged_in' not in request.cookies and 'username' not in request.cookies:
        return redirect(url_for('hello'))
    profile = qry.get_profile(request.cookies.get('username'))
    return render_template('profile.html', profile=profile)


@app.route("/register", methods = ['POST', 'GET'])
def register():
    if 'logged_in' in request.cookies and 'username' in request.cookies:
        return redirect(url_for('hello'))
    error = None

    if request.method == 'POST':
        email = escape(request.form['email'])
        username = escape(request.form['username'])
        password = escape(request.form['password'])
        hashed = util.secure_md5_hashing(password)
        registered = qry.register_account(username, email, hashed)
        if registered:
            flash('You were successfully registered', 'success')
            resp = app.make_response(redirect(url_for('hello')))
            resp.set_cookie('username', value=username)
            resp.set_cookie('logged_in', value='1')
            return resp
        else:
            error = 'Something went wrong when registring your account'

    return render_template('register.html', error=error)

#################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    config.init_db()
    app.run(host="0.0.0.0")
