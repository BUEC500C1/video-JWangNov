import queue
import threading
from videoGenerator import VideoGen


class VideoQueue():
    def __init__(self, pipelineNum, queueSize):
        self.pipelineNum = pipelineNum
        self.queueSize = queueSize
        self.processingItems = []
        self.myQueue = queue.Queue(queueSize)

    def getQueued(self, username, howManyTweets):
        currT = threading.Thread(target=self.genCurrVideo, args=(username, howManyTweets))
        processingNum = threading.active_count() - 1
        if processingNum < self.pipelineNum:
            currT.run()
            self.processingItems.append(currT)
        else:
            self.myQueue.put(currT)
            print('{} is in queue now.'.format(username))
        return currT

    def genCurrVideo(self, username, howManyTweets):
        currVideo = VideoGen(username, howManyTweets)
        print('Start generating {}\'s video.'.format(username))
        currVideo.run()
        print('{} DONE'.format(username))

    def run(self):
        while not self.myQueue.empty():
            processingNum = threading.active_count()
            if processingNum < self.pipelineNum:
                t = self.myQueue.get()
                t.run()
        for eachItem in self.processingItems:
            if eachItem.is_alive():
                eachItem.join()
        return 0


def main():
    pipelineNum = 2
    queueSize = 100
    obj = VideoQueue(pipelineNum, queueSize)
    obj.getQueued('@LagavulinWhisky', 10)
    obj.getQueued('@Laphroaig', 10)
    obj.getQueued('@Kilchomanwhisky', 10)
    obj.getQueued('@Benromach', 10)
    obj.getQueued('@clydesidewhisky', 10)
    obj.run()


if __name__ == '__main__':
    main()
