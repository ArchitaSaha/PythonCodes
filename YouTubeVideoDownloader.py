from pytube import YouTube
from tkinter import *
# from tkinter import ttk

def showDetails(yt):
    print("-----------------------------------------------")
    print("---------------- VIDEO DETAILS ----------------")
    print("-----------------------------------------------")
    print('Title : ', yt.title)
    # print('Description : ', yt.description)
    # print('Publish Date : ', yt._publish_date)
    # print('Captions : ', yt.captions)
    # print('Caption Tracks : ', yt.caption_tracks)
    # print('Video Information : ', yt._vid_info)
    print('Author : ', yt.author)
    print('Channel Link : ', yt.channel_url)
    print('Video Duration : ', yt.length)
    print('Total Views : ', yt.views)
    # print('Rating : ', yt.rating)
    print("-----------------------------------------------")

def downloadVideoHighestResolution(yt):
    print("Download started ...")
    yt.streams.get_highest_resolution().download()
    print("Download completed ...")

def downloadVideoLowestResolution(yt):
    print("Download started ...")
    yt.streams.get_lowest_resolution().download()
    print("Download completed ...")

def downloadVideoByResolution(yt, resolution):
    print("Download started ...")
    yt.streams.filter(res=resolution).first().download()
    print("Download completed ...")

def getVideoResolutions(yt):
    resolution = set([stream.resolution for stream in yt.streams])
    resolution.remove(None)
    return list(sorted(resolution, key = lambda x: int(x[:-1])))

if __name__ == "__main__":
    window = Tk()
    window.configure(bg="white")
    window.geometry("600x550")
    window.title("Rolling The Dices Game")
    window.resizable(0, 0)
    # roll_button = Button(window, text="Roll!", width=10, height=2, font=15, bg="white", bd=2, command=rollDiceDigital)
    # roll_button.pack(padx=10, pady=15)
    text = Entry(window).grid(row=0, column=1)
    label = Label(window, font=("times", 250), bg="black", fg="white")
    window.mainloop()

    link = input("Enter video link : ")
    yt = YouTube(link)

    # Display Video Details
    showDetails(yt)

    # Download video with the highest resolution
    # downloadVideoHighestResolution(yt)

    # Download video with the lowest resolution
    # downloadVideoLowestResolution(yt)

    # Get available video resolutions
    print(getVideoResolutions(yt))

    resolution = input('Enter desired resolution : ')

    # Download video by resolution
    downloadVideoByResolution(yt, resolution)