from clearscreen import *
import cv2
import numpy as np

gu()


def to_bin(d):
    """Function to convert 'd' to binary format as string"""
    if isinstance(d, str):
        return ''.join([format(ord(i), "08b") for i in d])
    elif isinstance(d, bytes) or isinstance(d, np.ndarray):
        return [format(i, "08b") for i in d]
    elif isinstance(d, int) or isinstance(d, np.uint8):
        return format(d, "08b")
    else:
        raise TypeError("Type not Supported.")


def encode(img_nm, sec_d):
    """Function to hide the data into the image"""
    # reading the image
    img = cv2.imread(img_nm)
    # max bytes to encode
    n_bytes = img.shape[0] * img.shape[1] * 3 // 8
    print("[*] Max Bytes to encode: ", n_bytes)
    if len(sec_d) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or lesser data")
    print("[*] Encoding data...")
    # add stopping criteria
    sec_d += "====="
    d_i = 0
    # convert data to binary
    b_sec_d = to_bin(sec_d)
    # size of data to hide
    d_len = len(b_sec_d)
    for row in img:
        for pix in row:
            # convert RGB values to binary format
            r, g, b = to_bin(pix)
            # modify LSB only if there is still data to store
            if d_i < d_len:
                # LSB of Red Pixel bit
                pix[0] = int(r[:-1] + b_sec_d[d_i], 2)
                d_i += 1
            if d_i < d_len:
                # LSB of Green Pixel bit
                pix[1] = int(g[:-1] + b_sec_d[d_i], 2)
                d_i += 1
            if d_i < d_len:
                # LSB of Blue Pixel bit
                pix[2] = int(b[:-1] + b_sec_d[d_i], 2)
                d_i += 1
            # if data encoded, break out of loop
            if d_i >= d_len:
                break
    return img


def decode(img_nm):
    print("[+] Decoding...")
    # read the image
    img = cv2.imread(img_nm)
    b_d = ""
    for row in img:
        for pix in row:
            r, g, b = to_bin(pix)
            b_d += r[-1]
            b_d += g[-1]
            b_d += b[-1]
    # split by 8 bits
    a_b = [b_d[i: i+8] for i in range(0, len(b_d), 8)]
    # convert bits to characters
    dec_d = ""
    for byte in a_b:
        dec_d += chr(int(byte, 2))
        if dec_d[-5:] == "=====":
            break
    return dec_d[:-5]

if __name__ == "__main__":
    ip_img = "image.png"
    op_img = "enc_image.png"
    sec_d = "Hello World!"
    # encoding data into image
    enc_image = encode(ip_img, sec_d)
    # save the output image (encoded)
    cv2.imwrite(op_img, enc_image)
    # decode secret data from image
    dec_d = decode(op_img)
    print("[+] Decoded data: ", dec_d)

