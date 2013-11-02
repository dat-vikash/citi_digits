import os
from django.core.management import BaseCommand
from subprocess import call

__author__ = 'vikashdat'

"""
    This command converts amr files to mp3 audio files.
"""

class Command(BaseCommand):
    args = ''
    help = ''

    def convertAMRToMp3(self,dirpath,filename):
        pathToAMR = os.join(dirpath,filename)
        pathToMP3 = os.join(dirpath,"%s.mp3" % (filename))

        print "Creating file: " + pathToMP3

        # ffmpeg -i .amr -acodec libmp3lame -ab 64k test.mp3
        call(["ffmpeg", "-i",pathToAMR,"-acodec","libmp3lame","-ab","64k",pathToMP3])

    def findAMRFiles(self, paths):
        for dirpath, dirnames, filenames in paths:
            fileToProcess = None
            alreadyEncodedFlag = False
            for filename in filenames:
                if ".amr" in filename:
                    fileToProcess = (dirpath,filename)
                if ".mp3" in filename:
                    alreadyEncodedFlag = True
            if (alreadyEncodedFlag):
                print "Working on file: " + fileToProcess[1]
                self.convertAMRToMp3(fileToProcess)

    def getDirectoryListing(self):
        """
            Returns a listing of the application's audio directory
        """
        for dirpath, dirnames, filenames in os.walk('../../../media/audio/'):
            self.findAMRFiles((dirpath, dirnames, filenames))

    def handle(self, *args, **options):
        print "Starting audio conversions...."
        self.getDirectoryListing()
        print "Conversion complete..."

