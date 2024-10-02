import scipy.io
import os
import matplotlib.pyplot as plt
from PIL import Image

# Path to the local dataset directory
data_dir = './wiki'

# Path to the metadata file
metadata_file = os.path.join(data_dir, 'wiki.mat')

# Load the metadata from the .mat file
metadata = scipy.io.loadmat(metadata_file)
# Extract the relevant metadata
wiki_data = metadata['wiki'][0, 0]
image_paths = wiki_data[2][0]
names = wiki_data[4][0]
genders = wiki_data[3][0]
dobs = wiki_data[1][0]
face_scores = wiki_data[6][0]

# Function to display an image with its metadata
def display_image_with_metadata(image_path, name, gender, dob, face_score):
    # Construct the full image path
    full_image_path = os.path.join(data_dir, image_path[0])
    
    # Open and display the image
    image = Image.open(full_image_path)
    plt.imshow(image)
    plt.imshow(image)
    title = (f"Name: {name[0]}\n"
             f"Gender: {gender}\n"
             f"Birthdate: {dob}\n"
             f"Face score: {face_score}")
    plt.title(title)
    plt.axis('off')
    plt.show()
    plt.axis('off')
    plt.show()

# Display a few images with their metadata
for i in range(5):
    display_image_with_metadata(image_paths[i], names[i], genders[i], dobs[i], face_scores[i])