import numpy as np
from PIL import Image as im


class PNGReader:
    # TODO: Remove path default value for production use
    def __init__(self, read_path: str = '../resources/test.png'):
        # Image data
        self.img = im.open(read_path, 'r')  # Throws FileNotFoundError
        self.array = np.array(list(self.img.getdata()))

        # Image specifications
        self.width, self.height = self.img.size
        self.mode = self.img.mode
        self.n = {'RGB': 3, 'RGBA': 4}[self.img.mode]
        self.pixels = self.array.size // self.n

    def get_data(self):
        return {'width': self.width,
                'height': self.height,
                'capacity': self.pixels,
                'mode': self.mode,
                'n': self.n}

    def get_img(self):
        return self.img

    def get_array(self):
        return self.array


class StringReader:
    def __init__(self, text: str):
        self.text = text
        self.message = self.translate()

    def translate(self) -> str:
        return ''.join([format(ord(i), "08b") for i in self.text])

    def get_text(self) -> str:
        return self.text

    def get_message(self) -> str:
        return self.message


# TODO: Remove for production use
if __name__ == "__main__":
    with open('../resources/text.txt', 'r') as file:
        text = file.read().replace('\n', '')
    str_reader = StringReader(text)
    print(str_reader.message)
    print(str_reader.text)
