# This is a application designed to edit scripts for Falcon BMS 
# using Pysimplegui 3.17.
# Sao Paulo, Brazil
# Dec 2023
#__version__ = "1.24.2 - mar 2024"

import PySimpleGUI as sg
import os
import sys

version = "1.24.2"

sg.theme("GrayGrayGray")

#get list of BMS SCRIPT FUNCTIONS to be displayed in sg.Combo
def get_list_of_functions():
   list_of_functions = []
   try:
       with open("Functions_List.txt") as text_file_with_functions:
           list_of_functions = text_file_with_functions.readlines()
           list_of_functions.sort() 
   except:
       sg.popup("Functions_List.txt is missing! Program will close!")
       print("Functions_List.txt not found!")
       sys.exit(0)
   return list_of_functions

#get list of BMS CALLBACKS to be displayed in sg.Combo
def get_list_of_callbacks():
   list_of_callbacks = []
   try:
       with open("Callbacks_List.txt") as text_file_with_callbacks:
           list_of_callbacks = text_file_with_callbacks.readlines()
           list_of_callbacks.sort()
   except:
       sg.popup("Callbacks_List.txt is missing! Program will close!")
       print("Callbacks_List.txt not found!")
       sys.exit(0)
   return list_of_callbacks

#get list of SCRIPT HEX COLORS to be displayed in sg.Combo
def get_list_of_colors():
   list_of_colors = []
   try:
       with open("Colors_List.txt") as text_file_with_colors:
           list_of_colors = text_file_with_colors.readlines()
           list_of_colors.sort()
   except:
       sg.popup("Colors_List.txt is missing! Program will close!")
       print("Colors_List.txt not found!")
       sys.exit(0)
   return list_of_colors

#remove all "\n" symbol generated from "append.values" within the sublists 
def remove_symbol_from_list (list_with_symbols):
    no_symbol_list = []
    for _list in list_with_symbols:
       for _string in _list:
          _list=[_string.strip() for _string in _list]
          no_symbol_list.append(_list)
       return no_symbol_list    
   
def display_folder_and_files(folder_location):
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


    #return a, b, c

#merge lists to be displayed in sg.Combo
merged_colors_callbacks = (get_list_of_colors() + get_list_of_callbacks())

