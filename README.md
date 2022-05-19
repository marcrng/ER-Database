# 1 | Introduction
Elden Ring is an Action-Adventure video game that utilizes an items based system to alter the player's character statistics. 

The focus on this project will be practicing cleaning data with a large amount of errors while using the `BeautifulSoup` Python library that allows us to pull data from HTML and XML sites.

_This work and the usage of the data within this work will not be used to create profit._

# 2 | Goals
- Create an interactive dashboard, allowing easy lookup and visualization of Elden Ring weapon data.
- Practice cleaning data containing errors commonly found in real-life datasets using SQL and Python
- Try using data scraping tools to create a database from scratch and build an accurate dashboard from this data

# 3 | Process
## 3.1 | Data Collection
### Creating a Pandas dataframe using BeautifulSoup

#### Importing Libraries
First, we need to import the libraries we'll be using to first download the HTML webpage, then parse it so we can pull the data that we're looking for from the raw HTML

```python
import requests                 # Allows us to download the raw HTML from a website 
from bs4 import BeautifulSoup   # Allows us to parse and pull specific data from the raw HTML
import pandas as pd             # Allows us to place the extracted data into a Pandas dataframe
import re                       # Allows us to use regular expressions (regex) to manipulate strings 
```

#### Downloading the raw HTML
With the necessary libraries imported, we can start building our get request to pull the raw HTML of the entire page to start off
```python
URL = "https://eldenring.wiki.fextralife.com/Axes"  # Insert the URL into a variable for cleaner code
page = requests.get(URL)    # Begins the request to download the HTML from the website

print(page.status_code)    # Returns the HTTP status code returned by the link. ([200] = success, [404] = page not found)
print(page.content)    # Prints out the raw HTML returned by the request
```


Here are the first few lines of HTML returned by `page.content`. Definitely needs to be cleaned up to be useful.
```python
# Output of print(page.content)

"""
> b'\n\n\n\n\n<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta 
> http-equiv="X-UA-Compatible" content="IE=edge">\n\t\t<meta name="viewport" 
> content="width=device-width, initial-scale=1">\n\t\t\n\t\t<meta name="description" 
> content="Elden Ring Axes Guide: Complete list of all Axes, where to find them, stats, 
> defenses, requirements and upgrades." />\n\t\t<meta name="msvalidate.01" 
> content="663178F9F25C3ED57D64CFF2E5B7FFAA" />\n\t\t<meta name="google-site-verification" 
> content="bQqyY4AeKKKWxUQrr34-kgQNWyCx7DtDJ3nbKkYZrag" />\t\t\n\t\t<meta 
"""

```


#### Parsing the downloaded HTML
With the HTML fetched, we can now create a BeautifulSoup object with it called `bs_page`. We can use a few functions on this object like using `find()` to return the text within a given field. 

For now, we're going to use `prettify()` to view the formatted HTML

```python
bs_page = BeautifulSoup(page.content, "html.parser")    # Parse the HTML using BeautifulSoup

print(bs_page.prettify())    # Prints a formatted version of the HTML
```

Here's the first few lines of the output of `print(bs_page.prettify())`. Much easier to identify what the content of each tag is.
```python
# Output of print(bs_page.prettify())

"""
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <meta content="Elden Ring Axes Guide: Complete list of all Axes, where to find them, stats, defenses, requirements and upgrades." name="description">
   <meta content="663178F9F25C3ED57D64CFF2E5B7FFAA" name="msvalidate.01">
    <meta content="bQqyY4AeKKKWxUQrr34-kgQNWyCx7DtDJ3nbKkYZrag" name="google-site-verification"/>
    <meta content="BkHcHuN8mXWUPZ0QBrK4fTUij37eEjGHixZPyEbkZdg" name="google-site-verification"/>
    <link href="https://eldenring.wiki.fextralife.com/Axes" rel="canonical"/>
    <title>
     Axes | Elden Ring Wiki
    </title>
"""
```

#### Extracting the data we need from the HTML


## 3.x| Correlation Matrix
#### Version One
![Melee Correlation Matrix 1](./Visualizations/CorrMatrix1.png)
#### Version Two
![Melee Correlation Matrix 1](./Visualizations/CorrMatrix2.png)
# 4 | Requested Improvements
# 5 | Things to Improve
- Could have automated page fetching using a list and iterating through it
# 6 | Credits
# Special Thanks
Items Data from [Fextralife](https://fextralife.com/)

<a href="https://www.flaticon.com/free-icons/sword" title="sword icons">Sword icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/axe" title="axe icons">Axe icons created by Those Icons - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/crossbow" title="crossbow icons">Crossbow icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/crossbow" title="crossbow icons">Crossbow icons created by Zlatko Najdenovski - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/bow" title="bow icons">Bow icons created by Those Icons - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/hand" title="hand icons">Hand icons created by berkahicon - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/club" title="club icons">Club icons created by Smashicons - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/sabre" title="Sabre icons">Sabre icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/knight" title="knight icons">Knight icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/fist" title="fist icons">Fist icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/flail" title="flail icons">Flail icons created by surang - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/axe" title="axe icons">Axe icons created by Dreamstale - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/artemis" title="artemis icons">Artemis icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/spear" title="spear icons">Spear icons created by iconixar - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/miscellaneous" title="miscellaneous icons">Miscellaneous icons created by Muhammad Ali - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/sword" title="sword icons">Sword icons created by pongsakornRed - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/halberd" title="halberd icons">Halberd icons created by PIXARTIST - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/hammer" title="hammer icons">Hammer icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/sword" title="sword icons">Sword icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/ninja" title="ninja icons">Ninja icons created by Handicon - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/bow" title="bow icons">Bow icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/scythe" title="scythe icons">Scythe icons created by Icongeek26 - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/talisman" title="talisman icons">Talisman icons created by photo3idea_studio - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/shield" title="shield icons">Shield icons created by Good Ware - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/magic" title="magic icons">Magic icons created by David Carapinha - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/sword" title="sword icons">Sword icons created by Nikita Golubev - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/fight" title="fight icons">Fight icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/torch" title="torch icons">Torch icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/foil" title="foil icons">Foil icons created by Handicon - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/thor" title="thor icons">Thor icons created by Freepik - Flaticon</a>

<a href="https://www.flaticon.com/free-icons/whip" title="whip icons">Whip icons created by Freepik - Flaticon</a>
