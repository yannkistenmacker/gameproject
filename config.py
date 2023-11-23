from jogoteca import app

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqlconnector://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+connector',
        usuario='root',
        senha='Tryh4ckm3.',
        servidor='localhost',
        database='jogoteca'
    )