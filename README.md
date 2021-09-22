# Eigen-Face
Thanks to my Math 318 instructor in University of Washington, who gave me
the inspiration to launch this little project as my first step on machine
learning and computer vision.
## Intro
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
- static: because this is a Flask project (Flask is a kind of python web framework), 
  by convention, we need to put all front-end stuffs (Javascript, CSS) but except html into a directory
  called "static".
- templates: also by Flask's convention, it's necessary to put the html file into a 
  directory called "templates".
- main.py: the main/server of this project.
### Some disclaimers

## Demo

## Theorem
