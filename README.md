#Python GUI project
This repo is aimed to test all the major Python libraries that build Graphic User Interface.

## Table of contents
- [Discuss the project](#discuss-the-project)
- [Prerequisites](#prerequisites)
    - [Suggested virtual environment](#suggested-virtual-environment)
    - [Suggested IDE](#suggested-ide)
- [Libraries](#libraries)
    - [PySimpleGUI](#pysimplegui)
        - [Inside the event loop](#inside-the-event-loop)
- [Contribute](#contribute)
- [Versioning](#versioning)
- [Author](#author)

<hr>

## Discuss the project
I'll soon built a forum (maybe a Django blog) where we can discuss all the projects. For now, you could open a subreddit if you want. 

## Prerequisites

### Suggested virtual environment
I'll write you how to create the environment I am using.

### Suggested IDE
I suggest you to use [PyCharm](https://www.jetbrains.com/pycharm/)

## Libraries

### PySimpleGUI

#### Inside the event loop
For persistent windows (after creating the window), you have an event loop that runs until you exit the window. Inside this loop you will read values that are returned from reading the window and you'll operate on elements in your window. To operate on elements, you look them up and call their method functions such as `update`.

##### Element 

## Contribute
Feel free to contribute by opening a pull request, but take care about the naming conventions.
## Versioning
For the versions available, see the [tags on this repository](https://github.com/PitPietro/pythonGUI/tags).

## Author
**Pietro Poluzzi** - [PitPietro](https://github.com/PitPietro)
<br>See also the list of [contributors](https://github.com/PitPietro/pythonGUI/contributors) who participated in this project.