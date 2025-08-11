import os
from PIL import Image

#settings
input_folder="input_images"
output_folder="output_images"
new_size=(800,800)
output_format="JPEG"

os.makedirs(output_folder,exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png','.jpg','.jpeg','.bmp','.gif','.webp'):
        img_path=os.path.join(input_folder,filename)
        try:
            with Image.open(img_path) as img:
                img_resized=img.resize(new_size,Image.LANCZOS)
                base_name=os.path.splitext(filename)[0]
                output_path=os.path.join(output_folder,f"{base_name}.{output_format.lower()}")
                img_resized.save(output_path,output_format)
                print(f"processed:{output_path}")
        except Exception as e:
            print(f"Error proceesing {filename}:{e}")
print("All image resized & convert")
