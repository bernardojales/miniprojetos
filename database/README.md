## Why should i learn
- It is a flexible way of store data
- An important knowledge to complement the tool kit when developing backend applications

## Initial steps

- run mongodb service with docker compose
```sh
docker compose up -d mongo # setup mongodb
```
- [setup virtual environment](https://docs.google.com/document/d/1QI9jc3wl92B6KOrpgS-xi9OnOO1kkAm6g4pHx42Mwsk/edit#heading=h.v74wpoyxy3z)
- install dependencies
```sh
pip install -r requirements.txt
```
- there is a [python script](./server.py) that interacts with mongodb using pymongo lib