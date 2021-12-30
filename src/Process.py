from Reader import PNGReader, StringReader, FileReader
from Encoder import PNGEncoder
from Decoder import PNGDecoder
from Writer import PNGWriter


class Process:
    # TODO: User inputs for required fields
    def __init__(self):
        pass

    def encode(self):
        png_reader = PNGReader('../resources/HiddenFeelings000_ShapeObscured.png')
        # with open('../resources/text.txt', 'r') as file:
        #     text = file.read()
        file_reader = FileReader('../resources/HiddenFeelings000_Payload.mp3')
        png_encoder = PNGEncoder(png_reader.get_array(), png_reader.get_data(), file_reader.get_message())
        png_encoder.encode_file_except([0, 0, 0])
        png_writer = PNGWriter(png_encoder.get_array(), png_reader.get_data())
        png_writer.write()

    def decode(self):
        png_reader = PNGReader('../resources/test_output.png')
        png_decoder = PNGDecoder(png_reader.get_array(), png_reader.get_data())
        png_decoder.decode_file_except([0, 0, 0])  # TODO: More selective algorithm


if __name__ == "__main__":
    process = Process()
    process.encode()
    process.decode()
