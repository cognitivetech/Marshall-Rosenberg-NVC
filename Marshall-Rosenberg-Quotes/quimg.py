# Print Quotes on Images
# Adapted from: https://muthu.co/instagram-quotes-generator-using-python-pil/

# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os, random, yaml

#variables for image size
x1 = 1900
y1 = 950

#choose a font OpenSansHebrew-BoldItalic.ttf
fnt = ImageFont.truetype('et-book-bold-line-figures.ttf', 69)

with open('quotes.yaml','r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    quotes = yaml.load(file, Loader=yaml.FullLoader)
    file.close()

acc = 0

for quote in quotes:
  acc += 1
  dir = 'imgs'
  rand = ''
  rand = random.choice(os.listdir(dir))
  randimg = dir + rand
  imgg = Image.open(randimg)
  img = imgg.convert('RGB')
  d = ImageDraw.Draw(img)

  #find the average size of the letter
  sum = 0
  for letter in quote:
    sum += d.textsize(letter, font=fnt)[0]
  
  average_length_of_letter = sum/len(quote)
  
  #find the number of letters to be put on each line
  number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
  incrementer = 0
  fresh_sentence = ''
  
  #add some line breaks
  for letter in quote:
    if(incrementer < number_of_letters_for_each_line):
      fresh_sentence += letter
    else:
      if(letter == ' '):
        fresh_sentence += '\n'
        incrementer = 0
      else:
        fresh_sentence += letter
    incrementer+=1
  fresh_sentence += '\n\n- Marshall B. Rosenberg'
  print fresh_sentence
  
  #render the text in the center of the box
  dim = d.textsize(fresh_sentence, font=fnt)
  x2 = dim[0]
  y2 = dim[1]
  
  qx = (x1/2 - x2/2)
  qy = (y1/2-y2/2)
  
  d.text((qx,qy), fresh_sentence,align="center",  font=fnt, fill=(0,0,0))
  ac = str(acc)
  filename = "imgs/MBRQuote" + ac + "-" + rand
  img.save(filename)

