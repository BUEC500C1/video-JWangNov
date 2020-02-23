import os
import sys


def encodeVideo(pathInput, pathOutput, resolution):
    if resolution == "0":
        # 480p at 1Mbps and 30fps
        cmd = "ffmpeg -i " + pathInput + " " + pathOutput
        cmd += " -c:a copy -c:v copy -r 30 -s hd4800 -b:v 1M"
    if resolution == "1":
        # 720p at 2Mbps and 30fps
        cmd = "ffmpeg -i " + pathInput + " " + pathOutput
        cmd += " -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M"

    try:
        os.system(cmd)
        print("DONE (720p at 2Mbps and 30fps)")
    except Exception as e:
        print("reencode FAILED")


if __name__ == '__main__':
    try:
        pathInput = sys.argv[1]
        pathOutput = sys.argv[2]
    except Exception as e:
        print("path setting FAILED")
    try:
        resolution = sys.argv[3]
    except Exception as e:
        print("resolution setting FAILED")

    encodeVideo(pathInput, pathOutput, resolution)
