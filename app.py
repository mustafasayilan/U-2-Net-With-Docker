import gradio as gr
from PIL import Image
import torch
from torchvision import transforms
from model import U2NET
from u2net_test import normPRED
import numpy as np
import os
import tempfile

# Load the pre-trained U-2-Net model
model_path = "./saved_models/u2net/u2net.pth"  # Path to the pre-trained model file
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available, otherwise fallback to CPU
model = U2NET(3, 1)  # Initialize the U-2-Net model with input channels = 3 and output channels = 1
model.load_state_dict(torch.load(model_path, map_location=device))  # Load model weights into the initialized model
model.to(device)  # Transfer the model to the appropriate device (CPU or GPU)
model.eval()  # Set the model to evaluation mode (disables training-specific layers like dropout)

def remove_background(image):
    """
    Removes the background from an uploaded image and saves the output as a JPG file.
    """
    # Prepare the input image by applying necessary transformations
    transform = transforms.Compose([
        transforms.Resize((320, 320)),  # Resize the image to 320x320 pixels
        transforms.ToTensor(),  # Convert the image to a PyTorch tensor
    ])

    # Convert the input image to a tensor and add a batch dimension
    input_image = transform(image).unsqueeze(0).to(device)

    # Perform inference using the U-2-Net model
    with torch.no_grad():  # Disable gradient calculations to speed up inference and save memory
        d1, *_ = model(input_image)  # Run the model and get the first output (d1 contains the most detailed prediction)
        pred = d1[:, 0, :, :]  # Extract the single-channel output
        pred = normPRED(pred)  # Normalize the output prediction to the range [0, 1]

    # Convert the prediction mask to a binary image
    mask = (pred.squeeze().cpu().numpy() * 255).astype(np.uint8)  # Convert the normalized prediction to uint8 (0-255)
    mask_image = Image.fromarray(mask).resize(image.size)  # Resize the mask to match the original image size
    result_image = Image.composite(
        image,  # The original input image
        Image.new("RGB", image.size, (0, 0, 0)),  # A black background to replace the removed areas
        mask_image  # The binary mask that determines where the background is removed
    )

    # Save the resulting image as a temporary JPG file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")  # Create a temporary file with .jpg extension
    result_image.save(temp_file.name, "JPEG", quality=95)  # Save the image with high quality (95)

    return temp_file.name  # Return the path to the saved temporary file

# Define the Gradio interface
interface = gr.Interface(
    fn=remove_background,  # The function to be called when an image is uploaded
    inputs=gr.Image(type="pil", label="Upload Image"),  # Specify input type as an image
    outputs=gr.File(label="Download Processed Image"),  # The output is a file (JPG format) for downloading
    title="U-2-Net Background Remover",  # The title displayed on the web interface
    description="Upload an image to remove its background. The result will be a JPG image."  # Short description
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)  # Start the interface on all network interfaces at port 7860
