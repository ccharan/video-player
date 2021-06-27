# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import PySimpleGUI as sg
import os.path
import vlc

file_list_column = [
    [
         sg.Text("Video Folder"), 
         sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse()
    ],  
    [
          sg.Listbox(
              values=[], enable_events=True, size=(40,20),background_color="GREY",
              key='-FILE LIST-'
          )
    ],
    
    [
     sg.Button("STOP", enable_events=True, change_submits=True,key = '-CLOSE VIDEO-', button_color = 'RED'),
     sg.Button("PAUSE/RESUME", enable_events=True, change_submits=True,key = '-PAUSE VIDEO-', button_color = 'GREEN')

               
    ]


]

window = sg.Window(title="Video Player", layout=file_list_column, margins=(20,10))


count = 0
video = None
while True:
    event, values = window.read()
    
    if event == 'EXIT' or event  == sg.WIN_CLOSED:
        break
    
    if event == '-FOLDER-':
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".mp4", ".mkv"))
                
        ]
        
        window["-FILE LIST-"].update(fnames)
        
    if event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values['-FOLDER-'], values["-FILE LIST-"][0]    
            )
            
            count += 1 

            if count > 1:
                video.stop()
                count = 1
            
            print("count->",count)
            video = vlc.MediaPlayer(filename)
            print(video.play())
            
        except BaseException as e:
            print(e)

    if event == '-CLOSE VIDEO-':
        video.stop()
       
    if event == '-PAUSE VIDEO-':
        video.pause()
window.close()
