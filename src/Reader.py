import numpy as np
from PIL import Image as im


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
    image = im.open('../resources/test_shape.png').convert('RGBA')
    new_image = im.new("RGBA", image.size, "WHITE")  # Create a white rgba background
    new_image.paste(image, (0, 0), image)  # Paste the image on the background. Go to the links given below for details.
    new_image.convert('RGB').save('../resources/test_shape.png', "PNG")
