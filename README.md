# [Stachebot](https://github.com/WildSiphon/Stachebot)
[![Twitter](https://img.shields.io/twitter/url?label=RealStachBot&style=social&url=https%3A%2F%2Ftwitter.com%2FRealStachBot)](https://twitter.com/RealStachBot) [![GitHub license](https://img.shields.io/github/license/WildSiphon/Mustachizer)](https://github.com/WildSiphon/Mustachizer/blob/main/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p)

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png" alt="bulb" style="zoom:33%;" /> The Idea

The idea behind his project was to propose a solution to **mustachize as many faces as possible**. So we did it!
And because it's funny and we like to share, we made it a twitter bot ([@RealStachBot](https://twitter.com/RealStachBot)) and a discord bot.

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f6e0.png" alt="hammer_and_wrench" style="zoom:33%;" /> Installation

If you want to use our work locally, just follow instructions below :

### Using `pip` requirements

```bash
$ git clone https://github.com/WildSiphon/Mustachizer.git
$ cd Mustachizer
$ pip install -r requirements/mustachizer.txt
```

*Change the file name based on your usage. Choose between `mustachizer.txt`, `twitter_bot.txt` or `discord_bot.txt`*

### Using `Pipenv`

```bash
$ git clone https://github.com/WildSiphon/Mustachizer.git
$ cd Mustachizer
$ pipenv shell
```

### Using `docker`

Just kidding, we haven't gone that far.

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4c8.png" alt="chart_with_upwards_trend" style="zoom:33%;" />Use

### Local use

If you want to mustachize your pictures by yourself, simply run `mustachizer.py` :

```bash
$ python3 mustachizer.py --show "FILE"
```

**Options available**

```
usage: mustachizer.py [-h] [--list-mustaches] [--size {realist,big,massive}] [--type [NAME]] [--show] [--list-formats] [--no-banner] [--output [DIRPATH]] [--log {CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET}]
                      [FILES [FILES ...]]

MUSTACHE THE WORLD!! Script to mustachize everything... or almost

positional arguments:
  FILES                 path(s) to the file(s)

optional arguments:
  -h, --help            show this help message and exit

Mustaches parameters:

  --list-mustaches      list all the mustaches types
  --size {realist,big,massive}
                        choose size of the mustache (default is "realist")
  --type [NAME]         choose mustache type (default is "RANDOM")

Settings:

  --show                display the mustachized media(s)
  --list-formats        list all the accepted media formats
  --no-banner           doesn't display banner
  --output [DIRPATH]    choose output location (default is "output/")
  --log {CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET}
                        choose logging level (default is "INFO")

Mustaches names: BAMBINO, CAPTAIN_HOOK, DOCTOR_WATSON, EDWARDIAN, FANCY_CURL, HANDLEBAR, HERCULE_POIROT, HULK_HOGAN, KAISER_WILHELM, REVERSE_HANDLEBAR, ROLLIE_FINGERS, SALVADOR_DALI, TRYPHON_TOURNESOL,
WRESTLER

```

**Mustaches available**

![collection](assets/documentation/collection.png)

**Demo**

Mustachization of a photo!![demo](assets/documentation/demo_photo.gif)

Mustachization of a gif!![demo](assets/documentation/demo_gif.gif)

### Twitter use

[@RealStachBot](https://twitter.com/RealStachBot) is already on twitter. If you want it to mustachize something, just tag it :

+ When you **post** a picture
+ In the **reply** of someone's picture

The bot doesn't mustachize when you tag it in a quote RT of a tweet with media.

You can publish your own bot based on our work if, and only if, ***it brings something different to Twitter***. Otherwise make a pull request.
If you publish your own bot based on our work, please ***link the project and our bot in the account description***.

### Discord use

We published the code for a discord bot but didn't make one public.
Feel free to use our project for personal use only, but ***don't make a public bot with it***.

### Developers use

Install dev requirements:
```bash
$ pip install -r requirements/dev.txt
```

Then install `pre-commit` in your git folder:
```
$ pre-commit install
```

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4da.png" alt="books" style="zoom:33%;" /> Code review

Now that all the script kiddies are trying to mustachize some stuff without reading more, we can talk about how the code works with y'all real mustache growers.

The first toward mustachization is to detect the face.
This is done with a [Cascade Classifier](https://docs.opencv.org/4.5.3/db/d28/tutorial_cascade_classifier.html) (depicted in red in the following image).

The goal is to eliminate the big chunks of the image which don't contain any face.

The selected part of the image is then passed through a [Local Binary Feature Facemarker](https://docs.opencv.org/3.4.15/javadoc/org/opencv/face/FacemarkLBF.html) which is essentially an AI specialised in putting reference points on a face.

You can see the result here :
![Before/After Detection](assets/documentation/before_after.jpg)

The facemarker outputs a lot of points which we ignore.

Our reference points are in blue on the picture.

We then map those points to a virtual face model using [Perspective N Points solving algorithm](https://shimat.github.io/opencvsharp_docs/html/64263f79-df37-20d6-0753-daf54d958ffe.htm).

It determines the rotation and translation of the face needed to match the two sets of points like shown in the following picture :

![PnP](https://docs.opencv.org/master/pnp.jpg)

Beside, we compute a rectangle on the plane parallel to the face.
This rectangle is the mustache's bounding box.

We can now use the rotation and translation of the face to determine the perspective transformation matrix to apply to put the flat mustache image into the said box.

We can see the result here :

<img src="assets/documentation/mustache_perspective.jpg" alt="Perspective process" style="zoom: 67%;" />

<img src="assets/documentation/mustachized_final_debug.jpg" alt="mustachized_final_debug" style="zoom:50%;" />

**Et voilà !**

You can now enjoy a pretty mustache !

![Final result](assets/documentation/mustachized_final.jpg)

### Design

#### Class diagram

![Class Diagram](assets/documentation/puml/out/class_diagram/class_diagram.svg)

## <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png" alt="memo" style="zoom:33%;" /> Stuff to add

+ ~~Creating `mustachizer.py` to mustachize locally~~
+ ~~Improve output of `mustachizer`~~
+ ~~Finish the README~~
+ ~~Comment all the code~~
+ ~~Implement gif support~~
+ Implement video support
+ ~~Add options to choose the size of the mustache~~
+ Implement unittest
+ Add twitter options to pass param (mustache name, size...)
+ Add mustache color management based on hair color
+ Adding more sentences when bot is posting result of mustachisation
+ MORE MUSTACHES (maybe not… but maybe more)

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
