from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:$uportE99@localhost/atividades'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.models.tables import Usuario
from app.models.tables import Atividade

@app.route('/home')
def home():
    title = "Atividades Complementares"
    usuarios = Usuario.query.all()
    return render_template('index.html', titulo=title, usuarios=usuarios)

