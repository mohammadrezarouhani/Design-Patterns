from abc import ABC, abstractmethod


class Compresor(ABC):
    @abstractmethod
    def compress(self, image):
        pass


class PngCompresor(Compresor):
    def compress(self, image):
        print('compressing to png')


class JpegCompressor(Compresor):
    def compress(self, image):
        print('compressing to Jpeg')


class Filter(ABC):
    @abstractmethod
    def apply(self, image):
        pass


class WbFilter(Filter):
    def apply(self, image):
        print('wb filter set on image')


class HighContrastFilter(Filter):
    def apply(self, image):
        print('High comress set on image')


class ImageStorage:
    def save(self, image, filtering: Filter, compressor: Compresor):
        compressor.compress(image)
        filtering.apply(image)
        print('image saved')


if __name__ == '__main__':
    storage = ImageStorage()
    storage.save('image file', HighContrastFilter(), PngCompresor())
