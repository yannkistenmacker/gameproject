views.py

@app.route('/')
Rota para a index da aplicacao.


@app.route('/novo')
Rota para cadastro de novo jogo onde sera verificado se o usuario esta logado na sessao,
caso esteja logado sera redirecionado para a pagina de criacao, se nao redirecionado para a pagina de login


@app.route('criar')
Rota para comunicacao com o banco de dados utilizando o POST para adicionar o jogo no banco. Caso o jogo
ja exista no banco, ele retorna uma mensagem informando que ja existe. E no final da funcao, estamos recebendo
a imagem de capa do jogo, onde o path de armazenamento esta configurado no arquivo config.


@app.route('/editar/<int:id>')
Rota editar informacoes de jogos ja cadastrados. Primeiro faz a checagem se o usuario esta logado,
se estiver sera redirecionado para a pagina editar, se nao, redirecionado para a pagina de login.
Depois é realizado uma consulta com o SQLalchmey filtrando pelo primeiro ID, em seguida recupera
a imagem do jogo pelo ID e redireciona pra pagina editar.


@app.route('deletar/int:id>')
Rota para deletar determinado jogo, primeiro checamos se o usuario esta logado, se nao
redirecionamos para a pagina de login. Caso esteja logado, a rota se comunica com o banco, executando
um delete.


@app.route('autenticar', methods=['POST', ])
Rota para autenticacao do usuario na aplicacao. O usuario entra com o login e senha e essas informacoes
sao armazenadas na sessao(session fornecida pelo Flask) do usuario. A variavel usuario armazena uma consulta realizada
dentro do banco de dados com a seguinte query: usuarios.query.filter_by(nickname=request.form['usuario']).first(), que
se comunica diretamente com o request html da pagina de login. Em seguida valida a entrada de senha com a senha cadastra
da no banco e armazena no session. Caso a senha esteja errada, o usuario é redirecionado para a pagina de login.





helpers.py
Configuracao de funcao para definir o diretorio de onde e como a imagem sera armazenada de forma dinamica.


models.py
Class Jogos estamos configurando com python a tabela jogos com suas respectivas colunas.
Class Usuarios estamos configurando com python a tabela usuario com suas respectivas informacoes.


config.py
Estamos configurando os acessos da aplicacao com o banco de dados.