from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Remember to install OpenPyXL and Pillow, pip install openpyxl pillow

wb = Workbook()
ws = wb.active

img = Image("coffee.png")
ws.add_image(img, "A2")

wb.save("coffee.xlsx")
