import cv2
import os


"""
This function takes in an input video and slices the 
"""
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

# Example usage
video_folder = "input_vid/"
video_filename = "monza_pov_2022_f1_guanyu_zhou.mp4"
video_path = video_folder + video_filename
output_folder = "out/" + video_filename[:-4] + "/"
interval = 1000
slice_video(video_path, output_folder, interval)
