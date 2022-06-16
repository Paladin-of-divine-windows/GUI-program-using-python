from email.mime import image
import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO


def update_image(original, blur, contrast, emboss, contour, flipx, flipy):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())
    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format = 'PNG')
    window['-IMAGE-'].update(data = bio.getvalue())

image_path = sg.popup_get_file('Open', no_window=True, file_types=(("Images", "*.png"),))

control_col =sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0,10), orientation='horizontal', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0,10), orientation='horizontal', key='-CONTRAST-')]])],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Contour', key='-CONTOUR-')],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Button('Save image', key='-SAVE-'), sg.Button('Load image', key='-LOAD-')],])
image_col =  sg.Column([[sg.Image(image_path, key='-IMAGE-')]])

layout = [[control_col, image_col]]

original = Image.open(image_path)
window = sg.Window('Image editor', layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break
    
    update_image(
    original, 
    values['-BLUR-'],
    values['-CONTRAST-'],
    values['-EMBOSS-'],
    values['-CONTOUR-'],
    values['-FLIPX-'],
    values['-FLIPY-'])

    if event == '-SAVE-':
        file_path = sg.popup_get_file('Save', no_window=True, save_as=True) + ".png"
        image.save(file_path, 'PNG')
    if event == '-LOAD-':
        image_path = sg.popup_get_file('Open', no_window=True, file_types=(("Images", "*.png"),))
        original = Image.open(image_path)
        window['-BLUR-'].update(0)
        window['-CONTRAST-'].update(0)
        window['-EMBOSS-'].update(0)
        window['-CONTOUR-'].update(0)
        window['-FLIPX-'].update(0)
        window['-FLIPY-'].update(0)

window.close()