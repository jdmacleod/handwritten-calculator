# Handwritten Calculator - Service Component

A Python Flask service that recognizes handwritten numbers and symbols. Part of the handwritten-calculator ensemble.

## Quick Start

### Set Up Python3 Virtual Environment

```bash
cd demo/backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

## Usage

```bash
source development.env
flask run
```

### Test Service Heartbeat Endpoint

Use [http://localhost:5001/heartbeat](http://localhost:5001/heartbeat) to check backend health.

## Docker

Build the image

```bash
docker build --tag hwcalc-backend .
```

Run the image in a container, connecting container port 5001 to external port 8001

```bash
docker run --name hwcalc-backend-demo -p 8001:5001 hwcalc-backend
```

## Acknowledgements

Extends the <https://www.toptal.com/data-science/machine-learning-number-recognition> example from [Teimur Gasanov](https://www.toptal.com/resume/teimur-gasanov).
