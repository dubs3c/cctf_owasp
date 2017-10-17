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

@app.route("/blog", methods=['GET'])
def view_post():
    blogID = request.args.get('blog')
	
    if(blogID is None):
        return blog()
    else:
        cur = qry.get_post(blogID)
        if not cur:
            return abort(404)
        return render_template('post.html', post=cur)

def blog():
    cur = qry.get_all_posts()
    return render_template('blog.html', posts=cur)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    config.init_db()
    app.run(host="0.0.0.0", port=5001)
