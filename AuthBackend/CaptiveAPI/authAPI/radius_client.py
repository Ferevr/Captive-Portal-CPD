from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest, AccessAccept
import os, logging
import traceback

def authenticate_with_radius(username, password):
    try:
        print(f"intentando autenticar con usuario: {username}, password: {password}")
        dict_path = os.path.join(os.path.dirname(__file__), "dictionary")
        client = Client(
            server="127.0.0.1",        # IP de tu servidor RADIUS
            secret=b"test1234",           # Clave compartida (coincide con FreeRADIUS)
            dict=Dictionary(dict_path)
        )
        client.AuthPort = 1812
        req = client.CreateAuthPacket(code=AccessRequest, User_Name=username)
        req["User-Password"] = req.PwCrypt(password)
        reply = client.SendPacket(req)

        print(f"codigo de respuesta RADIUS: {reply.code}")

        if reply.code == AccessAccept:
            print("Autenticación exitosa")
            return True
        else:
            print("Autenticación fallida")
            return False

    except Exception as e:
        print(f"RADIUS error: {e}")
        traceback.print_exc()
        return False