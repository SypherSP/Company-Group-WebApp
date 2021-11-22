from CG import app
from flask import render_template, flash, send_file, redirect, url_for
from CG.scripts import generateFile
from CG.forms import URLForm


@app.route("/", methods=["POST", "GET"])
@app.route("/home/", methods=["POST", "GET"])
@app.route("/index/", methods=["POST", "GET"])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = form.url.data
        res = inputRecieved(url)
        # activate download option
        if(res=="ERROR"):
            return render_template('index.html', form=form)
        else:
            return redirect(url_for('downloadFile'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
        return render_template('index.html', form=form)

    return render_template('index.html', form=form)


def inputRecieved(URL):
    # calling the getFile function to generate the file
    # with the user data in the post request
    # and enabling the download button
    res = generateFile.execute(URL)
    if res != "ERROR":
        flash("successifully created file", category='success')
        print(res)

    else:
        flash("Error while retrieving data", category='danger')
        # store the urls which caused errors
    return res

@app.route("/downloadfile/")
def downloadFile():
    return render_template("download.html")

@app.route("/download/")
def download():
    # return file here
    return redirect(url_for("index"))

@app.route("/contact/")
def contact():
    return render_template('contact.html')
