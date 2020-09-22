# Marshall Rosenberg Quotes

As time goes on I'll be adding all the links from this repository into the quotes queue, and make sure this account can stay fresh for a long time. This message is too valuable for it to not be shared. 

## Quote-Bots

I made these to demonstrate autoposting to twitter using [GitHub Actions](https://docs.github.com/en/actions/guides/building-and-testing-python).

#### Quote Bot (text)

The twitter quote bots were adapted the script found in [this guide](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/). I saved the secrets for the Marshall Rosenberg Quotes account as [encrypted environment variables](https://docs.github.com/en/actions/reference/encrypted-secrets) saved in this repository, which are pulled into a bash shell as part of the action, and then called into the python script. If you copy this code, you'll need to set your own.

Using the GitHub Action workflow file [.github/workflows/quote.yml](/.github/workflows/quote.yml), this quotes.py runs every 5 hours at the 33rd minute:

```yaml
    - cron:  '33 */5 * * *'
```

[Workflow Scheduler/Cron Syntax](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events)

[quotes.py](Marshall-Rosenberg-Quotes/quotebot/quotes.py) pulls a random quote from [/Marshall-Rosenberg-Quotes/quotebot/quotes.yaml](/Marshall-Rosenberg-Quotes/quotebot/quotes.yaml) and sends it as a status update to [@MarshallRsnberg](https://twitter.com/marshallrsnberg) the Marshall Rosenberg Quotes twitter account.

#### Quimg Bot

I printed [quotes](/Marshall-Rosenberg-Quotes/quotes.yaml) onto [images](/Marshall-Rosenberg-Quotes/imgs/) using [quimg.py](Marshall-Rosenberg-Quotes/quimg.py).

[.github/workflows/quimg.yml](/.github/workflows/quimg.yml) sends an image quote status update every 9 hours at the 11th minute.

```yaml
    - cron:  '11 */9 * * *'
```

## Cropping Tools

Aspect Ratio Calculator:

https://andrew.hedges.name/experiments/aspect_ratio/

Need Imagemagick for all this stuff:

https://imagemagick.org/index.php

### crop all in directory

http://www.fmwconcepts.com/imagemagick/aspectcrop/index.php

```bash
for f in * ;
./aspectcrop -a 1920:1080 $f cropped.$f
```

### Using Convert 
Aspectcrop only crops proportionally, if you want exact dimensions cropped, use convert.

```bash
for f in * ;   
convert $f -crop 1080x1080+0+0 -gravity center insta.$f
```

## Optimization
### Reduce size of jpg in place

https://stackoverflow.com/questions/50985087/how-to-reduce-the-file-size-on-jpeg-images-in-batch-mac

```bash
mogrify -define jpeg:extent=300kb *.jpg
```

### PngQuant

https://pngquant.org/

---

With Love