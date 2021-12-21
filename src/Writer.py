import numpy as np
from PIL import Image as im


class PNGWriter:
    # TODO: Remove path default value for production use
    def __init__(self, array: np, data: dict, write_path: str = '../resources/test_output.png'):
        self.array = array  # Array obtained from PNGEncoder
        self.data = data  # Data obtained from PNGReader
        self.write_path = write_path

    def write(self):
        self.array = self.array.reshape(self.data['height'], self.data['width'], self.data['n'])
        im.fromarray(self.array.astype('uint8'), self.data['mode']).save(self.write_path)


# TODO: Remove for production use
if __name__ == "__main__":
    pass
