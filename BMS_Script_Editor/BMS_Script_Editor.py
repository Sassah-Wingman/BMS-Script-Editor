from gc import disable
from turtle import heading
from weakref import finalize
import PySimpleGUI as sg
import os.path
import sys
import mmap, re
import warnings

__version__ = "1.0.0"

sg.theme("GrayGrayGray")
#sg.main_sdk_help()


def get_function_list():
   function_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Functions.txt") as file_functions:
      function_list=file_functions.readlines()
      function_list.sort()
   return function_list

def get_callback_list():
   callback_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Callback_List.txt") as file_callbacks:
      callback_list=file_callbacks.readlines()
      callback_list.sort()
   return callback_list

def get_color_list():
   color_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Colors.txt") as file_colors:
      color_list=file_colors.readlines()
      color_list.sort()
   return color_list

merged_color_callback = (get_color_list() + get_callback_list())

def editor_window():
    header = [sg.Text("Functions", pad=(0,0), size = (15, 1), justification = "center"),
              sg.Text("Parameter 1", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 2", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 3", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 4", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 5", pad=(0,0), size = (20, 1), justification = "center"),
              sg.Text("Parameter 6", pad=(0,0), size = (20, 1), justification = "center"),]

    layout = [header]
     
    for row in range (0, 20):
        current_row = [sg.Combo(values = get_function_list(), size = (15, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = merged_color_callback, size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = get_callback_list(), size = (20, 1), pad = (0, 0), key = (row, 0)), 
                       sg.Combo(values = get_callback_list(), size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = get_callback_list(), size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = get_callback_list(), size = (20, 1), pad = (0, 0), key = (row, 0)),
                       sg.Combo(values = get_callback_list(), size = (20, 1), pad = (0, 0), key = (row, 0)),]

        layout.append(current_row)
        
    button_row = [sg.Button("Edit"), sg.Button("Clear"), sg.Button("Delete"), sg.Button("Close")]
    
    layout.append(button_row)
    
    color_row = [[sg.HorizontalSeparator()],
                 [sg.Button("0xFFFF0000", tooltip="Red.", size=(10,2), button_color = ("White", "Red"), key="-RED-"),
                 sg.Button("0x00FFFF00", tooltip="Yellow.", size=(10,2), button_color = ("Black", "Yellow"), key="-YELLOW-") ,
                 sg.Button("0x0000FFFF", tooltip="Cyan.", size=(10,2), button_color = ("Black", "Cyan"), key="-CYAN-"),
                 sg.Button("0x00FF00FF", tooltip="Magenta.", size=(10,2), button_color = ("White", "Magenta"), key="-MAGENTA-"),
                 sg.Button("0xFF00FF00", tooltip="Green.", size=(10,2), button_color = ("White", "Green"), key="-GREEN-"),
                 sg.Button("0xFFFFFFFF", tooltip="Black.", size=(10,2), button_color = ("White", "Black"), key="-BLACK-")],
                [sg.HorizontalSeparator()],
                [sg.Text("Remarks:"), sg.Text(" ", key = "-RMK-")],]
    
    layout.append(color_row)
    
    editor_window = sg.Window("Editor Window", layout)
    
    while True:
        event, values = editor_window.read()
        if event in (sg.WIN_CLOSED, "Close"):
            break
        if event == "-RED-":
            editor_window["-RMK-"].update("Red!")
        if event == "-YELLOW-":
            editor_window["-RMK-"].update("Yellow!")
        if event == "-CYAN-":
            editor_window["-RMK-"].update("Cyan!")
        if event == "-Magenta-":
            editor_window["-RMK-"].update("Magenta!")
        if event == "-GREEN-":
            editor_window["-RMK-"].update("Green!")
        if event == "-BLACK-":
            editor_window["-RMK-"].update("Black!")    
        # if event == 'SaveSettings':
        #     filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
        #     window.SaveToDisk(filename)
        #     # save(values)
         # elif event == 'LoadSettings':
         #    filename = sg.popup_get_file('Load Settings', no_window=True)
         #    window.LoadFromDisk(filename)
         #    # load(form)

               
    editor_window.close()
    return editor_window

    
def table_window():
    find_tooltip = "TODO."
   
    data = [["WaitTime",30, 2.0, " "], ["SetCursor", 60, " ", 0.05], ["SetColor", "000F000F", " ", " "]]
    #data = [["-TEXT-"]]
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
                    [sg.Button(button_text = "Close", key="-CLOSE_TABLE-", size = (10, 1), font="_ 12")],]

    layout = [[table_window], [table_buttons]]


    table_window = sg.Window("Script Table", layout, size = (700, 600), resizable=True)

    while True:
      event, values = table_window.read()
      print(event, values)
      if event in (sg.WIN_CLOSED, "-CLOSE_TABLE-"):
        print (event)
        break
    table_window.close()
    return table_window
   

def make_window(): 
    
    find_tooltip = "TODO."
    
    browse_line = [[sg.Text("Scripts Data Folder",  font="_ 16")],
                   [sg.Input(size=(40, 1), enable_events=True,  key="-FOLDER-"), sg.FolderBrowse(enable_events=True)],
                   #[sg.Combo(sg.user_settings_get_entry("-filenames-", []), default_value=sg.user_settings_get_entry("-last filename-", " "), size = (50/1), key= "-FOLDER-"), sg.FolderBrowse()],
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
                     sg.Button(button_text = "New", key = "-NEW-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Delete", key = "-DEL-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Quit", key = "-QUIT-", size = (10, 1), font="_ 12"),
                     sg.Button(button_text = "Show Table", key = "-TABLE-", size = (10, 1), font="_ 12")],]
    
    checkbox_line = [[sg.Text(" ")],
                    [sg.Radio("Show TXT Only", "RADIO1", enable_events=True, default=False, key = "-TXT-", circle_color="darkblue", tooltip = "Show only txt extention."), 
                     sg.Radio("Show RUN Only", "RADIO1", default =  False, key = "-RUN-", circle_color="darkblue",  tooltip = "Show only run extention."),
                     sg.Radio("Show TXT and RUN Files", "RADIO1", default =  True, key = "-ALL-", circle_color="darkblue",  tooltip = "Show run and txt extentions.")],
                    [sg.Text("TXT scripts are used with Tactical Engagement missions (*.TAC) and can be disabled before flight.")],
                    [sg.Text("RUN scripts are used in TRAINING missions (*.TRN) and cannot be disabled by players.")],
                     sg.Button(button_text = "Version", key = "-VER-"),]
        

    layout = [[browse_line], [left_col, right_col], [buttons_line], [checkbox_line]]
              
    window = sg.Window("BMS Script Editor", layout, finalize=True, resizable=True, size = (800, 800))
   
    return window

def main():
 
    window = make_window()
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            print (event)
            break
        if event == "-VER-":
            sg.popup_scrolled(sg.get_versions())
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
                print (contents)
        if event == "-OPEN-":
            print (["-TEXT-"])
        if event == "-NEW-":
            editor_window()
        if event == "-DEL-":
            pass
        if event == "-TABLE-":
            table_window()

                        
            
    window.close()
    
main()
        