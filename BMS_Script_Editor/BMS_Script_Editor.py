# This is a application designed to edit scripts for Falcon BMS 
# using Pysimplegui 3.17.
# Sao Paulo, Brazil
# Dec 2023
#__version__ = "1.0.2 - Feb 2024"

import PySimpleGUI as sg
import os
import sys

sg.theme("GrayGrayGray")

# get list of BMS SCRIPT FUNCTIONS to be displayed in Combo
def get_function_list():
   function_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Functions.txt") as file_functions:
   #with open("G:/Other computers/My Computer/repos/BMS_Script_Editor/Functions.txt") as file_functions:   
      function_list=file_functions.readlines()
      function_list.sort()
   return function_list

# get list of BMS CALLBACKS to be displayed in Combo
def get_callback_list():
   callback_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Callback_List.txt") as file_callbacks:
   #with open("G:/Other computers/My Computer/repos/BMS_Script_Editor/Callback_List.txt") as file_callbacks:   
      callback_list=file_callbacks.readlines()
      callback_list.sort()
   return callback_list

# get list of SCRIPT COLORS to be displayed in Combo
def get_color_list():
   color_list=[]
   with open("C:/Users/gsmei/source/repos/BMS_Script_Editor/Colors.txt") as file_colors:
   #with open("G:/Other computers/My Computer/repos/BMS_Script_Editor/Colors.txt") as file_colors:   
      color_list=file_colors.readlines()
      color_list.sort()
   return color_list

merged_color_callback = (get_color_list() + get_callback_list())

