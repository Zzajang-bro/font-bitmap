import subprocess
subprocess.run(['pip','install','pillow'], capture_output=True)

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('neodgm.ttf', 12)

def saveOnFile( ch ):
  im = Image.new(mode='RGBA', size=(100,100))
  dr = ImageDraw.Draw(im, 'RGBA')
  dr.rectangle((0,0,100,100),fill=(255,255,255,0))
  dr.text((0,0), ch, (0,0,0), font=font)
  im.save(f'{ch}.png')

ch = input('문자: ')
saveOnFile(ch)
