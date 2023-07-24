from PIL import Image, ImageDraw, ImageFont, ImageChops

font = ImageFont.truetype('DungGeunMo.ttf', 16)

def saveOnFile( im, nm ):
  im.save(f'{nm}.png')

def image( ch ):
  im = Image.new(mode='RGBA', size=(100,100))
  dr = ImageDraw.Draw(im, 'RGBA')
  dr.rectangle((0,0,100,100),fill=(255,255,255,0))
  dr.text((0,0), ch, (0,0,0), font=font)
  return im

def multi( im1, im2 ):
  im3 = ImageChops.multiply(im1, im2)
