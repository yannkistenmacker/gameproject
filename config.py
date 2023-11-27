import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqlconnector://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+connector',
        usuario='root',
        senha='password',
        servidor='localhost',
        database='jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
