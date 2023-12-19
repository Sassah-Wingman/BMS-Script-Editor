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
    main_window_title = "THIS IS MY APP"

    if not glfw.init():
        print("Could not initialize OpenGL context!")
        sys.exit(1)

    # Create a windowed mode window and its OpenGL context
    main_window = glfw.create_window(int(main_window_width), int(main_window_height), main_window_title, None, None)
    glfw.make_context_current(main_window)

    if not main_window:
        glfw.terminate()
        print("Could not initialize Window!")
        sys.exit(1)

    return main_window

def main():
    imgui.create_context()
    window = gflw_init()
    sleep(5)
    glfw.terminate()

if __name__ == "__main__":
    main()