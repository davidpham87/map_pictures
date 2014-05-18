### In order to run this file, you just need to put the location folders 
### in the the pictures_portrait folder and run the scripts

import Image # Import the PIL package for resizing and croping the images
import os # Os walking, listing files

global ext # Bad 
ext = ".jpg" # Worse 

def save_picture(im, name, path = 'pictures_landscape'):
    im.save(path + '/' + name + ext)
    return None

def find_locations(path = 'pictures_portrait'):
    return os.walk(path).next()[1]

def portrait_pictures_filenames(path = 'Geneva'):
    _, _, filenames =  os.walk(path).next()
    return [path +  '/' + f for f in filenames if f[-4:] == '.jpg']
        
def keep_aspect_ratio(im, width=640, height=480):
    """
    Find the ratio needed to resize to picture
    If the pictures is a portrait then reduce width to 640
    If the pictures is a landsacpe then reduce height to 480
    """

    w, h = im.size
    if w > h:
        return int(1.0*w/h*height), height
    else:
        return width,  int(width*1.0/w*h)

def box_crop_from_middle(im, width=640, height=480):
    """
    Return a 4-tuple needed for the crop function of im in order to crop from 
    the middle    
    """
    w, h = im.size
    return (w/2-width/2, h/2-height/2, w/2+width/2, h/2+height/2)

def img_resize_crop(im, name_out = '01', width=640, height=480, 
                    save_path = 'pictures_landscape'):
    """
    Resize the image by keeping the ratio and then crop the picture 
    from the middle
    """
    
    w, h = keep_aspect_ratio(im, width, height) # Find the new width and height
    im_resize = im.resize((w, h), Image.ANTIALIAS) # best down-sizing filter    
    
    box = box_crop_from_middle(im_resize, width, height) # Crops from middle
    im_crop = im_resize.crop(box)    

    save_picture(im_crop, name_out, path = save_path)

def count_file(k):
    """
    Useful for naming files
    """
    return str(k) if k > 10 else '0' + str(k)

def im_resize_folder(path = 'pictures_portrait'):
    """
    Find the subfolder/location in the path then save each croped and resized
    picture in that location folder in a new folder 'picture_landscape/location'
    
    The names of the files are convinent for the use of the map_picture project
    (github.com/davidpham87/map_picture)
    """

    locations = find_locations(path)
    for loc in locations:
        pictures = portrait_pictures_filenames(os.path.join(path, loc))

        save_path = os.path.join('pictures_landscape', loc)

        if not os.path.exists(save_path): # Check if directory exist
            os.makedirs(save_path) # Creates it, not perfect solution but ok!

        k = 1
        for pic in pictures:
            im = Image.open(pic)
            img_resize_crop(im, count_file(k), save_path = save_path)
            k += 1

im_resize_folder()
