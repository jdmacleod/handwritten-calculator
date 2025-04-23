# Handwritten Calculator Demo - Front End Web App

A Python Flask web app that recognizes handwritten numbers and symbols, can predict simple integer expression results, and can capture handwritten arithmetic symbols as images for training. Part of the handwritten-calculator ensemble.

## Quick Start

### Set Up Python3 Virtual Environment

```bash
cd demo/frontend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

### Run Flask Web App (local host only)

```bash
source development.env
flask run
```

#### Run Flask Web App (make available to local network)

```bash
flask run --host=0.0.0.0
```

### Connect to Web App

Point a web browser to the URL reported by flask - likely either <http://localhost:5000> or a local network IP address like <http:192.168.1.19:5000>

## Docker

docker build --tag hwcalc-frontend .

docker run --name hwcalc-frontend-demo -p 8000:5000 hwcalc-frontend

## Acknowledgements

Extends the <https://github.com/TalhaQuddoos/digit-recognizer-tensorflow-flask> example from [Talha Quddoos](https://github.com/TalhaQuddoos).