#manipulates the script using a table, adding, editing or deleting lines 
def script_manipulation_form(list_to_manipulate):
    manipulation_window_tooltips = ["Script functions only.", 
                                    "color, callback, integer, float, string, time and section.", 
                                    "callback, float, string.",
                                    "integer and float.",
                                    "float.",
                                    "float.",
                                    "CRTL_L + A.", 
                                    "CRTL_L + E.", 
                                    "CRTL_L + S.", 
                                    "CRTL_L + D.",
                                    "CRTL_L + F.",
                                    "CRTL_L + C."] 

    list_of_script_parameters = list_to_manipulate
    headings = ["Function", "First Parameter", "Second Parameter", "Third Parameter", "Forth Parameter", "Fifth Parameter"]
    layout = [[sg.Text("Function:"), 
               sg.Combo(values = get_list_of_functions(),  
                        default_value = "//",
                        readonly = True,
                        auto_size_text = True,
                        key="-FUNC-", 
                        tooltip = manipulation_window_tooltips[0])],
              [sg.Text(headings[1]), sg.Combo(values = merged_colors_callbacks, key = "-PAR1-", auto_size_text = True, tooltip = manipulation_window_tooltips[1])],
              [sg.Text(headings[2]), sg.Combo(values = merged_colors_callbacks, key = "-PAR2-", auto_size_text = True, tooltip = manipulation_window_tooltips[2])],
              [sg.Text(headings[3]), sg.Input(key = "-PAR3-", do_not_clear = False, tooltip = manipulation_window_tooltips[3])],
              [sg.Text(headings[4]), sg.Input(key = "-PAR4-", do_not_clear = False, tooltip = manipulation_window_tooltips[4])],
              [sg.Text(headings[5]), sg.Input(key = "-PAR5-", do_not_clear = False, tooltip = manipulation_window_tooltips[5])],
              [sg.Button("Add Line", key = "-ADD-", tooltip = manipulation_window_tooltips[6]), 
               sg.Button("Edit Line", key = "-EDIT-", tooltip = manipulation_window_tooltips[7]),
               sg.Button("Save Edition", key = "-SAED-", tooltip = manipulation_window_tooltips[8], disabled = True),
               sg.Button("Delete Line", key = "-DEL-", tooltip = manipulation_window_tooltips[9]),
               sg.Text("                           "),
               sg.Button("Save File", key = "-SAVE-", tooltip = manipulation_window_tooltips[10]),
               sg.Text("                           "),
               sg.Button("Close Window", key = "-CLOSE-", tooltip = manipulation_window_tooltips[11])],
              [sg.Table(list_of_script_parameters,
                        headings,
                        expand_x = True,
                        auto_size_columns = True,
                        header_text_color = "Blue",
                        header_font = ("Arial", 14),
                        num_rows = 20,
                        font = ("Arial", 10),
                        display_row_numbers = True,
                        background_color = "gray", 
                        alternating_row_color = "light gray",
                        text_color = "Black",
                        selected_row_colors = ("white", "blue"),
                        justification = "left", 
                        key = "-TABLE-")],]
    
    color_row = [[sg.HorizontalSeparator()],
                 [sg.Button("0xFFFF0000", tooltip = "Red.", size = (10,2), button_color = ("White", "Red"), key = "-RED-"),
                 sg.Button("0x00FFFF00", tooltip = "Yellow.", size = (10,2), button_color = ("Black", "Yellow"), key = "-YELLOW-") ,
                 sg.Button("0x0000FFFF", tooltip = "Cyan.", size = (10,2), button_color = ("Black", "Cyan"), key = "-CYAN-"),
                 sg.Button("0x00FF00FF", tooltip = "Magenta.", size = (10,2), button_color = ("White", "Magenta"), key = "-MAGENTA-"),
                 sg.Button("0xFF00FF00", tooltip = "Green.", size = (10,2), button_color = ("White", "Green"), key = "-GREEN-"),
                 sg.Button("0xFFFFFFFF", tooltip = "Black.", size = (10,2), button_color = ("White", "Black"), key = "-BLACK-")],
                [sg.HorizontalSeparator()],
                [sg.Text("Remarks:"), sg.Text(" ", key = "-RMK-")],]
    
    layout.append(color_row)
    
    manipulation_window = sg.Window("Script Form", layout, resizable = True, size = (1200, 700), modal = True, finalize = True)
    
    manipulation_window["-FUNC-"].set_focus()
    manipulation_window.bind("<Control_L><a>", "Add Line")
    manipulation_window.bind("<Control_L><e>", "Edit Line")
    manipulation_window.bind("<Control_L><s>", "Save Edition")
    manipulation_window.bind("<Control_L><d>", "Delete Line")
    manipulation_window.bind("<Control_L><f>", "Save File")
    manipulation_window.bind("<Control_L><c>", "Close Window")
    
    while True:
        event, values = manipulation_window.read()
        #print(event, values)
        if event in (sg.WIN_CLOSED, "-CLOSE-", "Close Window"):
            break
        
        # routine to add single line to a script text
        if event in("-ADD-", "Add Line"):
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
            adjusted_list_of_script_parameters = remove_symbol_from_list (list_of_script_parameters)
        
        #routine to edit and save a edited line          
        if event in ("-EDIT-", "Edit Line"):
            if values["-TABLE-"] == []:
                sg.popup("No row selected!")
            else:
                edit_row = values["-TABLE-"][0]
                manipulation_window["-FUNC-"].update(value=list_of_script_parameters[edit_row][0])
                manipulation_window["-PAR1-"].update(value=list_of_script_parameters[edit_row][1])
                manipulation_window["-PAR2-"].update(value=list_of_script_parameters[edit_row][2])
                manipulation_window["-PAR3-"].update(value=list_of_script_parameters[edit_row][3])
                manipulation_window["-PAR4-"].update(value=list_of_script_parameters[edit_row][4])
                manipulation_window["-PAR5-"].update(value=list_of_script_parameters[edit_row][5])
                manipulation_window["-SAED-"].update(disabled=False)
        if event in ("-SAED-", "Save Edition"):
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
            adjusted_list_of_script_parameters = remove_symbol_from_list (list_of_script_parameters)
          
            

        #routine to delete script lines
        if event in("-DEL-", "Delete Line"):
            if values["-TABLE-"] == []:
                sg.popup("You must select a row to delete!", no_titlebar = True, any_key_closes = True, keep_on_top = True, modal = True)
            else:
                if sg.popup_ok_cancel("Once deleted, the line can't be restored! Continue?", no_titlebar = True, keep_on_top = True,  modal = True) == "OK":
                    del list_of_script_parameters[values["-TABLE-"][0]]
                    manipulation_window["-TABLE-"].update(values=list_of_script_parameters)
                    adjusted_list_of_script_parameters = remove_symbol_from_list (list_of_script_parameters)
                   
        #routine to save a script text file in BMS folder
        if event in ("-SAVE-", "Save File"):
            file_to_save_name=sg.popup_get_file(message = "Save",
                                                title = "Save New File", 
                                                default_extension = "*.txt",
                                                file_types = (("TXT Files", "*.txt")),
                                                history = True,
                                                keep_on_top = True, 
                                                modal = True,
                                                save_as = True)
            with open(file_to_save_name, "w") as new_file_to_save_as_text:
                for _list in adjusted_list_of_script_parameters:
                  for _string in _list:
                      new_file_to_save_as_text.write(str(_string) + " ")
                  new_file_to_save_as_text.write("\n")
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
    
    manipulation_window.close()
    return manipulation_window

