VIDEO_PATH = r'./root/Fog20200313000026.mp4' # 视频地址
EXTRACT_FOLDER = r'./output_dir' # 存放帧图片的位置
EXTRACT_FREQUENCY = 25 # 帧提取频率

import cv2
def extract_frames(video_path, dst_folder):
    # 主操作
    video = cv2.VideoCapture(video_path)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(frame_width)
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(frame_height)
    count = 0
    i = 0
    retaining = True

    while (count < frame_count and retaining):
        retaining, frame = video.read()
        if frame is None:
            continue

        if count % EXTRACT_FREQUENCY == 0:
            if (frame_height != 448) or (frame_width != 448):
                frame = cv2.resize(frame, (448, 448))
                frame = frame[112:336,50:274]
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # print(frame)
            cv2.imwrite(filename=os.path.join(r'./output_dir','0000{}.jpg'.format(str(i))), img=frame)
            print('******add******')
            i += 1
        count += 1
    video.release()
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(i-1))

import os
def main():
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER)
if __name__ == '__main__':
    main()