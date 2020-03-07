import configparser
import os
import cv2
import json
import tweepy

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

KEY_PATH = r'keys'
# KEY_PATH = r'./myRealKeys'
FONT_PATH = r'./28DaysLater.ttf'
JSON_LOCAL = r'./local.json'


class VideoGen:
    def __init__(self, user, howManyTweets, keys=KEY_PATH):
        self.user = user
        self.imgPath = './img_{}'.format(user)
        self.howManyTweets = howManyTweets
        self.keys = keys
        cfg = configparser.ConfigParser()
        cfg.read(self.keys)
        try:
            self.consumer_key = cfg.get('auth', 'consumer_key').strip()
            self.consumer_secret = cfg.get('auth', 'consumer_secret').strip()
            self.access_token = cfg.get('auth', 'access_token').strip()
            self.access_secret = cfg.get('auth', 'access_secret').strip()
        except Exception as e:
            print(str(e),' could not read configuration file')

    def getTweets(self):
        tweetsCollection = []
        if os.path.getsize(KEY_PATH) != 91:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_secret)
            myAPI = tweepy.API(auth)
            tweetsReceived = myAPI.user_timeline(screen_name=self.user, count=self.howManyTweets)
            for ele in tweetsReceived:
                tweetsCollection.append(ele.text)
        else:
            with open(JSON_LOCAL, 'r') as ff:
                localJSON = json.load(ff)
                tweetsCollection.append(localJSON['text'])
        return tweetsCollection

    def deleteUnwritable(self, input):
        return input.encode('ascii', 'ignore').decode('ascii')

    def imgGen(self, text, userIdx):
        myFont = ImageFont.truetype(FONT_PATH, 20)
        img = Image.new('RGB', (1600, 500), color=(255, 255, 255))
        graph = ImageDraw.Draw(img)
        graph.text((5, 100), text, font=myFont, fill=(0, 0, 0))
        imgName = '{}/img{}{}.png'.format(self.imgPath, userIdx, self.user)
        img.save(imgName)

    def videoGen(self, videoName):
        # collect all images
        if os.path.exists('{}/.DS_Store'.format(self.imgPath)):
            os.remove('{}/.DS_Store'.format(self.imgPath))
        imgCollection = []
        for root, dirs, files in os.walk(self.imgPath):
            for file in files:
                imgCollection.append(file)
        imgCollection.sort()

        # generate video
        # video = cv2.VideoWriter('./{}.avi'.format(videoName), cv2.VideoWriter_fourcc(*'MJPG'), 0.333, (1600, 500))
        video = cv2.VideoWriter('./{}.mp4'.format(videoName), cv2.VideoWriter_fourcc(*'MP4V'), 0.333, (1600, 500))
        for ii in range(0, len(imgCollection)):
            img = cv2.imread('{}/{}'.format(self.imgPath, imgCollection[ii]))
            img = cv2.resize(img, (1600, 500))
            video.write(img)
        for eachImg in imgCollection:
            os.remove('{}/{}'.format(self.imgPath, eachImg))

    def run(self):
        tweet_list = self.getTweets()

        # generate images, then generate video
        if not os.path.exists(self.imgPath):
            os.mkdir(self.imgPath)
        for ii in range(len(tweet_list)):
            self.imgGen(self.deleteUnwritable(tweet_list[ii]), ii)
        self.videoGen('TV_{}'.format(self.user))
        os.rmdir(self.imgPath)


def main():
    user = '@Bayern_mania'
    howManyTweets = 10
    obj = VideoGen(user, howManyTweets, KEY_PATH)
    obj.run()


if __name__ == '__main__':
    main()
