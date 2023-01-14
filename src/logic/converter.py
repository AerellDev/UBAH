from progress.bar import Bar
from pytube import YouTube
import shutil
import os
from pathlib import Path
from logic.services.ConfigService import ConfigService
from utils.utility import deleteIsiFolder

class Converter():
    configIni = ConfigService
    temp = 'temp'
    def YoutubeToMp3(self, url):
        #Inisiasi Loading Progress
        bar = Bar('Converter : Progress', max=100)
        #Converter Logger
        print('\nConverter : Sedang mengubah video Youtube "' + url + '" menjadi mp3...')
        try:
            # url input from user
            yt = YouTube(url)
            bar.next(n=10)

            try:
                ##@ Extract audio with 160kbps quality from video
                video = yt.streams.filter(abr='160kbps').last()
                bar.next(n=20)

                try:
                    ##@ Downloadthe file
                    out_file = video.download(output_path=self.temp)
                    bar.next(n=20)
                    base, ext = os.path.splitext(out_file)
                    bar.next(n=20)
                    new_file = Path(f'{base}.mp3')
                    bar.next(n=10)
                    os.rename(out_file, new_file)
                    bar.next(n=20)

                    try:
                        ##@ Check success of download
                        if new_file.exists():
                            self.configIni.init(self.configIni)
                            shutil.move(new_file, self.configIni.audioPath)
                            deleteIsiFolder(self.temp)
                            print(f'\nConverter : Berhasil, kamu bisa melihat hasil nya di "' + self.configIni.audioPath + '"')
                            bar.finish()
                            
                        else:
                            deleteIsiFolder(self.temp)
                            print(f'\nConverter : (ERROR) Gagal, file audio tidak ada')

                    except Exception:
                        deleteIsiFolder(self.temp)
                        print(f'\nConverter : (ERROR) Terjadi ke gagalan, ini bisa terjadi karena file config.ini hilang atau terdapat file yang sama pada folder output')
                        
                except Exception:
                    print('\nConverter : (ERROR) Gagal pada mendownload file audio')

            except Exception:
                print('\nConverter : (ERROR) Gagal pada saat mengekstrak audio')
                
        except Exception:
            print('\nConverter : (ERROR) Gagal, Url tidak valid')

        

        

        