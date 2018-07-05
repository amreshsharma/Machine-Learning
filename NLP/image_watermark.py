from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_image(input_image,
                   output_image,
                   text, pos):
    photo = Image.open(input_image)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image)


if __name__ == '__main__':
    # img = name of Image to be watermarked
    # text = 'your water mark text on Image'
    img = 'flower1.jpg'
    watermark_image(img, 'flower_watermark.jpg',
                   text='www.99school.in',
                   pos=(0, 0))
