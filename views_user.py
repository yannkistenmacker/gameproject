from jogoteca import app, db
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioCadastro
from flask_bcrypt import check_password_hash, generate_password_hash


# Criando rota para a pagina de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)

    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario nao logado!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if session['usuario_logado'] is None:
        flash('Usuario nao esta logado!')
        return redirect(url_for('index'))
    else:
        session['usuario_logado'] = None
        flash('Usuario deslogado com sucesso!')
        return redirect(url_for('index'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormularioCadastro(request.form)
    return render_template('cadastro.html', form=form)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = FormularioCadastro()

    nickname = form.nickname.data
    nome = form.nome.data
    senha = generate_password_hash(form.senha.data)

    name = Usuarios.query.filter_by(nickname=nickname).first()
    if name:
        flash('Usuario ja existe!')
        return redirect('cadastro')


    if form.validate_on_submit():
        nickname = form.nickname.data
        password = generate_password_hash(form.senha.data)

        new_user = Usuarios(nickname=nickname, nome=nome, senha=senha)
        db.session.add(new_user)
        db.session.commit()
        flash('Conta criada com sucesso')
        return redirect('/')
    return render_template('cadastro.html', form=form)
