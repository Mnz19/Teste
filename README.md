# Iniciando o Projeto Django

## Pré-requisitos

- Python 3.8 ou superior
- Django 3.2 ou superior
- Um ambiente virtual Python

## Passos para iniciar o projeto

1. **Crie um ambiente virtual**

  ```
    python -m venv venv
  ```

2. **Ative o ambiente virtual**

- No Mac/Linux:
  ```
  source venv/bin/activate
  ```

- No Windows:
  ```
  .\venv\Scripts\activate
  ```

3. **Instale as dependências**

  ```
    pip install -r requirements.txt
  ```

4. **Execute as migrações**
  ```
    python manage.py migrate
  ```

5. **Inicie o servidor**
  ```
    python manage.py runserver
  ```
