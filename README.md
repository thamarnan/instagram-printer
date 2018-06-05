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
| ![](https://github.com/thamarnan/instagram-printer/blob/master/images/default_theme.jpg?raw=true =300x450) |

# Requirements

# Customization

# Notes
