# Projeto Univali — Servidor Python + Flask

## Requisitos
- Python 3 instalado
- VS Code (recomendado)
- Terminal

## Instalação no Windows

Abra o terminal na pasta do projeto e execute:

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py


Se a ativação do ambiente virtual for bloqueada no PowerShell, use o terminal CMD:

venv\Scripts\activate.bat

Depois, abra no navegador: http://127.0.0.1:5000/

## Instalação no Ubuntu / Linux

Abra o terminal na pasta do projeto e execute:


python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py


Se a criação do ambiente virtual apresentar um erro informando que o módulo `venv` não está disponível, instale-o com:


sudo apt update
sudo apt install python3-venv


Depois, execute novamente o comando de criação do ambiente virtual.

Se o terminal mostrar que o servidor está rodando, abra no navegador:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Estrutura
- `app.py`: servidor Python/Flask e rota principal `/`
- `templates/index.html`: conteúdo HTML da página
- `static/style.css`: estilos visuais
- `requirements.txt`: dependências do projeto