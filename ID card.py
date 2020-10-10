from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)
import random
import datetime
import qrcode

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")

print (reg_format_date)


print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)



(x, y) = (600, 75)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)


(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name=message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)





 
image.save(str(name)+'.png')



img = qrcode.make(str(company)+str(idno))   
img.save(str(idno)+'.bmp')


til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp') #25x25
til.paste(im,(600,350))
til.save(name+'.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))

eval(input('\n\nPress any key to Close program...'))
