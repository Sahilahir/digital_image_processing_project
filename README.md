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

