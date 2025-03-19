<div align="center">

# Exercise 6 - Image Processing Project

**Image Processing Project** is the sixth exercise I solved as part of Huji's **Introduction to Computer Science** course.  
The main goal of this exercise is to get familiar with **Python 3**, the **Math library**, and to practice working with images, matrix manipulation, and algorithm implementation.

[View All Exercises](https://github.com/AfekAharoni/Intro2CS)

</div>

---

## Exercise Description

This project includes:
1. `image_editor.py` - Implements an interactive console-based image editor. The program allows users to load an image and perform various operations on it, such as converting to grayscale, blurring, resizing, rotating, detecting edges, quantizing, and saving the edited image.
2. `ex6_helper.py` - Provides helper functions for loading, displaying, and saving images. It also includes conversions between PIL images and Python lists for image manipulation.

### Features:
- Convert RGB images to grayscale
- Blur images with customizable kernel size
- Resize images using bilinear interpolation
- Rotate images by 90 degrees (right or left)
- Edge detection using adaptive thresholding
- Quantize images to reduce the number of colors
- Save and display the edited images

---

## How to Run the Code

Run the program with the following command and provide an image path as an argument:

```
python image_editor.py <image_path>
```

Example:

```
python image_editor.py sample_image.png
```

Once running, the program will show an interactive menu where you can select the operations to perform.

---

## Technologies Used
- **Math library** (`math` module)
- **PIL (Python Imaging Library)** (`PIL` module)
- `copy`, `sys` modules for system operations and deep copies
- Type hinting for clean and readable code

---

## File Structure

```
Ex6-ImgProcessing/
├── image_editor.py
└── ex6_helper.py
```

---
