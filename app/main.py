from fastapi import FastAPI
from pydantic import BaseModel
from wakeonlan import send_magic_packet

app = FastAPI()

@app.get("/")
def read_items(macaddr: str):
    send_magic_packet(macaddr)
    return {'send magic packet to ': macaddr}
