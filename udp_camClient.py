import time
from socket import *
import cv2
import struct

# class VideoCamera(object):
#     def __init__(self):
#         # Using OpenCV to capture from device 0. If you have trouble capturing
#         # from a webcam, comment the line below out and use a video file
#         # instead.
#         self.video = cv2.VideoCapture(0)
#
#         # if not self.video.isOpened():
#         #     print("Cannot open camera")
#         #     exit()
#         # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#         # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#         # If you decide to use video.mp4, you must have this file in the folder
#         # as the main.py.
#         # self.video = cv2.VideoCapture('video.mp4')
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         success, image = self.video.read()
#         # We are using Motion JPEG, but OpenCV defaults to capture raw images,
#         # so we must encode it into JPEG in order to correctly display the
#         # video stream.
#         # print(np.size(image))
#         image = cv2.resize(image,(200,200))
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()



# cam = VideoCamera()

host = "10.167.97.225"
port = 5005

Udp_Socket = socket(AF_INET,SOCK_DGRAM)
Udp_Socket.bind(("10.167.102.123", 6543))
video = cv2.VideoCapture(0)
while True:


    success, image = video.read()
    image = cv2.resize(image, (400, 300))
    ret, jpeg = cv2.imencode('.jpg', image)
    # cv2.imshow("capature", image)
    frame_b = jpeg.tobytes()
    # print(len(frame_b))
    # str_b = b'CAM'
    # frame_len = b'str(len(frame))'
    # send_b = str_b + frame_b
    # frame_len = struct.pack("i",len(frame))#struct 相关的都是为了避免分包和粘包

    # clientSocket.send(frame_len)#先发一个当前frame的Bytes长度。指导服务端接受的buffer的大小
    Udp_Socket.sendto(frame_b, (host, port))

    # clientSocket.send(frame)

    # time.sleep(0.03)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        Udp_Socket.close()
        video.release()
        break

    print("send success")

