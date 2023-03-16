# -*- coding: utf-8 -*-

import cv2
import os
import pdb
import numpy as np


# from glob2 import glob


def vdprocess(videos_src_path, output_path):
    # 获取指定路径下的文件
    dirs = os.listdir(videos_src_path)
    print(dirs)

    # 根据名称创建对应的文件夹
    for video_name in dirs:
        video_filename = video_name.split('.')[0]
        print(video_filename)
        if not os.path.exists(os.path.join(output_path, video_filename)):
            os.mkdir(os.path.join(output_path, video_filename))

        # 循环读取路径下的文件并操作
        print("start\n")
        print(videos_src_path + video_name)
        vc = cv2.VideoCapture(videos_src_path + video_name)

        # 初始化,并读取第一帧
        # rval表示是否成功获取帧
        # frame是捕获到的图像
        rval, frame = vc.read()

        # 获取视频fps
        fps = vc.get(cv2.CAP_PROP_FPS)
        # 获取每个视频帧数
        frame_all = vc.get(cv2.CAP_PROP_FRAME_COUNT)
        # 获取所有视频总帧数
        # total_frame+=frame_all

        print("[INFO] 视频FPS: {}".format(fps))
        print("[INFO] 视频总帧数: {}".format(frame_all))
        # print("[INFO] 所有视频总帧: ",total_frame)
        # print("[INFO] 视频时长: {}s".format(frame_all/fps))

        # if os.path.exists(outputPath) is False:
        #     print("[INFO] 创建文件夹,用于保存提取的帧")
        #     os.mkdir(outputPath)

        # 每n帧保存一张图片
        frame_interval = 4
        # 统计当前帧
        frame_count = 0
        count = 0

        while rval:
            rval, frame = vc.read()
            if frame_count % frame_interval == 0:
                if frame is not None:
                    filename = output_path + video_filename + "/0000{}.jpg".format(count)
                    cv2.imwrite(filename, frame)
                    count += 1
                    print("保存图片:{}".format(filename))
            frame_count += 1
        # 关闭视频文件
        vc.release()
        print("[INFO] 总共保存：{}张图片\n".format(count))
