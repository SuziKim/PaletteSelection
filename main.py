from palette.io_util.image import loadRGB
from palette.core.hist_3d import Hist3D
from palette.core.palette_selection import PaletteSelection
import matplotlib.pyplot as plt

image_file = "cazannemont1.jpg"

# Load image.
image = loadRGB(image_file)

# 16 bins, Lab color space
hist3D = Hist3D(image, num_bins=16, color_space='Lab')

color_coordinates = hist3D.colorCoordinates()
color_densities = hist3D.colorDensities()
rgb_colors = hist3D.rgbColors()

# 5 colors from Lab color samples.
palette_selection = PaletteSelection(color_coordinates,
                                             color_densities, rgb_colors,
                                             num_colors=5, sigma=70.0)

