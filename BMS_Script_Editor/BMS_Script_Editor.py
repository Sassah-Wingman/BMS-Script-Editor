from turtle import heading
from weakref import finalize
import PySimpleGUI as sg
import os.path
import sys
import mmap, re
import warnings

__version__ = "1.0.0"

#sg.main_sdk_help()


def get_function_list():
   Function_List=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Functions.txt") as file_functions:
      Function_List=file_functions.readlines()
      Function_List.sort()
   return Function_List


def prototipe_window():
    header = [sg.Text("Command", pad=(0,0), size = (15, 1), justification = "center"),
              sg.Text("Parameter 1", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 2", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 3", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 4", pad=(0,0), size = (20, 1), justification = "center"),
             ]
    
    layout = [header]

    
  
    command_names = ("SetTime\n", "WaiTime\n", "SetColor\n", "EndLine\n")
    
    for row in range (0, 5):
        current_row = [sg.Combo(values = get_function_list(), size = (15, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = command_names, size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = command_names, size = (20, 1), pad = (0, 0), key = (row, 0)), 
                       sg.Combo(values = command_names, size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = command_names, size = (20, 1), pad = (0, 0), key = (row, 0)),
                      ]
        layout.append(current_row)
        
    button_row = [sg.Button("Edit"), sg.Button("Clear"), sg.Button("Delete"), sg.Button("Close")]
    
    layout.append(button_row)
    
    prototipe_window = sg.Window("Prototipe Window", layout)
    
    while True:
        event, values = prototipe_window.read()
        if event in (sg.WIN_CLOSED, "Close"):
            break
           
                
    prototipe_window.close()
    return prototipe_window

    
def editor_window():
    find_tooltip = "TODO."
   
    data = [["WaitTime", 30, 2.0, " "], ["SetCursor", 60, " ", 0.05], ["SetColor", "000F000F", " ", " "]]
    table_window = [[sg.Table(values=data, headings=["Command", "Parameter 1", "Parameter 2", "Parameter 3"], 
                        def_col_width = 30,
                        text_color="Dark Blue",
                        num_rows=20,
                        justification="center",
                        alternating_row_color='lightblue',
                        selected_row_colors='red on white',
                        display_row_numbers = True, 
                        expand_x=True)],]

    table_buttons = [[sg.Text(" ")],
                    [sg.HorizontalSeparator()],
                    [sg.Text(" ")],
                    [sg.Button(button_text = "Edit", key="-EDIT_TABLE-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Save", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Delete", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Close", key="-CLOSE_TABLE-", size = (10, 1), font="_ 12")],]

    layout = [[table_window], [table_buttons]]


    editor_window = sg.Window("Script Editor", layout, size = (600, 600), resizable=True)

    while True:
      event, values = editor_window.read()
      print(event, values)
      if event in (sg.WIN_CLOSED, "-CLOSE_TABLE-"):
        print (event)
        break
        
      elif event == "-EDIT_TABLE-":
        prototipe_window()
    editor_window.close()
    return editor_window
   

def make_window(): 
    
    find_tooltip = "TODO."
    
    browse_line = [[sg.Text("Scripts Data Folder",  font="_ 16")],
                   [sg.Input(size=(40, 1), enable_events=True,  key="-FOLDER-"), sg.FolderBrowse(enable_events=True)],
                   [sg.Text(" ")],
                   [sg.HorizontalSeparator()],]
                 
   
    left_col = sg.Column([[sg.Text("List of Files:")],
                          [sg.Listbox(values=[], enable_events=True, size=(20,20), key="-FILE_LIST-", expand_x=True, expand_y=True)],], 
                           element_justification = "Left", expand_x = True, expand_y = False)
          
    right_col = sg.Column([[sg.Text("File Name: ", key = "-TOUT-")],
                          [sg.Multiline(size=(30,24), key="-TEXT-", expand_x=True, expand_y=False)],], 
                           element_justification = "Left", expand_x = True, expand_y=False)
     
    buttons_line = [[sg.Text(" ")],
                    [sg.HorizontalSeparator()],
                    [sg.Text(" ")],
                    [sg.Button(button_text = "Open", key = "-OPEN-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Delete", key = "-DEL-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Quit", key = "-QUIT-", size = (10, 1), font="_ 12")],]
    
    checkbox_line = [[sg.Text(" ")],
                    [sg.Radio("Show TXT Only", "RADIO1", enable_events=True, default=False, key = "-TXT-", circle_color="darkblue", tooltip = "Show only txt extention."), 
                     sg.Radio("Show RUN Only", "RADIO1", default =  False, key = "-RUN-", circle_color="darkblue",  tooltip = "Show only run extention."),
                     sg.Radio("Show TXT and RUN Files", "RADIO1", default =  True, key = "-ALL-", circle_color="darkblue",  tooltip = "Show run and txt extentions.")],
                    [sg.Text("TXT scripts are used with Tactical Engagement missions (*.TAC) and can be disabled before flight.")],
                    [sg.Text("RUN scripts are used in TRAINING missions (*.TRN) and cannot be disabled by players.")],]
        

    layout = [[browse_line], [left_col, right_col], [buttons_line], [checkbox_line]]
              
    window = sg.Window("BMS Script Editor", layout, finalize=True, resizable=True, size = (800, 800))
   
    return window

def main():
 
    window = make_window()
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            sg.popup_ok("We are done here.  Thanks!", line_width=30,  no_titlebar=True, keep_on_top=True)
            print (event)
            break
        if event == "-OPEN-":
            editor_window()
        if event == "-FOLDER-":
            folder_location = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder_location)
            except:
                file_list = []
            if values ["-TXT-"] == True:    
                file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt"))]
                window["-FILE_LIST-"].update(file_names)
            elif values ["-RUN-"] ==  True:   
                file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".run"))]
                window["-FILE_LIST-"].update(file_names)
            else:  
                file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
                window["-FILE_LIST-"].update(file_names)
        elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) > 0:
            file_selection = values["-FILE_LIST-"] [0]
            with open(os.path.join(folder_location, file_selection)) as file:
                contents=file.read()
                window["-TOUT-"].update(os.path.join(folder_location, file_selection))
                window["-TEXT-"].update(contents)
        
            

                        
            
    window.close()
    
main()
        