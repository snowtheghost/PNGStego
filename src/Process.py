from Reader import PNGReader, StringReader
from Encoder import PNGEncoder
from Writer import PNGWriter


class Process:
    # TODO: User inputs for required fields
    def __init__(self):
        pass

    def run(self):
        png_reader = PNGReader()
        with open('../resources/text.txt', 'r') as file:
            text = file.read().replace('\n', '')
        str_reader = StringReader(text)
        png_encoder = PNGEncoder(png_reader.get_array(), png_reader.get_data(), str_reader.get_message())
        png_encoder.encode()
        png_writer = PNGWriter(png_encoder.get_array(), png_reader.get_data())
        png_writer.write()


if __name__ == "__main__":
    process = Process()
    process.run()
