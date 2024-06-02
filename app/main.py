from fastapi import FastAPI
from pydantic import BaseModel
from wakeonlan import send_magic_packet
import subprocess

app = FastAPI()

@app.get("/")
def read_items(macaddr: str):
    ret = subprocess.run('sudo', 'etherwake', '-i', 'wlan0', macaddr)
    send_magic_packet(macaddr,interface='wlan0')
    return {'send magic packet to ': ret}
