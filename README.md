# Case GOL
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)

> Case técnico disponibilizado pela **GOL Linhas Aéreas**, com o objetivo de desenvolver uma aplicação web para visualização de dados de RPK a partir de filtros de mercado e período.

---

## Requisitos do Case

- [x] Aplicação desenvolvida em **Python Flask**
- [x] Banco de dados com os seguintes critérios:
  - **Mercado** = Aeroporto de origem + aeroporto de destino, em ordem alfabética
  - Exemplo:
    - Origem = SBSV | Destino = SBGR → Mercado = SBGRSBSV
    - Origem = SBGR | Destino = SBSV → Mercado = SBGRSBSV
- [x] Tabela contendo as colunas:
  - ANO
  - MÊS
  - MERCADO
  - RPK
- [x] Autenticação de usuários (login)
- [x] Filtro por mercado
- [x] Filtro por intervalo de datas
- [x] Gráfico de RPK (eixo Y) por data (eixo X)

### Entregáveis

- [x] Repositório no GitHub
- [x] Aplicação containerizada
- [x] Aplicação publicada

---

## Índice
1. [Descrição](#descrição)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Requisitos](#requisitos)
5. [Como Rodar a Aplicação](#como-rodar-a-aplicação)
6. [Estrutura de Diretórios](#estrutura-de-diretórios)

---

## Descrição

Aplicação web desenvolvida com **Flask** para análise e visualização de dados de RPK, permitindo que usuários autenticados filtrem informações por mercado e intervalo de datas.  
Os dados são processados a partir de um banco PostgreSQL e apresentados por meio de gráficos interativos, simulando um cenário real de análise de dados no contexto da aviação comercial.

## Funcionalidades
- **Criação automática de Banco de Dados e Aplicação Backend**:
    - Cria e inicia automaticamente o banco de dados com suas dependencias e tabelas e a aplicação backend com o Docker Compose
- **Cadastro de usuários**: 
    - Os usuários podem se registrar na aplicação.
- **Login de usuários**: 
    - Autenticação de usuario para acessar pagina de dashboard.
    - Caso usuario esteja logado há mais de 10 minutos, a sessão é encerrada. 
- **Gerar gráfico (caso logado)**: 
    - Os usuários podem filtrar e gerar gráfico em linha para o filtro selecionado.

---

## Tecnologias Utilizadas

A aplicação foi desenvolvida com as seguintes tecnologias:

- **Python 3.12.3**
- **Flask**
- **Flask-Login**
- **SQLAlchemy**
- **Pandas**
- **Plotly**
- **Docker**

---

## Requisitos

Para rodar a aplicação, é necessário ter instalado as seguintes tecnologias:

- [Docker](https://www.docker.com/products/docker-desktop/)


## Como Rodar a Aplicação

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/dev-emanuelpereira/case-gol.git
cd case-gol
```

### 2. Descompactar Base de Dados
Descompacte o arquivo ```case_gol.zip``` dentro do diretório ```case-gol/db/``` para que o Docker consiga ler e criar o container com todos os dados no PostgreSQL dentro do Docker.

```
db/
├── dados_postgres/
├── → case_gol.zip ←
└── Dockerfile
```


### 3. Iniciar Docker

Em seguida, dentro da pasta raiz do projeto (```case-gol/```), crie e inicie o Docker Compose da aplicação com o seguinte comando:

```docker
docker-compose up --build 
```

### 4. Inserir host e porta no navegador

Após os passos anteriores, já é possível rodar a aplicação no navegador. Coloque o seguinte host e port no navegador:

```
http://127.0.0.1:5000/login/
```

#### Realizando todos os passos com sucesso, o projeto fica acessível para uso.

## Estrutura de Diretórios

```
case-gol/
│
├── backend/
├── frontend/
├── db/
│
└── docker-compose.yml
```
```case-gol/ (raiz do projeto)``` │ Sumário de cada pasta/arquivo:

- ```backend/``` : Diretório onde estão todos os arquivos/pacotes da aplicação backend.
- ```frontend/``` : Diretório dos templates do frontend.
- ```db/``` : Diretório responsável por armazenar o banco de dados.
- ```docker-compose.yml``` : Arquivo responsável por configurar o Docker Compose.


### Backend

```
backend/
│
├── ambvir/
├── logs/
├── model/
│   └── MercadoModel.py
│   └── UsuarioModel.py
│
├── routes/
│   └── AuthRoute.py
│   └── DashboardRoute.py
│
├── services/
│   └── AuthService.py
│   └── DashboardService.py
│
│
├── app.py
├── Dockerfile
├── requirements.txt
└── sql.py
```

```backend/``` │ Sumário de cada pasta/arquivo:

- ```ambvir/``` : Ambiente virtual da aplicação.
- ```logs/``` : Pasta onde são armazenados os arquivos de log da aplicação.
- ```routes/``` : Configurações das rotas e endpoints.
- ```model/``` : Entidades para transição de dados entre aplicação e banco de dados.
- ```services/``` : Regras de negócio.
- ```app.py``` : Aplicação principal, responsável por rodar todo o projeto.
- ```database.db``` : Banco de dados.
- ```Dockerfile``` : Arquivo de configuração do Docker.
- ```requirements.txt``` : Dependências do código.
- ```sql.py``` : Arquivo responsável por conexão com o banco de dados.

### Frontend
```
frontend/
├── static/
│   └── imagens/
│   │   └── background.jpg
│   │   └── favicon.ico
│   └── cadastro.css
│   └── dashboard.css/
│   └── index.css/
│
└── templates/
    └── index.html
    └── cadastro.html
    └── dashboard.html
```

```frontend/``` │ Sumário de cada pasta/arquivo:

- ```static/``` : Diretório para arquivos estáticos: CSS e imagens
- ```templates/``` : Arquivos HTML

### DB
```
db/
├── dados_postgres/
├── case_gol.zip
└── Dockerfile
```

```db/``` │ Sumário de cada pasta/arquivo:

- ```dados_postgres/``` : Pasta de transição de dados das tabelas entre container e maquina local.
- ```case_gol.zip``` : Backup do banco de dados.
- ```Dockerfile``` : Arquivo de configuração do Docker.

---

## Autor
### Emanuel Pereira
- 🔗 *Github:* https://github.com/dev-emanuelpereira 
