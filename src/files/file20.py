Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import os, sys
from pytube import YouTube

def main():
    links=list()
    # Example usage
    link = input(f'\n {Wh}target video URL: {Gr}')
    links.append(link)
    if len(links) == 0:
        print(f" {Re}!There are no urls available!")
        sys.exit()

    for link in links:
        url = link.strip()
        #check if the os is windows/macOS it save all videos in videos folder
        if os.name == 'nt' or os.name == 'posix':
            output_path = ""
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, resolution="720p").filter(only_audio=False).first()
            # Try to find a 720p video with audio
            if not stream:
                stream = yt.streams.filter(progressive=True, resolution="480p").filter(only_audio=False).first()
            # If no 480p video found, try 360p
            elif not stream:
                stream = yt.streams.filter(progressive=True, resolution="360p").filter(only_audio=False).first()
            # Download the stream
            if stream:
                print(f"\n{Gr} Please wait downloading..")
                stream.download(output_path)
                print(f"{Gr} Download Completed {output_path}\n")
            else:
                print(f"{Re} !Couldn't find video!\n")
        #if the os is linux/termux it save all videos in Download/YT_Downloader folder
        else:
            output_path = ""
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, resolution="720p").filter(only_audio=False).first()
            # Try to find a 720p video with audio
            if not stream:
                stream = yt.streams.filter(progressive=True, resolution="480p").filter(only_audio=False).first()
            # If no 480p video found, try 360p
            elif not stream:
                stream = yt.streams.filter(progressive=True, resolution="360p").filter(only_audio=False).first()
            # Download the stream
            if stream:
                print(f"{Gr} Please wait downloading..")
                stream.download(output_path)
                print(f"{Gr} Download Completed - {output_path}\n")
            else:
                print(f"{Re} !Couldn't find video!\n")
    print(f"{Gr} Video Downloaded Complete")