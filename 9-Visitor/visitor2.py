from abc import ABC, abstractmethod

# Visitor Interface
class FileOperation(ABC):
    @abstractmethod
    def visit_text(self, file: "TextFile"):
        pass

    @abstractmethod
    def visit_image(self, file: "ImageFile"):
        pass

    @abstractmethod
    def visit_video(self, file: "VideoFile"):
        pass


# Concrete Visitor 1: Virus Scanner
class VirusScanner(FileOperation):
    def visit_text(self, file: "TextFile"):
        print(f"Scanning text file: {file.name} for viruses...")

    def visit_image(self, file: "ImageFile"):
        print(f"Scanning image file: {file.name} for viruses...")

    def visit_video(self, file: "VideoFile"):
        print(f"Scanning video file: {file.name} for viruses...")


# Concrete Visitor 2: Compression
class Compression(FileOperation):
    def visit_text(self, file: "TextFile"):
        print(f"Compressing text file: {file.name}")

    def visit_image(self, file: "ImageFile"):
        print(f"Compressing image file: {file.name}")

    def visit_video(self, file: "VideoFile"):
        print(f"Compressing video file: {file.name}")


# Element Interface
class File(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def accept(self, operation: FileOperation):
        pass


# Concrete Elements: Different File Types
class TextFile(File):
    def accept(self, operation: FileOperation):
        operation.visit_text(self)


class ImageFile(File):
    def accept(self, operation: FileOperation):
        operation.visit_image(self)


class VideoFile(File):
    def accept(self, operation: FileOperation):
        operation.visit_video(self)


# Client Code
if __name__ == "__main__":
    files = [
        TextFile("document.txt"),
        ImageFile("photo.png"),
        VideoFile("movie.mp4")
    ]

    scanner = VirusScanner()
    compressor = Compression()

    print("Running Virus Scan:")
    for file in files:
        file.accept(scanner)

    print("\nRunning Compression:")
    for file in files:
        file.accept(compressor)
