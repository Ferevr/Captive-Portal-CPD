#Script to authenticate users with the RADIUS server
# made by ferevr ;)
# was not payed :C 

from pyrad.client import Client
from pyrad.dictionary import Dictionary
from pyrad.packet import AccessRequest, AccessAccept, AccessReject
import logging
import os

def authenticate_with_radius(username, password):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dictionary_path = os.path.join(base_dir, "dictionary")

    try:
        client = Client(
            server="10.18.245.10", #server route
            secret=b"test1234",     # shared key
            dict=Dictionary(dictionary_path)  # path to dictionary file
        )
        client.AuthPort = 1812  # default port

        req = client.CreateAuthPacket(code=AccessRequest, User_Name=username)
        req["User-Password"] = req.PwCrypt(password)

        reply = client.SendPacket(req)

        if reply.code == AccessAccept:
            print("Access granted")
            return True
        else:
            print("Access denied")
            return False
    except Exception as e:
        logging.error(f"RADIUS error: {e}")
        return False
    

#authenticate_with_radius("ferevr", "test1234")
