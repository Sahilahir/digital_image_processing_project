from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *


torch.backends.cudnn.benchmark = True

# Specify the path to your black and white restored image
input_path = Path("C:/Semester4/digital_image_processing/dip_project/images/Restored_denoised_image.jpg")

# Colorize the image and store the result in a results folder
colorizer = get_image_colorizer(artistic=True)
colorizer.plot_transformed_image(input_path, results_dir=Path('C:/Semester4/digital_image_processing/dip_project/result_images'), watermarked=False)
