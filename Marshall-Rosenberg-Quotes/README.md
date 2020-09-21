# Quote Bots

## [Quote Bot](quotebot)

Sends text posts [to twitter](../.github/workflows/main.yml)

## Quote Images
### Print Quote on Images 

https://muthu.co/instagram-quotes-generator-using-python-pil/

[quimg.py](quimg.py) is based on the above link.

### Quimgbot

Based on [Quotebot](quotebot) which auto posts quotes \ images to twitter.

### Cropping Tools

Need Imagemagick for all this stuff:

https://imagemagick.org/index.php

#### crop all in directory

http://www.fmwconcepts.com/imagemagick/aspectcrop/index.php

```bash
for f in * ;
./aspectcrop -a 1920:1080 $f cropped.$f
```

#### Using Convert 
Aspectcrop only crops proportionally, if you want exact dimensions cropped, use convert.

```bash
for f in * ;   
convert $f -crop 1080x1080+0+0 -gravity center insta.$f
```

### Optimization

#### Reduce size of jpg in place

https://stackoverflow.com/questions/50985087/how-to-reduce-the-file-size-on-jpeg-images-in-batch-mac

```bash
mogrify -define jpeg:extent=300kb *.jpg
```

#### PngQuant

https://pngquant.org/