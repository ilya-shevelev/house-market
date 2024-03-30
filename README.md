# HOUSE MARKET
#### Многофункциональная платформа для покупки и аренды недвижимости с внутренней социальной сетью и риэлторскими услугами.

## Quick start
1. Rename env.example to .env
2. Build and run docker containers:


    docker compose up -d --build
3. Apply database migrations:


    docker exec web alembic upgrade head
4. Go to [API page](http://localhost:8000/docs)

## For development
1. Prepare virtual environment with poetry:


    poetry install
    poetry shell
*[How to install Poetry](https://python-poetry.org/docs/#installation)*
2. Install Pre-commit:


    pre-commit install

Run pre-commit without commit:

    pre-commit run --all-files
