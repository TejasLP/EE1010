from PIL import Image

# Load the original image
image = Image.open("input.jpg")

# 1. Convert to Grayscale
# The 'L' mode stands for luminance (8-bit pixels, 256 shades of gray)
grayscale_image = image.convert('L')
grayscale_image.save("grayscale.jpg")

# 2. Convert to strict Black & White (using a threshold)
# Map grayscale pixels to exactly 0 (black) or 255 (white) based on a threshold value
threshold = 128
bw_image = grayscale_image.point(lambda p: 255 if p > threshold else 0)
bw_image = bw_image.convert('1') # Convert to actual 1-bit pixel mode
bw_image.save("black_and_white.png")

# 3. Convert to Dithered Black & White
# PIL's default '1' conversion applies dithering (a stippled/dotted effect) to simulate shading
dithered_image = image.convert('1')
dithered_image.save("dithered_bw.png")

