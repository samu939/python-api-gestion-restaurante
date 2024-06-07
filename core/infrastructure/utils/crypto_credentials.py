import json
from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from icecream import ic
from loguru import logger
from shared.core.config import AES_BLOCKSIZE, AES_KEY


class CryptoAES:
    @classmethod
    def encrypt(cls, data):
        cipher = AES.new(AES_KEY.encode("utf-8"), AES.MODE_ECB)
        encrypted = cipher.encrypt(pad(data.encode("utf-8"), AES_BLOCKSIZE))

        return b64encode(encrypted).decode("utf-8")

    @classmethod
    def decrypt(cls, data_encrypted):
        data = data_encrypted

        enc = b64decode(data)
        cipher = AES.new(AES_KEY.encode("utf-8"), AES.MODE_ECB)
        data = unpad(cipher.decrypt(enc), AES_BLOCKSIZE)
        return data.decode("utf-8")
