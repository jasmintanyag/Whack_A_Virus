from PIL import Image

class ImageHandler:
    @staticmethod
    def resize_image(image_path, resized_path, size=(57, 70)):
        with Image.open(image_path) as img:
            img = img.resize(size)
            img.save(resized_path, format='GIF')