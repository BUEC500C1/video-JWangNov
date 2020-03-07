# HW4

## Task 1
Estimate the processing power need to execute such operations on your computer. 
Estimate the maximum number of such operations that can run on your system.

### FFmpeg
Use FFmpeg to re-encode a video file:

```
$ python videoEncoder.py [input path] [output path] [type]
or
$ python3 videoEncoder.py [input path] [output path] [type]
```

Note that [type] can only accept "0" (480p at 1Mbps and 30fps) and "1" (720p at 2Mbps and 30fps).

For example, 
you can run `python3 videoEncoder.py MonsterDrinkKebab.mp4 nu.mp4 1` in `this_repo/task_1`.

Example video get from [here](https://www.youtube.com/watch?v=cw31vtWOXuk).


## Task 2
Build Twitter Video Generator in Queue Frame

`videoGenerator.py` generates tweeter video from 1 user.

`videoQueue.py` generates videos in queue frame.


## Web Service
I use Flask to provide the web service.

[](http://3.136.158.120:8421/)
