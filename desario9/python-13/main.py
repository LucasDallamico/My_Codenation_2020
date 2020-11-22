# .travis.yml
config = """
language: python
python:
  -"2.7"
  -"3.7"
  -"pypy"
  -"pypy3"
pypy: 
    -"7.1.1"
    -"7.1.1-beta0"
script: 'pytest'
install: "pip install -r requirements.txt"
"""