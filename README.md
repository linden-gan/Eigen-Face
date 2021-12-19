# Eigen-Face
Thanks to my Math 318 instructor in University of Washington, who gave me
the inspiration to launch this little project as my first step on machine
learning and computer vision.
## Structure
So, let's be concise and straightforward: this is a python-based full-stack
project, in which users can choose "sign up" to record their face information in the database
so that when they "sign in" at the next time, the system will hopefully 
recognize and admit them. Users who didn't "sign up" will not leave information and thus not be recognized.
The method used to process human faces is called Eigenface Method, which I'll
elaborate later.
  
To help you navigate through my project, here is the navigator:
- .idea: things related to IDEA.
- src: the real meat, including all python back-end codes and logic.
  - db: database storing users' face information in form of .npy file, with additional
    script files used to manipulate and view this database
  - eigenface: the main eigenface algorithm is here!
    - Service: contains back-end logic of "sign in" and "sign up" functions
    - Training: all files needed for the machine learning training process, including
      "Data" directory for all training data, train.py for the training script, and .npy
      files for training outcome's models
    - commons: some public, tool-like files for raw image processing
- static: because this is a Flask (a python web framework) project, 
  by convention, we need to put all front-end stuffs (Javascript, CSS) but except html into a directory
  called "static".
- templates: also by Flask's convention, it's necessary to put the html file into a 
  directory called "templates".
- main.py: the main/server of this project.

## Overview
Generally, you can view this project as a sample machine learning model project. Our goal is to have a model so that 
given an input human face image, it can analyze the main components of this face and compare to existing faces in our
database, and eventually determine whether the person this face belongs to is in our recognized user or not. 

First, similar to almost every machine learning process, we train our model. The specific training code is in train.py
inside of the Training directory (I didn't commit my training data file since it contains my friends' and my private photos
(yeah we need human faces :P), which means you need to collect your training data by your own). Basically, the mathematical
abstraction of training is just linear algebra: an image is merely a set of numerous RGB values, and by converting it to
grey scale, we can have a vector with _n_ entries with values from 0 to 255. Assume we have _m_ images, then we can put these _m_
image vectors into the _m_ rows of a matrix, thus forming an _m_ by _n_ matrix _M_. We compute the dot product of _M_ and _M_'s transpose, 
which is _M_'s covariance matrix. Next, we compute the eigenvectors of it. Each eigenvector represent one component, or
dimension/characteristic, of a human face.

Now, suppose we have eigenvectors e_1, e_2, e_3, ..., e_m. Note that eigenvectors with the bigger eigenvalues are more
"important", or "dominant", and vice versa. Now, we can concisely represent any human faces by the linear combination
of these _m_ eigenvectors. For example, face _A_ is approximately `1.6` times e_1 plus `-10.4` times e_2 plus ... plus `0.01` times
e_m. By approximately, it means we are actually working on the _projection_ of face _A_ to the characteristic subspace spanned
by those eigenvectors. Projection is the best approximation we can make. Now, we can have a unique "key" for each face! For face
A, its key is `1.6`, `-10.4`, ..., `0,01`. Note that these keys can best capture the main characteristics of a human face, since 
it's derived from the eigenvectors. We store each user's key in database, and when someone scans their face to try to log in, we use
the same method to generate a key for this unknown face, and compare this key to keys in database. If the difference (2-norm) between
this face and a face in our database is small enough, then we are confident to say that these two faces belong to the same person. So,
we recognize this user and allow they to log in.
 
That's pretty much the general picture of this project. Feel free to check or download the code for greater detail.
