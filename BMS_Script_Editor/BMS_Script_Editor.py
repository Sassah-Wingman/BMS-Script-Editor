# -*- coding: utf-8 -*-
import sys

# rendering modules
import OpenGL.GL as gl
import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer
from time import sleep

# main window frame implementation
def gflw_init():
    main_window_width, main_window_height = 900, 600
    main_window_title = ">>> BMS SCRIPT EDITOR <<<"

    if not glfw.init():
        print("Could not initialize OpenGL context!")
        sys.exit(1)

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
    imgui.create_context()   # bring imgui
    main_window = gflw_init()
    render_main_window = GlfwRenderer(main_window)
    
    # Allow instatiate second window 
    file_window = True
    
    # Determine the window is not closed by shorcuts 
    while not glfw.window_should_close(main_window):
        glfw.poll_events()  # function processes events already in queue
        render_main_window.process_inputs()   # python function allow inputs to menu

        imgui.new_frame()    # Start a new frame until next new frame or render

        # main menu bar routine
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):
                imgui.menu_item("New", "Ctrl + N", False, True)
                imgui.menu_item("Open", "Ctrl + O", False, True)
                imgui.menu_item("Close", "Ctrl + C", False, True)
                imgui.menu_item("Save", "Ctrl + S", False, True)

                clicked_quit, selected_quit = imgui.menu_item("Quit", "Ctrl + Q", False, True)

                if clicked_quit:
                    sys.exit(0)

                imgui.end_menu()
            imgui.end_main_menu_bar()

            # Define the main window background color
            gl.glClearColor(0.2, 0.2, 0.4, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        render_main_window.render(imgui.get_draw_data())
        glfw.swap_buffers(main_window)

    render_main_window.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()