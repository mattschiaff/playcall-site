from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];a=r/'dist/assets'
icon=Image.open(a/'app-icon.png').convert('RGB')
for size,name in [(64,'favicon.png'),(180,'apple-touch-icon.png')]:icon.resize((size,size),Image.Resampling.LANCZOS).save(a/name)
im=Image.new('RGB',(1200,630),'#090b0e');d=ImageDraw.Draw(im)
logo=Image.open(a/'wordmark.png').convert('RGBA');logo.thumbnail((360,60),Image.Resampling.LANCZOS);im.paste(logo,(64,54),logo)
font=lambda size:ImageFont.truetype(str(a/'fonts/BarlowCondensed-Bold.ttf'),size)
body=lambda size:ImageFont.truetype(str(a/'fonts/Barlow-Regular.ttf'),size)
d.text((64,155),'Your game.',font=font(103),fill='#f2f1ec');d.text((64,260),'Your calls.',font=font(103),fill='#ff781f')
d.text((68,411),'Live coach-to-catcher communication.',font=body(26),fill='#b6bcc1');d.text((68,510),'COMING TO iPHONE',font=body(22),fill='#ff781f')
screen=Image.open(a/'screenshots/ready.png').convert('RGB');screen.thumbnail((246,492),Image.Resampling.LANCZOS)
x,y=844,60;d.rounded_rectangle((x-9,y-9,x+screen.width+9,y+screen.height+9),radius=29,fill='#20262c',outline='#40464d',width=2)
mask=Image.new('L',screen.size);ImageDraw.Draw(mask).rounded_rectangle((0,0,screen.width,screen.height),radius=20,fill=255);im.paste(screen,(x,y),mask)
im.save(a/'social-preview.png')
print('Generated favicon/touch icon and 1200x630 social preview from authentic brand/UI assets')
