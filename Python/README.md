# Automatic Image Resizing and Cropping

## Introduction

Basically, it is annoying to convert by hand the pictures in order for them to fit in the slider in the project. Hence I created this scripts to automatically resize and crops the pictures put in the **pictures_portrait** folder.

## Prerequisites

You probably need [Python](https://www.python.org/download/) and the [PIL](http://www.pythonware.com/products/pil/) module.

## How to use it

You just need to put your pictures from a certain location *loc* in the folder
*pictures_portrait/loc* and then run the scripts to find the results in the
folder *pictures_landscape/loc*.

For example, some pictures from Geneva would be in the folder *pictures_portrait/Geneva* and the results would be in
*pictures_landscape/Geneva*.

Then you just need to run the scripts with:

```{bash}
python resize_crop_pictures.py
```

The pictures are all renamed and resized to fit in the pictures sliders from the **index.html**.

## Note
Any format of image are resized (ie. portrait but also 3/2 format pictures). The truncation or crop are taken from the middle of the pictures.