#make main window
def main_window(): 
    
    main_window_tooltips = ["CRTL_L + O.", 
                            "CRTL_L + N.",
                            "CRTL_L + D.",
                            "CRTL_L + Q.",
                            "Show only txt extention.",
                            "Show only run extention.",
                            "Show run and txt extentions.",
                            "CRTL_L + V.",]
    
    browse_line = [[sg.Text("Scripts Data Folder",  font = "_ 16")],
                   [sg.Input(size = (40, 1), enable_events = True,  key="-FOLDER-"), sg.FolderBrowse(enable_events = True)],
                   [sg.Text(" ")],
                   [sg.HorizontalSeparator()],]
   
    left_col = sg.Column([[sg.Text("List of Files:")],
                          [sg.Listbox(values = [], 
                                      enable_events = True, 
                                      size = (20,20), 
                                      key="-FILE_LIST-", 
                                      expand_x = True, 
                                      expand_y = True, 
                                      select_mode = sg.LISTBOX_SELECT_MODE_SINGLE)],], 
                           element_justification = "Left", expand_x = True, expand_y = False)
          
    right_col = sg.Column([[sg.Text("File Name: ", key = "-TOUT-")],
                          [sg.Multiline(size  =(30,24), 
                                        key = "-TEXT-", 
                                        expand_x = True, 
                                        expand_y = False, 
                                        disabled = True, 
                                        do_not_clear = False)],], 
                           element_justification = "Left", expand_x = True, expand_y=False)
     
    buttons_line = [[sg.Text(" ")],
                    [sg.HorizontalSeparator()],
                    [sg.Text(" ")],
                    [sg.Button(button_text = "Open Script", key = "-OPEN_S-", size = (12, 1), font = "_ 12", tooltip = main_window_tooltips[0]),
                     sg.Button(button_text = "New Script", key = "-NEW_S-", size = (12, 1), font = "_ 12", tooltip = main_window_tooltips[1]),
                     sg.Button(button_text = "Delete Script", key = "-DEL_S-", size = (12, 1), font = "_ 12", tooltip = main_window_tooltips[2]),
                     sg.Button(button_text = "Quit", key = "-QUIT_S-", size = (12, 1), font = "_ 12",  tooltip = main_window_tooltips[3])]]
    
    checkbox_line = [[sg.Text(" ")],
                    [sg.Radio("Show TXT Only", "RADIO1", enable_events=True, default=False, key = "-TXT-", circle_color="darkblue", tooltip = main_window_tooltips[4]), 
                     sg.Radio("Show RUN Only", "RADIO1", default =  False, key = "-RUN-", circle_color = "darkblue", tooltip = main_window_tooltips[5]),
                     sg.Radio("Show TXT and RUN Files", "RADIO1", default =  True, key = "-ALL-", circle_color = "darkblue", tooltip = main_window_tooltips[6])],
                    [sg.Text("TXT scripts are used with Tactical Engagement missions (*.TAC) and can be disabled before flight.")],
                    [sg.Text("RUN scripts are used in TRAINING missions (*.TRN) and cannot be disabled by players.")],
                     sg.Button(button_text = "Version", key = "-VER-", tooltip = main_window_tooltips[7]),]

    layout = [[browse_line], [left_col, right_col], [buttons_line], [checkbox_line]]
              
    main_window = sg.Window("BMS Script Editor", layout, finalize=True, resizable=True, size = (800, 800))
    
    main_window["-NEW_S-"].set_focus()
    main_window.bind("<Control_L><o>", "Open Script")
    main_window.bind("<Control_L><n>", "New Script")
    main_window.bind("<Control_L><d>", "Delete Scritp")
    main_window.bind("<Control_L><q>", "Quit")
    main_window.bind("<Control_L><v>", "Version")
   
    return main_window

