# import cv2

# def make_sketch(img):
#     grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     inverted = cv2.bitwise_not(grayed)
#     blurred = cv2.GaussianBlur(inverted, (19,19), sigmaX=0, sigmaY=0)
#     result = cv2.divide(grayed, 255 - blurred, scale=256)
#     return result


# import cv2

# def make_sketch(img):
#     # Convert the image to grayscale
#     grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply adaptive thresholding for better contrast
#     thresh = cv2.adaptiveThreshold(grayed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#     # Invert the thresholded image
#     inverted = cv2.bitwise_not(thresh)

#     # Apply Gaussian Blur for smoother lines
#     blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)

#     # Blend the original grayscale image with the blurred image using dodge blending
#     blend = cv2.divide(grayed, 255 - blurred, scale=256)

#     return blend



import cv2

def make_sketch(img):
    # Convert the image to grayscale
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to the grayscale image with a larger kernel
    blurred = cv2.GaussianBlur(grayed, (31, 31), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted = cv2.bitwise_not(blurred)

    # Blend the original grayscale image with the inverted image using dodge blending
    blend = cv2.divide(grayed, 255 - inverted, scale=256)

    return blend