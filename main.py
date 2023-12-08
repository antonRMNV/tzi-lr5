from PIL import Image
import os

# Кодування зображення
def encode_image(img_path, data):
    img = Image.open(img_path)

    binary_data = ''.join(format(ord(char), '08b') for char in data)
    data_index = 0

    pixels = list(img.getdata())

    for i in range(len(pixels)):
        pixel = list(pixels[i])
        for j in range(3):
            if data_index < len(binary_data):
                pixel[j] = pixel[j] & ~1 | int(binary_data[data_index])
                data_index += 1

        pixels[i] = tuple(pixel)

    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(pixels)
    encoded_img.save('encoded_image.jpg')

def decode_image(img_path):
    img = Image.open(img_path)

    binary_data = ''
    pixels = list(img.getdata())

    for pixel in pixels:
        for value in pixel:
            binary_data += str(value & 1)

    decoded_data = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        decoded_data += chr(int(byte, 2))

    return decoded_data

# Приклад використання
encode_image('original_image.jpg', 'Hello, steganography!')
decoded_data = decode_image('encoded_image.jpg')
print(decoded_data)

# Порівняння розмірів
empty_size = os.path.getsize('original_image.jpg')
stego_size = os.path.getsize('encoded_image.jpg')

print(f"Empty container size: {empty_size} bytes")
print(f"Stego container size: {stego_size} bytes")

# Відновлення даних
def decode(img_path):
    img = Image.open(img_path)
    pixels = list(img.getdata())

    binary_message = ""
    for pixel in pixels:
        for i in range(3):
            binary_message += bin(pixel[i])[2:][-1]

    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        decoded_message += chr(int(byte, 2))

    return decoded_message

# Приклад використання
decoded_message = decode('encoded_image.jpg')
print(f"Decoded message: {decoded_message}")

