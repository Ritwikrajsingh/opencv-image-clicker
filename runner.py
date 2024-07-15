import cv2
import os

def print_webcam_settings(cap):
    print(f"Default Exposure: {cap.get(cv2.CAP_PROP_EXPOSURE)}")
    print(f"Default Gain: {cap.get(cv2.CAP_PROP_GAIN)}")
    print(f"Default Brightness: {cap.get(cv2.CAP_PROP_BRIGHTNESS)}")
    print(f"Default Contrast: {cap.get(cv2.CAP_PROP_CONTRAST)}")


# Function to set webcam parameters
def set_webcam_parameters(cap):
    # Set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Set exposure time (values might need tweaking)
    cap.set(cv2.CAP_PROP_EXPOSURE, 10000)  # default 15, adjust as needed

    # Set gain (values might need tweaking)
    cap.set(cv2.CAP_PROP_GAIN, 10000)  # default 14, adjust as needed

    # Set brightness (values might need tweaking)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, -20)  # default 10, adjust as needed

    # Set contrast (values might need tweaking)
    cap.set(cv2.CAP_PROP_CONTRAST, 25)  # default 11, adjust as needed

    # Set frame rate (values might need tweaking)
    cap.set(cv2.CAP_PROP_FPS, 1)  # default 5, adjust as needed

def capture_images(num_images):
    image_dir = 'images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        
    cap = cv2.VideoCapture(0)
    print_webcam_settings(cap)
    set_webcam_parameters(cap)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture image.")
            break
        
        cv2.imshow('Camera', frame)
        
        image_path = os.path.join(image_dir, f'image_{count+1}.png')
        cv2.imwrite(image_path, frame)
        print(f"Image {count+1} saved as {image_path}")
        
        count += 1
        
        cv2.waitKey(500)
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    num_images = int(input("Enter the number of images to capture: "))
    capture_images(num_images)