Steganography Tool:
This python based tool allows users to encrypt crucial message within an image (using steganography) and retrieve it later using a passcode. The message is encoded in the image by modifying the pixel values, and it can only be decrypted with the correct passcode. This is a basic implementation of image-based steganography using Python and the OpenCV library.

Requirements:
Python 3.x or higher
OpenCV (cv2) library
An image file to embed the secret message (e.g., .png format).

Usage:
Step 1: Hide the Message in an Image
Input an Image: Provide an image file (e.g., image.png) to hide your message in.
Enter the Secret Message: Type the message you want to hide.
Enter a Passcode: Set a passcode for securing the message. You will need this passcode later for decryption.

Example:
Enter secret message: The text you want to encrypt
Enter a passcode: pass@123
The tool will encode the message into the image and save it as encryptedImage.png. It will also open the image to show you the result.

Step 2: Decrypt the Message
Provide the Encrypted Image: Use the image with the hidden message (encryptedImage.png).
Enter the Passcode: To retrieve the hidden message, input the passcode that was used during encryption.
If the passcode is incorrect, you will receive an authorization error message.

Error Handling:
If the message is too long to fit in the image, the tool will notify you and stop.
If the image cannot be found, an error will be displayed.
If the wrong passcode is entered during decryption, an "Authorization Failed" message will appear.

Limitations:
The secret message is encoded in the least significant bits of the image pixels. This means:
The message size is limited by the number of pixels in the image.
Large messages may distort the image or exceed the image's capacity.
The image file must be in a format that OpenCV can read (e.g., .png, .jpg).
This tool does not perform advanced error handling or compression techniques for large messages.
Code Walkthrough
Reading the Image: The image is read using OpenCV's cv2.imread() function. If the image path is incorrect, the program will notify the user.

Message Encoding: The message is encoded character by character into the image pixels. Each pixel's RGB values are modified to store one character of the message in each channel (R, G, B).

Message Decoding: The encoded message can be retrieved by reversing the encoding process. The passcode entered by the user is checked to ensure that the decryption is authorized.

File Saving: After encoding the message, the modified image is saved as encryptedImage.png. This image contains the hidden message and can be shared.

Decrypting the Message:
Enter passcode for Decryption: mypasscode
Decrypted message: This is a secret.

Conclusion:
This tool provides a basic demonstration of steganography, enabling you to securely hide messages in images. It combines image manipulation with a password-based security mechanism to protect the hidden content.

