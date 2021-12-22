import numpy as np
from PIL import Image as im
import PIL.ImageOps


class PNGReader:
    def __init__(self, read_path: str):
        # Image data
        self.img = im.open(read_path, 'r')  # Throws FileNotFoundError
        self.array = np.array(list(self.img.getdata()))

        # Image specifications
        self.width, self.height = self.img.size
        self.mode = self.img.mode
        self.n = {'RGB': 3, 'RGBA': 4}[self.img.mode]  # Throws KeyError
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


class MessageReader:
    def __init__(self):
        self.message = self.translate()

    def translate(self) -> str:
        pass

    def get_message(self) -> str:
        return self.message


class StringReader(MessageReader):
    def __init__(self, text: str):
        self.text = text
        MessageReader.__init__(self)

    def translate(self) -> str:
        return ''.join([format(ord(i), "08b") for i in self.text])

    def get_text(self) -> str:
        return self.text

    def get_message(self) -> str:
        return self.message


class FileReader(MessageReader):
    def __init__(self, file_path: str):
        self.file = open(file_path, 'rb')
        MessageReader.__init__(self)
        print(self.message)

    def translate(self) -> np:
        return np.fromfile(self.file, np.dtype('B'))


# TODO: Remove for production use
if __name__ == "__main__":
    image = im.open('../resources/test_shape.png')
    PIL.ImageOps.invert(image).save('../resources/test_shape.png', "PNG")
