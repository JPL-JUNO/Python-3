import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d"))

from PIL import Image
img = Image.open('spiro-19Aug2023-231301' + '.eps')
img.save('spiro-19Aug2023-231301' + ".png", "png")
