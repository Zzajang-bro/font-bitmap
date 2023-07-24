import subprocess
subprocess.run(['pip','install','pillow'], capture_output=True)

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('neodgm.ttf', 12)

def saveOnFile( ch ):
  im = Image.new(mode="RGB", size=(100,100))
  dr = ImageDraw.Draw(im)
  dr.text((0,0), ch, (0,0,0), font=font)
  img.save(f'{ch}.png')