#manipulates the script adding, editing or deleting lines 
def script_manipulation_form(script_list):
    find_tooltip = "TODO."
    list_of_script_parameters = script_list
    headings = ["Function", "Parameter 1", "Parameter 2", "Parameter 3", "Parameter 4", "Parameter 5"]
    layout = [[sg.Text("Function:"), sg.Combo(values = get_function_list(),  key="-FUNC-")],
              [sg.Text("Parameter 1:"), sg.Combo(values = merged_color_callback, key="-PAR1-")],
              [sg.Text("Parameter 2:"), sg.Combo(values = merged_color_callback, key="-PAR2-")],
              [sg.Text("Parameter 3:"), sg.Input(key="-PAR3-", do_not_clear=False)],
              [sg.Text("Parameter 4:"), sg.Input(key="-PAR4-", do_not_clear=False)],
              [sg.Text("Parameter 5:"), sg.Input(key="-PAR5-", do_not_clear=False)],
              [sg.Button("Add Line", key = "-ADD-"), 
               sg.Button("Edit Line", key = "-EDIT-"),
               sg.Button("Save Edition", key = "-SAED-", disabled=True),
               sg.Button("Delete Line", key = "-DEL-"), 
               sg.Button("Save File", key = "-SAVE-")],
              [sg.Table(list_of_script_parameters, headings, 
                        num_rows = 20, 
                        display_row_numbers = True, 
                        background_color = "gray", 
                        alternating_row_color = "light gray",
                        text_color = "Black",
                        selected_row_colors = ("white", "blue"),
                        justification = "left", 
                        key = "-TABLE-")],]
    
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
    
    manipulation_window = sg.Window("Script Form", layout, resizable=True, modal = True)
    
    while True:
        event, values = manipulation_window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED:
            break
        
        # routine to add single line to a script text
        if event == "-ADD-":
            #store values filled in the form to a list
            list_of_script_parameters.append([values["-FUNC-"], 
                                    values["-PAR1-"], 
                                    values["-PAR2-"], 
                                    values["-PAR3-"], 
                                    values["-PAR4-"], 
                                    values["-PAR5-"]])
            manipulation_window["-TABLE-"].update(values=list_of_script_parameters)
            #clear form of previous inputs
            manipulation_window["-FUNC-"].update([])
            manipulation_window["-PAR1-"].update([])
            manipulation_window["-PAR2-"].update([])
            #remove "\n" symbol from all lists in the list, generated from append.values
            adjusted_list_of_script_parameters = []
            for _list in list_of_script_parameters:
                for _string in _list:
                    _list=[_string.strip() for _string in _list]
                adjusted_list_of_script_parameters.append(_list)
        
        #routine to edit and save a edited line          
        if event == "-EDIT-":
            if values["-TABLE-"]==[]:
                sg.popup("No row selected!")
            else:
                edit_row = values["-TABLE-"][0]
                sg.popup("Edit selected row!")
                manipulation_window["-FUNC-"].update(value=list_of_script_parameters[edit_row][0])
                manipulation_window["-PAR1-"].update(value=list_of_script_parameters[edit_row][1])
                manipulation_window["-PAR2-"].update(value=list_of_script_parameters[edit_row][2])
                manipulation_window["-PAR3-"].update(value=list_of_script_parameters[edit_row][3])
                manipulation_window["-PAR4-"].update(value=list_of_script_parameters[edit_row][4])
                manipulation_window["-PAR5-"].update(value=list_of_script_parameters[edit_row][5])
                manipulation_window["-SAED-"].update(disabled=False)
        if event == "-SAED-":
            list_of_script_parameters[edit_row]=[values["-FUNC-"], 
                                                          values["-PAR1-"], 
                                                          values["-PAR2-"], 
                                                          values["-PAR3-"], 
                                                          values["-PAR4-"], 
                                                          values["-PAR5-"]]
            manipulation_window["-TABLE-"].update(values=list_of_script_parameters)
            manipulation_window["-FUNC-"].update(value=" ")
            manipulation_window["-PAR1-"].update(value=" ")
            manipulation_window["-PAR2-"].update(value=" ")
            manipulation_window["-PAR3-"].update(value=" ")
            manipulation_window["-PAR4-"].update(value=" ")
            manipulation_window["-PAR5-"].update(value=" ")
            manipulation_window["-SAED-"].update(disabled=True)
            #remove "\n" symbol from all lists in the list, generated from append.values
            adjusted_list_of_script_parameters = []
            for _list in list_of_script_parameters:
                for _string in _list:
                    _list=[_string.strip() for _string in _list]
                adjusted_list_of_script_parameters.append(_list)

        #routine to delete script lines
        if event == "-DEL-":
            if values["-TABLE-"]==[]:
                sg.popup("No row selected!")
            else:
                sg.popup("Once deleted, the line can't be restored! Continue?")
                del list_of_script_parameters[values["-TABLE-"][0]]
                manipulation_window["-TABLE-"].update(values=list_of_script_parameters)
                adjusted_list_of_script_parameters = []
            for _list in list_of_script_parameters:
                for _string in _list:
                    _list=[_string.strip() for _string in _list]
                adjusted_list_of_script_parameters.append(_list)

        #routine to save a script text file in BMS folder
        if event == "-SAVE-":
            file_to_save_name=sg.popup_get_file(message="Save",
                                                title="Save New File", 
                                                default_extension="*.txt",
                                                file_types=(("TXT Files", "*.txt")),
                                                history=True,
                                                keep_on_top=True, 
                                                modal=True,
                                                save_as=True)
            with open (file_to_save_name, "w") as new_file_to_save:
                for _list in adjusted_list_of_script_parameters:
                  for _string in _list:
                      new_file_to_save.write(str(_string) + " ")
                  new_file_to_save.write("\n")
            manipulation_window.close()

        # routine that show color names in buttons         
        if event == "-RED-":
            manipulation_window["-RMK-"].update("Red!")
        if event == "-YELLOW-":
            manipulation_window["-RMK-"].update("Yellow!")
        if event == "-CYAN-":
            manipulation_window["-RMK-"].update("Cyan!")
        if event == "-MAGENTA-":
            manipulation_window["-RMK-"].update("Magenta!")
        if event == "-GREEN-":
            manipulation_window["-RMK-"].update("Green!")
        if event == "-BLACK-":
            manipulation_window["-RMK-"].update("Black!") 
    
    return manipulation_window

