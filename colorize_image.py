from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *

# Settings
torch.backends.cudnn.benchmark = True

# Specify the path to your black and white image
input_path = Path("C:/Semester4/digital_image_processing/digital_image_processing_project/images/Restored_shivaji.jpg")

# Colorize the image
colorizer = get_image_colorizer(artistic=True)
colorizer.plot_transformed_image(input_path, results_dir=Path('./result_images'), watermarked=False)
