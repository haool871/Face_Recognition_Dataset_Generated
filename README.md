# Face_Recognition_Dateset_Generate
## Back Ground
I found this job for one of my competitions.This job is expected to creat a Dataset that include some pictures of face
experession.

## Install
Necessary packages are as fllowed.
- os
- opencv
## usage
Put your videos in *mp4_real* and *mp4_fake* to get pictures.Then simply run main.py.
## notes for myself
- Store videos in *mp4_real*  and *mp4_Fake*.
- Store draw_Frames pictures in *genuine_human*  and *Fake_human*.
- Store final results in *genuine* & *Fake*.
- model store in absolute path.
## To Do List
- [x] 实现视频抽帧并保存
- [x] 识别抽帧图片中人脸并保存
- [ ] 获得较为纯净的数据集，减少清洗难度
