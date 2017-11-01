#! usr/bin/python
# -*- coding: utf-8 -*-
import time
import subprocess
import hashlib
from flask import Flask, request, render_template
from flask_limiter import Limiter
import os
import config

def get_remote_address():
    return request.remote_addr
# Initialization of variables and modules
app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per second"]
)

def check_link(link):
    #Open page in firefox via slimer
    path = hashlib.sha256(link).hexdigest() + ".js"
    template = '''
var page = require("webpage").create();

page.open(atob("__URL__"))
    .then(function(status){
        x=1;
        setTimeout(function(){
            alerted = page.evaluate(function(){
                return window.hasAlerted;
            });
            if(alerted){
                console.log("WIN");
            }else{
                console.log("FAIL");
            }
            slimer.exit();
        }, 4000);
});
    '''
    with open(path, 'w') as f:
        f.write(template.replace("__URL__", link.encode("base64").strip().replace("\n","").replace("\r","")))
    #Run it in firefox
    process = subprocess.Popen('timeout -t 10 /usr/bin/slimerjs '+path, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    if "WIN" in out:
        win = True
    else:
        win = False

    #Remove temp js
    process = subprocess.Popen('/bin/rm '+ path, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return win
    
@app.route('/getflag', methods=['POST'])
@limiter.limit("3 per minute")
def getflag():
    link = request.form.get("link")
    if not link.startswith(config.PROTOCOL+'://'+config.HOST+':'+str(config.PORT)+'/'):
        return "Link must start with "+config.PROTOCOL+'://'+config.HOST+':'+str(config.PORT)+'/'
    if link:
        if check_link(link):
            return os.environ["FLAG"]
        else:
            return "Nope"

@app.after_request
def after_request(response):
    response.headers.add('X-XSS-Protection', '0')
    response.headers.add('X-Frame-Options', 'deny')
    return response

@app.route('/post')
def testflag():
    return render_template('post.html')
    
@app.route('/')
def main():
    return render_template('index.html')

## RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=config.DEBUG, threaded=True)