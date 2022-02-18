from PIL import Image
import thermalprinter

with thermalprinter(port='/dev/ttyAMA0') as printer:
    printer.image(Image.open('home.png'))
    printer.feed(2)