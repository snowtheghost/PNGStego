import numpy as np
from PIL import Image as im


class PNGDecoder:
    def __init__(self, array: np, data: dict):
        self.array = array
        self.data = data

    # TODO: Identify output type
    def decode(self):
        message = ""
        for p in range(self.data['capacity']):
            for q in range(0, 3):
                # TODO: Allow for selection of bits
                message += (format(self.array[p][q], '#010b')[2:])

        message_bytes = [message[i:i+8] for i in range(0, len(message), 8)]
        text = ""
        for i in range(len(message_bytes)):
            if message_bytes[i] != '11111111':  # Assumes that text never uses 255
                text += chr(int(message_bytes[i], 2))
        print(text)
