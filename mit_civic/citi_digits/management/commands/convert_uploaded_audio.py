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

        # ffmpeg -i amrfile -acodec mp3 -ab 64k .mp3file
        call(["ffmpeg", "-i",pathToAMR,"-acodec","mp3","-ab","64k",pathToMP3])

    def findAMRFiles(self, paths):
        for dirpath, dirnames, filenames in paths:
            for filename in filenames:
                if ".amr" in filename:
                    self.convertAMRToMp3(dirpath,filename)

    def getDirectoryListing(self):
        """
            Returns a listing of the application's audio directory
        """
        for dirpath, dirnames, filenames in os.walk('../../../media/audio/'):
            yield (dirpath, dirnames, filenames)

    def handle(self, *args, **options):
        print "Starting audio conversions...."
        for data in self.getDirectoryListing():
            self.findAMRFiles(data)
        print "Conversion complete..."

