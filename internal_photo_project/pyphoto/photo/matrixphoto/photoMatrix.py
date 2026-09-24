import numpy as np
from PIL import Image

# 1. Load the image and convert it into a NumPy matrix
# Shape will be (Height, Width, 3)
img = Image.open("input.jpg")
img_matrix = np.array(img)

# Strip any alpha (transparency) channel if it's a PNG, keeping only RGB
img_matrix = img_matrix[..., :3]

# 2. Define the luminance weights as a 1D matrix (vector)
weights = np.array([0.299, 0.587, 0.114])

# 3. Perform matrix multiplication (Dot Product)
# This multiplies every [R, G, B] pixel across the entire Height x Width matrix 
# by the weights vector in a single optimized operation.
grayscale_matrix = np.dot(img_matrix, weights)

# 4. Clean up the data
# The result is a matrix of floats. Convert them back to standard 8-bit image integers (0-255).
grayscale_matrix = grayscale_matrix.astype(np.uint8)

# 5. Convert the NumPy matrix back to a PIL Image and save
final_image = Image.fromarray(grayscale_matrix)
final_image.save("matrix_grayscale.jpg")

print("Matrix multiplication complete. Image saved.")
