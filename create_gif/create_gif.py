# Project is from https://www.codedex.io/projects/create-a-gif-with-python
import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)

# This code creates an animated GIF from two PNG images.

