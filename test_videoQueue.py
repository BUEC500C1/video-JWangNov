from videoQueue import VideoQueue


def test_000():
    pipelineNum = 6
    queueSize = 100
    howManyTweets = 10

    ll0 = ['@LagavulinWhisky', '@Laphroaig', '@Kilchomanwhisky', '@Benromach', '@clydesidewhisky']
    obj0 = VideoQueue(pipelineNum, queueSize)
    for user in ll0:
        obj0.getQueued(user, howManyTweets)
    assert obj0.run() == 0

    ll1 = ['@Benromach']
    obj1 = VideoQueue(pipelineNum, queueSize)
    for user in ll1:
        obj1.getQueued(user, howManyTweets)
    assert obj1.run() == 0

    ll2 = ['@LagavulinWhisky', '@Laphroaig']
    obj2 = VideoQueue(pipelineNum, queueSize)
    for user in ll2:
        obj2.getQueued(user, howManyTweets)
    assert obj2.run() == 0


def test_001():
    pipelineNum = 2
    queueSize = 100
    howManyTweets = 10

    ll3 = ['@LagavulinWhisky', '@Laphroaig', '@Kilchomanwhisky', '@Benromach', '@clydesidewhisky']
    obj3 = VideoQueue(pipelineNum, queueSize)
    for user in ll3:
        obj3.getQueued(user, howManyTweets)
    assert obj3.run() == 0


def test_002():
    pass
