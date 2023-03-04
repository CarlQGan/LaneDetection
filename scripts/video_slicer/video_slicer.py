import argparse
import cv2
import os

def slice_video(video_path, output_folder, interval):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Set the initial frame count and image count
    frame_count = 0
    image_count = 0
    
    # Loop through the video frames
    while cap.isOpened():
        # Read the next frame
        ret, frame = cap.read()
        
        # Check if frame was read successfully
        if not ret:
            break
        
        # Check if enough frames have passed to capture an image
        if frame_count % interval == 0:
            # Save the frame as a JPG image
            image_path = os.path.join(output_folder, f"image{image_count}.jpg")
            cv2.imwrite(image_path, frame)
            image_count += 1
        
        # Increment the frame count
        frame_count += 1
    
    # Release the video file
    cap.release()

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("video_path", help="Path to the video file to slice")
parser.add_argument("interval", type=int, help="Number of frames to wait between capturing each image")
args = parser.parse_args()

# Get video filename and create output folder
video_filename = os.path.basename(args.video_path)
output_folder = os.path.join("out", video_filename[:-4] + "_" + str(args.interval))
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Slice the video
input_path = os.path.join("input_vid", video_filename)
slice_video(input_path, output_folder, args.interval)
