from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

class Editor:
    def __init__(self):
        self.videoPath = ''
        self.videoName = ''
        self.videoDuration = 0
        self.numberCuts = 0

    def setVideoPath(self, path):
        if path != "":
            self.clip = VideoFileClip(path)
            self.videoDuration = self.clip.duration
        self.videoPath = path

    def setVideoCuts(self, cuts):
        if cuts != "":
            self.numberCuts = cuts

    def setVideoName(self, name):
        self.VideoName = name

    def startEdition(self):
        try:
            if self.numberCuts == '':
                return False

            if self.videoDuration == '':
                return False

            if self.videoPath == '':
                return False

            self.numberCuts = float(self.numberCuts)
            self.videoDuration = float(self.videoDuration)

            intervalo = round(self.videoDuration / self.numberCuts)

            contador = 0
            timer = 0
            while contador < self.numberCuts:
                if contador == self.numberCuts - 1:
                    ffmpeg_extract_subclip(self.videoPath, timer, self.videoDuration, targetname="VIDEO_CUT_{}.mp4".format(contador))
                else:
                    ffmpeg_extract_subclip(self.videoPath, timer, intervalo+timer, targetname="VIDEO_CUT_{}.mp4".format(contador))

                timer = timer + intervalo
                contador = contador + 1

            return True
        except:
            print('teste exepct')
            return False
