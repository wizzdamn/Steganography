import cv2
import os

# Check if the message can fit in the image
def can_fit_message(img, msg):
    return len(msg) <= img.size // 3  # Each pixel can hold one character in one channel

# Read the image
img = cv2.imread("image.png")  # Replace with the correct image path
if img is None:
    print("Error: Image not found.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

if not can_fit_message(img, msg):
    print("Error: Message is too long to fit in the image.")
    exit()

# Create dictionaries for encoding and decoding
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Embed the message into the image
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3
    if m >= img.shape[1]:  # Move to the next row if we reach the end of the current row
        m = 0
        n += 1
    if n >= img.shape[0]:  # Stop if it exceeds the image height
        break

# Save the modified image
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows

# Decrypt the message
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")
if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
        if m >= img.shape[1]:  # Move to the next row if we reach the end of the current row
            m = 0
            n += 1
        if n >= img.shape[0]:  # Stop if it exceeds the image height
            break
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")