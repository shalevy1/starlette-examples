# Starlette Example Projects

A few example projects using the light weight ASGI framework [Starlette](https://www.starlette.io/). These are just small projects built for learning purposes.

## Projects

1. `project_example` - A full project layout with some test API endpoints. Goal was to figure out what a good project structure might look like with Starlette. Took a lot of inspiration from how I structure Flask projects.
2. `db_example` - Wanted to see how I could use SQLAlchemy with Starlette. The project just uses a simple SQLite db. Basically just a simple API for getting and creating users with a simple schema. I've used the [databases](https://github.com/encode/databases) module to run async database queries too.
3. `bg_tasks` - Wanted to checkout how the async background tasks work in Starlette. The simple example just posts an email address to an API endpoint and then Starlette run a background task that saves the eamil to a csv file.

All projects run with [uvicorn](https://github.com/encode/uvicorn)!

## Installation

1. Clone the repo
2. Create a virtual environment (however you like)
3. Pip install the requirements from `requirements.txt`
