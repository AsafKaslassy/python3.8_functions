import abc


class AbstractVideo(abc.ABC):
    @abc.abstractmethod
    def play(self): pass

class VideoClip(AbstractVideo):
    def __init__(self,id):
        self__id = id
    def play(self):
        print("playing the video...")

class ProxyVideoClip(AbstractVideo):
    def __init__(self,id):
        self.__id = id
        self.__video = None
    def play(self):
        if self.__video == None:
            self.__video = VideoClip(self.__id)
            self.__video.play()

clips = [ProxyVideoClip(234233), ProxyVideoClip(54634), ProxyVideoClip(876433)]

clips[0].play()