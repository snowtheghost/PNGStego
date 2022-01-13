import numpy as np
from PIL import Image as im


class PNGEncoder:
    def __init__(self, array: np, data: dict, message: str):
        self.array = array
        self.data = data
        self.message = message

    def encode(self) -> None:
        # TODO: Check if there is sufficient capacity for the message
        i = 0
        for p in range(self.data['capacity']):
            for q in range(0, 3):
                if i < len(self.message):
                    # TODO: Allow for selection of bits
                    self.array[p][q] = int(self.message[i:i+8], 2)
                    i += 8

    def encode_except(self, colors: list) -> None:
        # TODO: Check if there is sufficient capacity for the message
        i = 0
        for p in range(self.data['capacity']):
            for q in range(0, 3):
                if i < len(self.message) \
                        and (self.array[p][0] != colors[0]
                             or self.array[p][1] != colors[1]
                             or self.array[p][2] != colors[2]):
                    # TODO: Allow for selection of bits
                    self.array[p][q] = int(self.message[i:i+8], 2)
                    i += 8

    def encode_file_except(self, colors: list) -> None:
        # TODO: Check if there is sufficient capacity for the message
        i = 0
        for p in range(self.data['capacity']):
            for q in range(0, 3):
                if i < len(self.message) \
                        and (self.array[p][0] != colors[0]
                             or self.array[p][1] != colors[1]
                             or self.array[p][2] != colors[2]):
                    # TODO: Allow for selection of bits
                    self.array[p][q] = self.message[i]
                    i += 1

    def get_array(self):
        return self.array


# TODO: Remove for production use
if __name__ == "__main__":
    pass
