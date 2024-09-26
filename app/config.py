import os

SECRET_KEY = 'secret-key'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\User\\Desktop\\даша\\сессия\\веб\\std_2440_exam.sqlite3'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\User\\Desktop\\даша\\сессия\\веб\\std_2440_exam.sqlite3'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_2440_exam:Thetreeoflive2005@std-mysql.ist.mospolytech.ru/std_2440_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')
PER_PAGE = 10

ADMIN_ROLE_ID = 1
MODERATOR_ROLE_ID = 2
USER_ROLE_ID = 3