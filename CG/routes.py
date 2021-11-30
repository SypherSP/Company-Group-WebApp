from CG import app
from flask import render_template, flash, send_file, session, redirect, url_for
from CG.scripts import generateFile
from CG.forms import URLForm
import os


@app.route("/", methods=["POST", "GET"])
@app.route("/home/", methods=["POST", "GET"])
@app.route("/index/", methods=["POST", "GET"])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = form.url.data
        res = inputRecieved(url)
        # activate download option
        if(res == "ERROR"):
            return indexPage(form)
        else:
            session['name'] = res
            return render_template('index.html', form=URLForm(), isPrepared=True)
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
        return indexPage(form)

    return indexPage(form)

def indexPage(form):
    session.pop('name', default=None)
    return render_template('index.html', form=form, isPrepared=False)

def inputRecieved(URL):
    # calling the getFile function to generate the file
    # with the user data in the post request
    # and enabling the download button
    val = generateFile.execute(URL)
    if val != "ERROR":
        flash("successifully created file", category='success')

    else:
        flash("Error while retrieving data", category='danger')
        # store the urls which caused errors
    return val


@app.route("/downloadfile/")
def downloadFile():
    # return file here isntead
    try:
        if 'name' in session:
            if(session['name'] != "" and session['name'] != "ERROR"):
                return send_file(f'.\\outputs\\{session["name"]}_company_group.xlsx')
        else:
            flash("Fill the form before visiting this URL", category='danger')
            return redirect(url_for('index'))
    except:
        flash("Error while retrieving file, please try again", category='danger')
        return redirect(url_for('index'))


@app.route("/contact/")
def contact():
    return render_template('contact.html')
