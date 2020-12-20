import os
import secrets
from flask import Flask, render_template, redirect, request

from core.ml.new_detector import classify_image

app = Flask(__name__)
# root directory


@app.route('/')
def root():
    return render_template('home.html')


current_dir = os.getcwd()
upload_dir = os.path.join(current_dir, 'core', 'ml', 'upload')

extensions = ['png', 'jpg', 'jpeg']


def allowed_extension(filename):
    if '.' not in filename:
        return False

    extension = filename.rsplit('.', 1)[1]
    if extension in extensions:
        return True
    else:
        return False


def generate_filename(image):
    filename = image.filename
    filextension = filename.rsplit('.', 1)[1]
    filename = secrets.token_hex(20) + '.' + filextension
    return filename


@app.route('/tool', methods=["GET", "POST"])
def upload():
    res = []
    if request.method == "POST":
        if request.files:
            image = request.files["image"]

            # validation
            if not allowed_extension(filename=image.filename):
                return redirect(request.url)

            new_filename = generate_filename(image)
            image.save(os.path.join(upload_dir, new_filename))
            file_path = os.path.join('core', 'ml', 'upload', new_filename)
            res = classify_image(file_path=file_path)
            print(res)
            os.remove(file_path)
            redirect(request.url)

    return render_template('tool.html', data=res, zip=zip)


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/about-us')
def about_us():
    return render_template('About Us.html')
