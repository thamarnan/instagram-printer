![](http://cdn.dnaindia.com/sites/default/files/styles/half/public/2016/05/12/459466-instagram-new-logo.jpg)
# Instagram Printer

Imagine you can setup the printer that can print out right from instagram when you tag it. This will be very useful at the party or event. I actually developed this one to use at one of the family party few years back.

Just need laptop or raspberry pi connected to printer.

![https://github.com/thamarnan/instagram-printer/blob/master/images/setup_laptop_printer.jpg?raw=true](https://github.com/thamarnan/instagram-printer/blob/master/images/setup_laptop_printer.jpg?raw=true "https://github.com/thamarnan/instagram-printer/blob/master/images/setup_laptop_printer.jpg?raw=true")

# How it works?
First you need to setup python to run on computer. In this case I'm using python 2.7 running on Windows.

(This code is dated, you might need to update the api and igURL)

The python code then login to instgram as your account.
It then freshed every few seconds to catch if there are any new picture that tagged with your specfic hashtag.

if it found the matched. It will printout to the printer replicating instagram on paper. Once printed, the picture is deleted.

| default_theme     |
| ---      |
| ![](https://github.com/thamarnan/instagram-printer/blob/master/images/default_theme.jpg?raw=true) |

# Requirements
What you will need are:
1. python 2.7 setup on computer
2. your instagram access token. You can follow [this](https://elfsight.com/blog/2016/05/how-to-get-instagram-access-token/ "this") instruction to get token

3. Update new token on the python code (printme.py)

````python

hashtag='kitty'
igurl = 'https://api.instagram.com/v1/tags/'+hashtag+'/media/recent?access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

````
Next step Set hashtag

Then Set Printer name (default_theme.cmd) last line

`rundll32    shimgvw.dll    ImageView_PrintTo /pt   %OUTPUT%.bmp  "Canon IP4500"`

and finally Run python printme.py

# Customization
| Customize Work Flow     |
| ---      |
| ![](https://github.com/thamarnan/instagram-printer/blob/master/images/printme_diagram.jpg?raw=true) |

When hashtag found in the image.
We can set the custom theme so that the picture print out in different template with secondary hashtag. For example,

I'm looking to print the hashtag "cat"
but if there is a secondary hashtag called "kitty"

I want to use hellokitty theme template.

To do this follow the step here:
1. new theme has prefix with the word 'theme' eg themekitty
2. create themekitty.cmd (example in this repository)
3. create folder call themekitty
4. set new background in the template_whitebackground.bmp

| themekitty     |
| ---      |
| ![](https://github.com/thamarnan/instagram-printer/blob/master/images/themekitty.jpg?raw=true) |

also included blank polariod theme in the example

| themepolaroid     |
| ---      |
| ![](https://github.com/thamarnan/instagram-printer/blob/master/images/themepolaroid.jpg?raw=true) |

Then virtually we have no limit on the variety
and have more fun with different pre define template

# Notes
Please check any update on instagram api on
https://www.instagram.com/developer/