#entrance of the program
def main():
 
    window = main_window()
    while True:
        event, values = window.read()
        
        #close window and terminate application
        if event in (sg.WIN_CLOSED, "-QUIT_S-", "Quit"):
            break
        
        #show python version
        if event in ("-VER-", "Version"):
            sg.popup_ok("BMS Script Editor version: ", version, no_titlebar = True, modal = True, keep_on_top=True)
            
        #select the folder and show files    
        if event == "-FOLDER-":
            display_folder_and_files(values["-FOLDER-"], values["-TXT-"], values["-RUN-"])

        #     folder_location = values["-FOLDER-"]
        #     try:
        #         file_list = os.listdir(folder_location)
        #     except:
        #         file_list = []
        #     if values ["-TXT-"] == True:    
        #         file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt"))]
        #         window["-FILE_LIST-"].update(file_names)
        #     elif values ["-RUN-"] ==  True:   
        #         file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".run"))]
        #         window["-FILE_LIST-"].update(file_names)
        #     else:  
        #         file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
        #         window["-FILE_LIST-"].update(file_names)
        # elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) > 0:
        #     file_selection = values["-FILE_LIST-"] [0]
        #     with open(os.path.join(folder_location, file_selection)) as file_to_read:
        #         contents=file_to_read.read()
        #         window["-TOUT-"].update(os.path.join(folder_location, file_selection))
        #         window["-TEXT-"].update(contents)
         
        #open a script file for edition
        if event in ("-OPEN_S-", "Open Script"):
            #select a file to open from a list
            opened_script_list = []
            file_selection=values["-FILE_LIST-"][0]
            file_to_open = os.path.join(folder_location, file_selection)
            with open (file_to_open) as _file_:   
              opened_script_list = _file_.readlines()
            #print(opened_script_list)
            #convert this list in a list of lists
            _list1 = []
            for _el1 in opened_script_list:
                sub1 = _el1.split(",")
                _list1.append(sub1)
            #print(_list1)
            # turn each sub list of strings, dealing with comments and texts
            _list2 = []
            for _list_ in _list1:
                for _str_ in _list_:
                   if (_str_.find("//") != -1) or (_str_.find("\"") != -1):
                       temp_list_a=[]
                       temp_list_a.append(_str_)
                       _list2.append(temp_list_a)
                   else:
                       _str_=_str_.strip(" ")
                       sub2=_str_.split(" ")
                       _list2.append(sub2)
            #print(_list2)
            #convert each sub list to a 6 itens string lists to fit in the table
            _list3 = []
            size = 5
            for lst in _list2:
                while len(lst) <= size:
                    lst.append(" ")
                _list3.append(lst)
            #print(_list3)
            script_manipulation_form(_list3)
     
        #create a new script text file    
        if event in ("-NEW_S-", "New Script"):
            empty_script_list = []
            script_manipulation_form(empty_script_list)
            file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
            window["-FILE_LIST-"].update(file_names)
            window["-TOUT-"].update(" ")
            window["-TEXT-"].update(" ")
         
        #delete a script text file    
        if event in ("-DEL_S-", "Delete Script"):
             if values["-FILE_LIST-"] == []:
                sg.popup("No script file selected!")
             elif sg.popup("Once deleted, the file can't be restored! Continue?"):
                file_selection = values["-FILE_LIST-"][0]
                file_to_delete = os.path.join(folder_location, file_selection)
                os.remove(file_to_delete)
                file_names = [f for f in file_list if os.path.isfile(os.path.join(folder_location, f)) and f.lower().endswith((".txt", ".run"))]
                window["-FILE_LIST-"].update(file_names)
                window["-TOUT-"].update(" ")
                window["-TEXT-"].update(" ")
           
    window.close()
    
if __name__ == '__main__':    
    main()
        