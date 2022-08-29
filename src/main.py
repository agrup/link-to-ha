from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/toggle-alarm")
def read_root(key: str ):

    try:
        url = "http://agrup.tplinkdns.com:8123/api/services/script/alarma_toggle_alarm"
        token = key
        payload = {}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.json())
        return {"status": response.status_code, "alarm":response.json()[0].get('state')}
    except Exception as error:
        return {"Error": error}

@app.get("/hello")
def hello():
    try:
        return {"Hello": "world!"}

    except Exception as error:
        return {"Error": error}        