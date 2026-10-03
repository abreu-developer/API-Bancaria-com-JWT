# JWD API — Estudo de API Bancária

API REST desenvolvida em **Python** e **Flask** com foco em estudos de arquitetura em camadas, autenticação JWT, persistência de dados e testes automatizados.

O projeto simula operações básicas de uma conta bancária, como cadastro de usuários, login e edição de saldo.

## 🚀 Tecnologias

* Python 3.13
* Flask
* SQLite
* JWT
* bcrypt
* pytest
* Git/GitHub

## 📁 Estrutura do projeto

```text
jwd-api-estudo/
├── src/
│   ├── controllers/
│   ├── drivers/
│   ├── errors/
│   ├── main/
│   │   ├── composers/
│   │   ├── middlewares/
│   │   ├── routes/
│   │   └── server/
│   ├── models/
│   └── views/
├── storage.db
├── requirements.txt
├── run.py
└── README.md
```

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura dividida em responsabilidades:

* **Routes** — recebem as requisições HTTP.
* **Views** — processam os dados da requisição e montam as respostas.
* **Controllers** — concentram as regras de aplicação.
* **Models/Repositories** — responsáveis pela comunicação com o banco de dados.
* **Drivers** — componentes externos, como JWT e conexão com banco.
* **Middlewares** — validações executadas antes do acesso às operações protegidas.
* **Composers** — responsáveis por montar as dependências necessárias para cada fluxo.

## 🔐 Autenticação

As rotas protegidas utilizam **JWT**.

A autenticação verifica:

1. O token enviado no header `Authorization`.
2. O identificador do usuário enviado no header `uid`.
3. O `user_id` armazenado dentro do JWT.
4. Se o usuário informado corresponde ao usuário autenticado.

Exemplo de headers:

```http
Authorization: Bearer SEU_TOKEN
uid: 13
```

## 📌 Endpoints

### Cadastro

```http
POST /bank/registry
```

Exemplo:

```json
{
    "username": "admin",
    "password": "admin"
}
```

### Login

```http
POST /bank/login
```

Exemplo:

```json
{
    "username": "admin",
    "password": "admin"
}
```

O login retorna as informações necessárias para autenticação através de JWT.

### Alterar saldo

```http
PATCH /bank/balance/<user_id>
```

Exemplo:

```http
PATCH /bank/balance/13
```

Headers:

```http
Authorization: Bearer SEU_TOKEN
uid: 13
```

Body:

```json
{
    "new_balance": 500.0
}
```

## 🧪 Testes

Os testes automatizados são executados utilizando `pytest`.

Para executar:

```bash
pytest
```

Para executar com mais detalhes:

```bash
pytest -v
```

## ⚙️ Instalação

Clone o projeto:

```bash
git clone https://github.com/abreu-developer/jwd-api-estudo.git
```

Entre no diretório:

```bash
cd jwd-api-estudo
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Executando o projeto

Com o ambiente virtual ativado:

```bash
python run.py
```

A API estará disponível localmente em:

```text
http://127.0.0.1:3000
```

## 🎯 Objetivos do projeto

Este projeto faz parte dos meus estudos de desenvolvimento **Back-end com Python** e tem como objetivo praticar:

* Desenvolvimento de APIs REST;
* Flask;
* Arquitetura em camadas;
* Separação de responsabilidades;
* Padrão Repository;
* Injeção de dependências;
* Autenticação com JWT;
* Criptografia de senhas com bcrypt;
* SQLite;
* Testes automatizados com pytest;
* Git e GitHub;
* Tratamento de erros HTTP.

## 📚 Status

🚧 Projeto em desenvolvimento e utilizado principalmente para fins de estudo.

Novas funcionalidades e melhorias de arquitetura serão adicionadas conforme o avanço dos estudos.

## 👨‍💻 Autor

**João Vitor Abreu**

Desenvolvedor Back-end focado em Python e desenvolvimento de APIs.

* [GitHub](https://github.com/abreu-developer)
* [LinkedIn](https://www.linkedin.com/in/vitorabreudev/)
* [Portfólio](https://vitorabreuportifolio.lovable.app)
