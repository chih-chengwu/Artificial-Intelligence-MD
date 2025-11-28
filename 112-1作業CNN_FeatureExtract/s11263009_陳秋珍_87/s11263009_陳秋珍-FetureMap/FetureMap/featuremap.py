import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

#fuction read image file 
def read_images_from_directory(directory):
    image_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    images = []
    for image_file in image_files:
        image_path = os.path.join(directory, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            images.append((image_file, image))
        else:
            print(f"Error: Unable to read image {image_path}")

    return images

def get_edge_features(image, kernel_size, direction):
    if direction == "horizontal":
        #kernel = np.array([[1, 1], [1, 1]])
        kernel = np.array([[0, 0], [1, 1]])
    elif direction == "vertical":
        #kernel = np.array([[1, 1], [1, 1]]).T
        kernel = np.array([[0, 1], [0, 1]]).T
    else:
        #kernel = np.array([[1, 1], [-1, 1]])
        kernel = np.array([[0, 1], [1, 0]])

    feature_map = cv2.filter2D(image, -1, kernel, borderType=cv2.BORDER_REPLICATE)
    return feature_map

def save_feature_map(feature_map, output_dir, original_name, suffix):
    output_name = f"{original_name.split('.')[0]}_{suffix}.jpg"
    output_path = os.path.join(output_dir, output_name)
    cv2.imwrite(output_path, feature_map)

if __name__ == "__main__":
    # Specify the image directory
    image_directory ='OriginalIMG'

    #read all .jpg file image
    image = read_images_from_directory(image_directory)

    # Process and save each image
    for image_file, image in image:
        
        # Get horizontal, vertical, and diagonal edge features
        horizontal_feature_map = get_edge_features(image, 3, "horizontal")
        vertical_feature_map = get_edge_features(image, 3, "vertical")
        diagonal_feature_map = get_edge_features(image, 3, "diagonal")

         # Specify the output directory
        output_dir = 'result'

        # Display the images using matplotlib.pyplot
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 4, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(1, 4, 2)
        plt.imshow(horizontal_feature_map, cmap='gray')
        plt.title('Horizontal Feature Map')
        save_feature_map(horizontal_feature_map, output_dir, image_file, 'horizontal')
        plt.axis('off')

        plt.subplot(1, 4, 3)
        plt.imshow(vertical_feature_map, cmap='gray')
        plt.title('Vertical Feature Map')
        save_feature_map(vertical_feature_map,output_dir, image_file,'vertical_feature_map.jpg')
        plt.axis('off')

        plt.subplot(1, 4, 4)
        plt.imshow(diagonal_feature_map, cmap='gray')
        plt.title('Diagonal Feature Map')
        save_feature_map(diagonal_feature_map,output_dir, image_file,'diagonal_feature_map.jpg')
        plt.axis('off')

        plt.show()