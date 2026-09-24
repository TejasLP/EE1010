#include <stdio.h>
#include <stdlib.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

int main() {
    int width, height, channels;
    
    // Load the image, forcing 3 channels (RGB)
    unsigned char *img = stbi_load("input.jpg", &width, &height, &channels, 3);
    
    if (img == NULL) {
        printf("Error: Could not load input.jpg. Make sure the file exists!\n");
        return 1;
    }

    size_t total_pixels = width * height;
    unsigned char *gray_img = malloc(total_pixels);
    unsigned char *bw_img = malloc(total_pixels);

    if (gray_img == NULL || bw_img == NULL) {
        printf("Error: Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < total_pixels; i++) {
        unsigned char r = img[i * 3 + 0];
        unsigned char g = img[i * 3 + 1];
        unsigned char b = img[i * 3 + 2];

        // Calculate grayscale using luminance formula
        unsigned char gray = (unsigned char)(0.299 * r + 0.587 * g + 0.114 * b);
        gray_img[i] = gray;

        // Apply strict 128 threshold for pure black and white
        bw_img[i] = (gray > 128) ? 255 : 0;
    }

    // Save outputs
    stbi_write_png("pure_c_grayscale.png", width, height, 1, gray_img, width);
    stbi_write_png("pure_c_bw.png", width, height, 1, bw_img, width);

    stbi_image_free(img);
    free(gray_img);
    free(bw_img);

    printf("Done! Saved pure_c_grayscale.png and pure_c_bw.png\n");
    return 0;
}

