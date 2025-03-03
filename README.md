# README.md (Project Documentation)
# Wikipedia Word-Frequency Dictionary
## Setup
```sh
pip install -r requirements.txt
python app.py
```
## API Usage
### GET /word-frequency
```sh
curl "http://127.0.0.1:5000/word-frequency?article=Python_(programming_language)&depth=2"
```
### POST /keywords
```sh
curl -X POST "http://127.0.0.1:5000/keywords" -H "Content-Type: application/json" -d '{"article": "Python_(programming_language)", "depth": 2, "ignore_list": ["the", "is"], "percentile": 80}'
