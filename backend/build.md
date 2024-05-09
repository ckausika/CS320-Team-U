## Build Instructions for Backend Virtual Environment Setup

```
  cd backend
  python -m venv .venv              # Create venv
  pip install -r requirements.txt   # Install python packages
```

### Running Flask Server

#### Windows

```
  cd backend
  .venv\Scripts\activate            # Enter venv
  flask --app app run               # Run Flask App
```

#### Mac OS / Linux

```
  cd backend
  source .venv/bin/activate         # Enter venv
  flask --app app run               # Run Flask App
```

### Running Tests
```
  pip install coverage              # Install python coverage
  coverage run -m unittest tests.py # Running Coverage
  coverage report -m                # View coverage report
  coverage html                     # View HTML version of coverage report
```
