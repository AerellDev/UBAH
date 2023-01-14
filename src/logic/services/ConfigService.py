import configparser
from pathlib import Path
import os

class ConfigService():
    config = configparser.ConfigParser()

    # Output Folder
    audioPath = ''
    dokumentPath = ''
    imagePath = ''
    videoPath = ''

    # Init
    def init(self):
        self.config.read('config.ini')
        self.audioPath = self.config.get('output', 'audio').strip('"')
        self.dokumentPath = self.config.get('output', 'document').strip('"')
        self.imagePath = self.config.get('output', 'image').strip('"')
        self.videoPath = self.config.get('output', 'video').strip('"')
        if not os.path.exists(self.audioPath):
            os.makedirs(self.audioPath)
        if not os.path.exists(self.dokumentPath):
            os.makedirs(self.dokumentPath)
        if not os.path.exists(self.imagePath):
            os.makedirs(self.imagePath)
        if not os.path.exists(self.videoPath):
            os.makedirs(self.videoPath)

        
        



