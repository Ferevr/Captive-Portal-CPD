from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest, AccessAccept
import os, logging

def authenticate_with_radius(username, password):
    try:
        dict_path = os.path.join(os.path.dirname(__file__), "dictionary")
        client = Client(
            server="10.18.245.10",        # IP de tu servidor RADIUS
            secret=b"test1234",           # Clave compartida (coincide con FreeRADIUS)
            dict=Dictionary(dict_path)
        )
        client.AuthPort = 1812
        req = client.CreateAuthPacket(code=AccessRequest, User_Name=username)
        req["User-Password"] = req.PwCrypt(password)
        reply = client.SendPacket(req)

        return reply.code == AccessAccept
    except Exception as e:
        logging.error(f"RADIUS error: {e}")
        return False