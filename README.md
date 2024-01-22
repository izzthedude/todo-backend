# todo-django

The backend for my Todo app project using the Python
[Django](https://www.djangoproject.com/) framework.

## Development Setup

### Requirements

- Python >= 3.12 (Might work in lower versions, haven't tested)
- Docker/Podman

### Steps

***Note: For deploying only, steps 2 and 3 can be skipped.***

1. Clone this branch

```bash
git clone -b python/django https://github.com/izzthedude/todo-backend.git
```

2. Create virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -e .[dev]
```

4. Build and run with docker/podman

```bash
docker compose up --build -d
```

## License
This project is licensed under **GPL-3.0**, see the [LICENSE](LICENSE) for more details.
