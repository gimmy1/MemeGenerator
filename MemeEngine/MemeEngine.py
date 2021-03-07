import os
import random
import uuid

from PIL import Image, ImageDraw, ImageFont
from PIL import UnidentifiedImageError

class MemeEngine:
    """ A class to create meme. """
    # class attribute
    allowed_extensions = ".jpg"

    def __init__(self, directory="."):
        """ Create meme to the output folder"""
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.image = None

    def load(self, image):
        if image.endswith(self.allowed_extensions):
            return Image.open(image)
        raise UnidentifiedImageError("Unsupported FileType")

    def resize_image(self, max_width=500):
        """
        Proportionally resize the image
        """
        if max_width > 500:
            max_width = 500
        
        width, height = self.image.size
        ratio = max_width / float(width)
        adjusted_height = int(height * ratio)
        return self.image.thumbnail((adjusted_height, width))

    @staticmethod
    def create_filename(directory):
        """
        Saves pillow image in the output_dir attribute.
        """
        return f"{directory}/{uuid.uuid4()}.jpg"

    def add_quote(self, body, author):
        """
        Add a quote to the image as text
        """
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("./_data/comicate/COMICATE.TTF", 30)
        draw.text((50, 50), f"* {body} *", font=font, fill="black")
        draw.text((55, 30), f"Author: {author}", font=font, fill="white")

    def make_meme(self, image, body, author, width=500):
        """
        Create meme and save into path
        """
        ouput_file_path = self.create_filename(self.directory)
        self.image = self.load(image)
        self.resize_image(width)
        self.add_quote(body, author)
        self.image.save(ouput_file_path, "JPEG")
        return ouput_file_path