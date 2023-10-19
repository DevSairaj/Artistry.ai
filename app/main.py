# import cv2
# import os
# from werkzeug.utils import secure_filename
# from flask import request, render_template
# from app import app
# from app.file import allowed_file
# from app.sketch import make_sketch


# UPLOAD_FOLDER = 'app/static/uploads'
# SKETCH_FOLDER = 'app/static/sketches'

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/sketch', methods=['GET', 'POST'])
# def sketch():
#     file = request.files['file']
#     if file and allowed_file(file.filename):
#         filename =secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
#         sketch_img = make_sketch(img)
#         sketch_img_name = filename.split('.')[0]+'_sketch.jpg'
#         save = cv2.imwrite(SKETCH_FOLDER+'/'+sketch_img_name, sketch_img)
#         return render_template('home.html', org_img_name=filename, 
#                                sketch_img_name=sketch_img_name)
#     return render_template('home.html')



# import cv2
# import os
# from werkzeug.utils import secure_filename
# from flask import request, render_template
# from app import app
# from app.file import allowed_file
# from app.sketch import make_sketch

# UPLOAD_FOLDER = 'app/static/uploads'
# SKETCH_FOLDER = 'app/static/sketches'

# @app.route('/')
# def index():
#   return render_template('index.html')

# @app.route('/sketch', methods=['GET', 'POST'])
# def sketch():
#   if request.method == 'GET':
#     return render_template('home.html')

#   file = request.files['file']

#   if file and allowed_file(file.filename):
#     filename = secure_filename(file.filename)
#     try:
#       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#       img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
#       sketch_img = make_sketch(img)
#       sketch_img_name = filename.split('.')[0]+'_sketch.jpg'
#       cv2.imwrite(SKETCH_FOLDER+'/'+sketch_img_name, sketch_img)
#     except Exception as e:
#       app.logger.error(e)
#       return render_template('home.html', error='Error processing file.')

#     return render_template('home.html', org_img_name=filename,
#                            sketch_img_name=sketch_img_name)

#   return render_template('home.html', error='Please upload an image file.')




import cv2
import os
from werkzeug.utils import secure_filename
from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for, session, flash
from app.file import allowed_file
from app.sketch import make_sketch

UPLOAD_FOLDER = 'app/static/uploads'
SKETCH_FOLDER = 'app/static/sketches'

from app.models import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id  # Set session for authenticated user
            # return redirect(url_for('index'))
            return redirect(url_for('index', user_id=user.id))  # Redirect to index page

        else:
            flash('Invalid username or password', 'error')  # Add this line
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user_id from the session
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'user_id' in session:
      return render_template('index.html')
    else:
      return redirect(url_for('login'))


@app.route('/sketch', methods=['GET', 'POST'])
def sketch():
  if request.method == 'GET':
    return render_template('home.html')

  file = request.files['file']

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    try:
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
      sketch_img = make_sketch(img)
      sketch_img_name = filename.split('.')[0]+'_sketch.jpg'
      cv2.imwrite(SKETCH_FOLDER+'/'+sketch_img_name, sketch_img)
    except Exception as e:
      app.logger.error(e)
      return render_template('home.html', error='Error processing file.')

    return render_template('home.html', org_img_name=filename,
                           sketch_img_name=sketch_img_name)

  return render_template('home.html', error='Please upload an image file.')
