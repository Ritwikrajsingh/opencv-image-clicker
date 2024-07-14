import cv2
import os

def capture_images(num_images):
    image_dir = 'images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        
    cap = cv2.VideoCapture(0)
    
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