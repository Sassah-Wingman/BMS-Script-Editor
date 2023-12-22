# -*- coding: utf-8 -*-
from ast import Return
import sys

# rendering modules
import OpenGL.GL as gl
import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer

active = {"welcome": True, "file": True}
opened_state = True

#welcome window inplementation
def welcome_window ():
      
      if active ["welcome"]:     
         imgui.begin("Welcome", True)
         imgui.text("Welcome to BMS Script Editor")
         clickclose = imgui.button("Close", 60, 20)
         imgui.same_line(spacing = 50)
         clickquit = imgui.button("Exit", 60, 20)
         if clickclose:
             active ["welcome"] = False 
             imgui.end()
             return

         if clickquit:
           sys.exit(0)   
     
         imgui.end()
     
# commands implementation
def frame_commands ():
          
     # assign ctrl + Q to Quit
     io = imgui.get_io()
     if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)
        
     # main menu bar routine
     if imgui.begin_main_menu_bar():
         if imgui.begin_menu("File", True):
             imgui.menu_item("New", "Ctrl + N", False, True)
             openfile = imgui.menu_item("Open", "Ctrl + O", False, True)
             imgui.menu_item("Close", "Ctrl + C", False, True)
             imgui.menu_item("Save", "Ctrl + S", False, True)

             if openfile:
                sentence = "hello world\n"
                with open("test_script.txt", "w") as test_file:
                   test_file.write(sentence)
             
             clicked_quit, selected_quit = imgui.menu_item("Quit", "Ctrl + Q", False, True)

             if clicked_quit:
                 sys.exit(0)

             imgui.end_menu()
         imgui.end_main_menu_bar()


# Window frame implementation
def render_frame(main_window, impl_main_window):
      
      # process mouse and keyboard inputs
      glfw.poll_events() 
      impl_main_window.process_inputs()   
      imgui.new_frame()   
                     
      # Clear the window buffer
      gl.glClearColor(0.2, 0.2, 0.4, 1)
      gl.glClear(gl.GL_COLOR_BUFFER_BIT)

      # Commands that define the application
      frame_commands()
      welcome_window()
      imgui.render()
      impl_main_window.render(imgui.get_draw_data())
      glfw.swap_buffers(main_window)
   
# Open GL implementation
def gflw_init():
    main_window_width, main_window_height = 900, 600
    main_window_title = ">>> BMS SCRIPT EDITOR <<<"

    if not glfw.init():
        print("Could not initialize OpenGL context!")
        sys.exit(1)
        
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    main_window = glfw.create_window(int(main_window_width), int(main_window_height), main_window_title, None, None)
    glfw.make_context_current(main_window)
    glfw.set_window_pos(main_window, 400, 200)

    if not main_window:
        glfw.terminate()
        print("Could not initialize Window!")
        sys.exit(1)

    return main_window

def main():
    #implement renderer and gui
    imgui.create_context()   
    main_window = gflw_init()
    impl_main_window = GlfwRenderer(main_window)
    
    # implemente loop
    while not glfw.window_should_close(main_window):
        render_frame(main_window, impl_main_window)
        
    # terminate implementation    
    impl_main_window.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()