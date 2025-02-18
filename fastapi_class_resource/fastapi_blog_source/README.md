# isbd_web_dev_batch_6

## Getting started

It's a blog application where user authentication & authorization is added.
We use **fastapi** for building our apis and **postgresql** as our database.

## Project setup

- Create a virtualenv
- Activate it
- Run `docker compose up --build` for postgresql database up & running
- Create a `.env` file and put the environment variables with values as shown in **.example.env**
- Run `alembic upgrade head` for the database migration
- Run `uvicorn main:app --reload port 8010` for starting the server with the autoreload and port mapping
