from PIL import Image
import os
import glob


def image_slice(image, height, width):
    imgwidth, imgheight = image.size
    for i in range(imgheight // height):
        for j in range(imgwidth // width):
            #print(i, j)
            img_box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            yield image.crop(img_box)


if __name__ == '__main__':
    imgdir = '2TestImages2Secs/'
    basename = '*.jpg'
    filelist = glob.glob(os.path.join(imgdir, basename))
    count = 0
    for filenum, infile in enumerate(filelist):
        image = Image.open(infile)
        #print (im)
        imgwidth, imgheight = image.size
        #print ('Image size is: %d x %d ' % (imgwidth, imgheight))
        height = int(imgheight / 100)
        width = int(imgwidth / 100)
        start_num = 0
        dirname = "slices_of_image"
        path1 = 'ColorTest2Secs10000Tiles/' + dirname + str(count)
        if not os.path.isdir(path1):
            os.mkdir(path1)
        count += 1
        imgcount = 0
        for k, piece in enumerate(image_slice(image, height, width), start_num):
            img = Image.new('RGB', (width, height), 255)  # change 'L' to 'RGB' to get colored images
            # print img
            img.paste(piece)
            temp = os.path.join(path1, "slice_" + str(imgcount) + ".jpg")
            img.save(temp)
            imgcount += 1


# mv .ipfs ipfs.bak;
#du -s or du -sh
