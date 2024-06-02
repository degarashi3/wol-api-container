from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

@app.get("/")
def read_items(macaddr: str):
    command = 'sudo etherwake -i wlan0 ' + macaddr
    ret = subprocess.run(command, shell=True)
    return {'send magic packet to ': macaddr}
