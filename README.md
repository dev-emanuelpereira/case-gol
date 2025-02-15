# Case GOL

> Case disponibilizado pela GOL Linhas Aéreas com o objetivo de desenvolver uma > aplicação web com os seguintes requisitos:

- [x] Aplicação deve ser desenvolvido utilizando Python Flask (preferencialmente)
- [x] Banco de dados contendo os seguintes filtros:
    - [x] MERCADO = AEROPORTO DE ORIGEM + AEROPORTO DE DESTINO, em ordem alfabética.
    - [x] Exemplo1: Origem = SBSV, Destino = SBGR -> Mercado = SBGRSBSV
    - [x] Exemplo2: Origem = SBGR, Destino = SBSV -> Mercado = SBGRSBSV
- Contendo uma tabela, contendo as colunas:
    - [x] ANO
    - [x] MES
    - [x] MERCADO
    - [x] RPK
- [x] Autenticação do usuário (login)
- [x] Filtro para o usuário selecionar o mercado
- [x] Filtro para selecionar o intervalo de datas (ANO/MÊS ou data inteira, de sua preferência)
- [x] Gráfico do RPK (eixo y) por data (eixo x), para o mercado e intervalo de datas selecionado pelo usuário

Por fim, a entrega deve conter:
- [x] Repositório github com os códigos
- [x] Container da aplicação
- [x] Link da aplicação publicada

## Índice
1. [Descrição](#descrição)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Funcionalidades](#funcionalidades)
4. [Como Rodar a Aplicação](#como-rodar-a-aplicação)
5. [Estrutura de Diretórios](#estrutura-de-diretórios)
6. [Contribuindo](#contribuindo)
7. [Licença](#licença)

## Descrição

Esta aplicação web foi desenvolvida utilizando o framework **Flask** e tem como objetivo filtrar informações inseridas pelo usuario (logado) e mostrar grafico na tela base o que foi encontrado no banco de dados.

### Funcionalidades
- **Criação automática de Banco de Dados**:
    - Cria automaticamente o banco de dados com suas dependencias e tabelas caso o programa identifique que o mesmo ainda não existe.
- **Cadastro de usuários**: 
    - Os usuários podem se registrar na aplicação.
- **Login de usuários**: 
    - Autenticação de usuario para acessar pagina de dashboard.
    - Caso usuario esteja logado há mais de 10 minutos, a sessão é encerrada. 
- **Gerar gráfico**: 
    - Os usuários podem filtrar e gerar gráfico em linha para o filtro selecionado.
## Tecnologias Utilizadas

A aplicação foi desenvolvida com as seguintes tecnologias:

- **Python 3.12.3**
- **Flask**
- **Flask-Login**
- **SQLAlchemy**
- **Pandas**
- **Plotly**
- **Docker**

## Requisitos

Para rodar a aplicação, é necessário ter instalado as seguintes tecnologias:

1. [Docker](https://www.docker.com/products/docker-desktop/)
2. [Python](https://www.python.org/downloads/)


## Como Rodar a Aplicação

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/dev-emanuelpereira/case-gol.git
cd case-gol
```

### 2. Iniciar Docker

Em seguida, crie e inicie uma imagem docker da aplicação com o seguinte comando:
```cmd
docker build -t app:v1.0 .
docker run -dp 5000:5000 app:1.0
```

### 3. Inserir host e porta no navegador

Após os passos anteriores, já é possível rodar a aplicação no navegador. Coloque o seguinte host e port no navegador:

```
http://127.0.0.1:5000/login/
```

#### Realizando todos os passos com sucesso, o projeto fica acessível para uso.

## Estrutura de Diretórios

Para a estrutura de diretórios, segue a seguinte:
```
case-gol/
│
├── ambvir/
├── configuration/
├── material/
├── model/
├── routes/
├── model/
├── services/
├── static/
├── templates/
│
├── app.py
├── database.db
├── Dockerfile
├── requirements.txt
└── sql.py
```

Explicação de cada pasta/arquivo:

- ```ambvir/``` : Ambiente virtual da aplicação
- ```configuration/``` : Possui arquivos de configuração da aplicação
- ```material/``` : Possui os arquivos necessários para criação do banco de dados
- ```routes/``` : Configurações das rotas e endpoints
- ```model/``` : Entidades para transição de dados entre aplicação e banco de dados
- ```services/``` : Regra de negócio
- ```static/``` : Arquivos estáticos, neste caso, imagem background
- ```app.py``` : Aplicação principal, responsável por rodar todo o projeto
- ```database.db``` : Banco de dados
- ```Dockerfile``` : Arquivo de configuração do Docker
- ```requirements.txt``` : Dependências do código
- ```sql.py``` : Arquivo responsável por conexão com o banco de dados