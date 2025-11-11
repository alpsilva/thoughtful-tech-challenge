# thoughtful-tech-challenge
This repo contains my submission for Thoughtful's AI Tech screening.

## Setup

### Pre-requisites
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (for dependency management and virtual environment)
- Python 3.13

### Install

1. cd into `package_sorter`:
```bash
cd package_sorter
```

2. Create a virtual python environment using uv:
```bash
uv venv
```

Activate the environment with:
```bash
source .venv/bin/activate
```

4. Install all necessary dependencies using uv:
```bash
uv sync
```

## Run
while inside `package_sorter` directory and using the virtual environment, simply run:
```bash
python3 main.py
```

You can change the values being inputted to `sort` at `main.py`

## Tests
while inside `package_sorter` directory and using the virtual environment, simply run:
```bash
pytest --cov=sorter 
```

To run all unit tests and see a code coverage report for `sorter.py`.