#make main window
def make_window(): 
    
    find_tooltip = "TODO."
    
    browse_line = [[sg.Text("Scripts Data Folder",  font="_ 16")],
                   [sg.Input(size=(40, 1), enable_events=True,  key="-FOLDER-"), sg.FolderBrowse(enable_events=True)],
                   [sg.Text(" ")],
                   [sg.HorizontalSeparator()],]
   
    left_col = sg.Column([[sg.Text("List of Files:")],
                          [sg.Listbox(values=[], enable_events=True, size=(20,20), key="-FILE_LIST-", expand_x=True, expand_y=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],], 
                           element_justification = "Left", expand_x = True, expand_y = False)
          
    right_col = sg.Column([[sg.Text("File Name: ", key = "-TOUT-")],
                          [sg.Multiline(size=(30,24), key="-TEXT-", expand_x=True, expand_y=False, disabled=True, do_not_clear=False)],], 
                           element_justification = "Left", expand_x = True, expand_y=False)
     
    buttons_line = [[sg.Text(" ")],
                    [sg.HorizontalSeparator()],
                    [sg.Text(" ")],
                    [sg.Button(button_text = "Open Script", key = "-OPEN_S-", size = (12, 1), font="_ 12"),
                     sg.Button(button_text = "New Script", key = "-NEW_S-", size = (12, 1), font="_ 12"),
                     sg.Button(button_text = "Delete Script", key = "-DEL_S-", size = (12, 1), font="_ 12"),
                     sg.Button(button_text = "Quit", key = "-QUIT_S-", size = (12, 1), font="_ 12")]]
    
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

#entrance of the program
def main():
 
    window = make_window()
    while True:
        event, values = window.read()
        #print(event, values)
        
        #close window and terminate application
        if event in (sg.WIN_CLOSED, "-QUIT_S-"):
            #print (event)
            break
        
        #show python version
        if event == "-VER-":
            sg.popup_ok("Version 1.0.2", modal = True, keep_on_top=True)
            
        #routine to pick work folder and to show files    
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
            with open(os.path.join(folder_location, file_selection)) as file_to_read:
                contents=file_to_read.read()
                window["-TOUT-"].update(os.path.join(folder_location, file_selection))
                window["-TEXT-"].update(contents)
         
        #routine to open a script file
        if event == "-OPEN_S-":
            #select a file to open from a list
            opened_script_list = [] 
            file_selection=values["-FILE_LIST-"][0]
            file_to_open = os.path.join(folder_location, file_selection)
            with open (file_to_open) as _file_:   
              opened_script_list=_file_.readlines()
            #print(opened_script_list)
            #turn a list in a list of lists
            _list1 = []
            for _el1 in opened_script_list:
                sub1=_el1.split(",")
                _list1.append(sub1)
            #print(_list1)
            # turn each sub list of strings, dealing with comments and texts
            _list2 = []
            for _list_ in _list1:
                for _str_ in _list_:
                   if (_str_.find("//")!=-1) or (_str_.find("\"")!=-1):
                       temp_list_a=[]
                       temp_list_a.append(_str_)
                       _list2.append(temp_list_a)
                   else:
                       _str_=_str_.strip(" ")
                       sub2=_str_.split(" ")
                       _list2.append(sub2)
            #print(_list2)
            #convert each sub list to 6 itens string lists to fit in table
            _list3 = []
            size = 5
            for lst in _list2:
                while len(lst) <= size:
                    lst.append(" ")
                _list3.append(lst)
            #print(_list3)
            script_manipulation_form(_list3)
     
        #routine to create a new script file    
        if event == "-NEW_S-":
            empty_script_list=[]
            script_manipulation_form(empty_script_list)
            file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
            window["-FILE_LIST-"].update(file_names)
            window["-TOUT-"].update(" ")
            window["-TEXT-"].update(" ")
         
        #routine to delete a script file    
        if event == "-DEL_S-":
             if values["-FILE_LIST-"]==[]:
                sg.popup("No script file selected!")
             elif sg.popup("Once deleted, the file can't be restored! Continue?"):
                file_selection=values["-FILE_LIST-"][0]
                file_to_delete = os.path.join(folder_location, file_selection)
                os.remove(file_to_delete)
                file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
                window["-FILE_LIST-"].update(file_names)
                window["-TOUT-"].update(" ")
                window["-TEXT-"].update(" ")
            
    window.close()
    
main()
        