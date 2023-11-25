# Digital Image Processing Project: Restoration of Chhatrapati Shivaji Maharaj's Image
Welcome to the Digital Image Processing project focused on restoring an old image of the Indian king Chhatrapati Shivaji Maharaj. In this project, we employ various image processing techniques to enhance and restore the historical image.

## Introduction
The goal of this project is to employ various image processing methods to address common challenges faced by historical images, such as noise, marks, and fading. We begin by adding and removing salt-and-pepper noise to simulate the effects of aging. Subsequently, we explore the process of inpainting to selectively restore specific regions of the image. To add a touch of vibrancy, we integrate DeOldify, a powerful deep-learning model for colorization, to bring the restored image to life.

## Features

- **Salt-and-Pepper Noise Addition and Removal:** Simulate aging effects and restore the image using a median filter.
- **Inpainting for Region Restoration:** Selectively restore marked regions using thresholding and dilation.
- **DeOldify Colorization:** Enhance the visual appeal by colorizing the final image.


Explore this project to witness the transformation of a historic image through the lens of digital image processing!


# Getting Started

Follow these steps to set up and run the Digital Image Restoration Project on your local machine.

## Prerequisites
- Python (version 3.10 or later)
- OpenCV library (install using `pip install opencv-python`)
- Matplotlib library (install using `pip install matplotlib`)
- NumPy library (install using `pip install numpy`)

## Installation
 
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Sahilahir/digital_image_processing_project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd digital_image_processing_project 
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv 
   ```

4. Activate the virtual environment:
- For Windows
  ```bash
   .\venv\Scripts\activate 
   ```
- For Mac
   ```bash
   source venv/bin/activate 
   ```

5. Install the project dependencies:

   ```bash
   pip install opencv-python 
   ```
   ```bash
   pip install matplotlib 
   ```
   ```bash
   pip install numpy 
   ```



# Usage

## 1. Salt-and-Pepper Noise Addition and Restoration

Run the following script to simulate the effects of aging by adding salt-and-pepper noise to the original image and then restoring it:

   ```bash
   python salt_pepper.py
   ```
See The Results in the images folder. 

This script utilizes OpenCV and Matplotlib to visualize the original image, the image with added noise, and the final restored image. Adjust the noise probability and filter size in the script as needed.

You can also see the process in the salt_pepper.ipynb file to understand the process.


## 2. Inpainting for artifact removal in the image

Before running this script you first need to mark the artifact area or damaged area or area thay you think are missing pixel values then mark those areas using paint or any other tools and make them white use paint and brush those region with white colour and save the image as marked_image.jpg in the images folder. then run the following script: 

   ```bash
   python artifact_removal.py
   ```
See the restored noise removed image in the images folder (Restored_denoiosed_image.jpg).

This script uses advanced techniques such as thresholding, dilation, and Inpainting. It creates a binary mask, expands the mask boundaries, and finally applies inpainting to restore the marked regions. 


