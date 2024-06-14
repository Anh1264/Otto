import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode('utf-8')
    return base64_string

image_path = "image/sourcecode.jpg"
base64_string = image_to_base64(image_path)
print("Base64 String:", base64_string)

def save_base64_image(base64_string, file_path):
    # Decode base64 string to binary image data
    binary_data = base64.b64decode(base64_string)

    # Write binary data to a file
    with open(file_path, 'wb') as file:
        file.write(binary_data)

    print(f"Image saved at: {file_path}")

file_path = 'image2/sourcecode2.jpg'

save_base64_image(base64_string, file_path )
