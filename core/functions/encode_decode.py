import base64

def encode_img(test_img):
    with open(test_img, "rb") as img_file:
        encode_string = base64.b64encode(img_file.read())
    return encode_string


def decode_img(test_img):
    with open(test_img, "rb") as img_file:
        encode_string = base64.b64encode(img_file.read())
    return encode_string