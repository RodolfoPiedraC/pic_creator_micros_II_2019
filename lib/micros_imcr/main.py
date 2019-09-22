# -*- coding: utf-8 -*-
#
# Copyright 2019 Rodolfo José Piedra Camacho

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from PIL import Image, ImageDraw
from json import loads
from logging import getLogger

log = getLogger(__name__)


# IMCR main class
# This creates and handles any new image
class ImcrPrinter:

    def __init__(self, json_data):
        """
        :param json_data: Is the json data in dictionary format
        """
        # Initialize all the private params based on the JSON information
        self.__imcr_color_array = [
            json_data["color1"],
            json_data["color2"],
            json_data["color3"],
            json_data["color4"]]
        self.__background = json_data["background"]
        self.__imcr_sizex = json_data["sizex"]
        self.__imcr_sizey = json_data["sizey"]
        self.__imcr_extension = json_data["format"]

        # Initialize the image
        self.current_image = Image.new(
            mode="RGB",
            size=(self.__imcr_sizex, self.__imcr_sizey),
            color=self.__background)

    def get_color_array_size(self):
        """
        Return the size of the color_array
        """
        return len(self.__imcr_color_array)

    def get_random_index(self):
        """
        Return a random valid index for the color_array
        """
        return random.randrange(len(self.__imcr_color_array))

    def restart_image(self):
        """
        Resets the internal parameter current_image
        """
        self.current_image = Image.new(
            mode="RGB",
            size=(self.__imcr_sizex, self.__imcr_sizey),
            color=self.__background)

    def save_image(self, file_root_name):
        """
        Saves the internal parameter current_image
        """
        self.current_image.save(
            "{}.{}".format(file_root_name, self.__imcr_extension))

    def draw_line(self, x_start, y_start, x_finish, y_finish, color_index):
        """
        Based on the different parameters creates a line in the objects image
        :param x_start:       X position of the start pixel
        :param y_start:       Y position of the start pixel
        :param x_finish:      X position of the last pixel
        :param y_finish:      Y position of the last pixel
        :param color_index:   Color index used to obtain the color from
                              __imcr_color_array
        """
        # Check that the length plus the start don't go over the images size
        # ---------------------
        if x_finish > self.__imcr_sizex:
            log.error("Start of X position plus the length goes beyond the"
                      " image's size")
            raise ValueError

        if y_finish > self.__imcr_sizey:
            log.error("Start of Y position plus the length goes beyond the"
                      " image's size")
            raise ValueError

        # Check that the desired index is obtainable
        if color_index > len(self.__imcr_color_array):
            log.error("Desired color index goes beyond the color array")

        # Get the desired color
        # ---------------------
        current_color = self.__imcr_color_array[color_index]

        # Start drawline process
        # ---------------------
        drawer = ImageDraw.Draw(self.current_image)
        drawer.line(
            xy=(x_start, y_start, x_finish, y_finish),
            fill=(current_color[0], current_color[1], current_color[2]))


def micros_imcr_main(args):
    """
    Main call of the IMCR package
    Takes a path to a JSON file and creates a set of default images
    """
    # Obtain the json information
    # --------------------------------------------------------------------------
    # Read the file
    json_file = open(args.path_to_json).read()
    json_data = loads(json_file)

    imcr_sizex = json_data["sizex"]
    imcr_sizey = json_data["sizey"]

    # Initialize the ImcrPrinter object
    printer = ImcrPrinter(json_data)

    # Generate the basic images
    # --------------------------------------------------------------------------
    # First Drawing: Single vertical Line
    # Starts 1/3 in the y axis and draws 1/3 of the size
    printer.draw_line(
        x_start=imcr_sizex//2,
        y_start=imcr_sizey//3,
        x_finish=imcr_sizex//2,
        y_finish=2*imcr_sizey//3,
        color_index=printer.get_random_index())

    printer.save_image(file_root_name="simple_line")

    # Second Drawing: Multiple lines
    # Restart Image
    printer.restart_image()

    # Adds one horizontal line of each color with no intersections
    for i in range(printer.get_color_array_size()):
        printer.draw_line(
            x_start=imcr_sizex//3,
            y_start=(i+1)*imcr_sizey//5,
            x_finish=2*imcr_sizex//3,
            y_finish=(i+1)*imcr_sizey//5,
            color_index=i)

    printer.save_image(file_root_name="multiple_horizontal_line")

    # Third Drawing: Diagonal line
    # Restart Image
    printer.restart_image()

    # Adds two diagonal lines of the same color
    random_color = printer.get_random_index()
    for i in range(2):
        printer.draw_line(
            x_start=imcr_sizex//5,
            y_start=(i+1)*imcr_sizey//5,
            x_finish=2*imcr_sizex//5,
            y_finish=(i+2)*imcr_sizey//5,
            color_index=random_color)

    printer.save_image(file_root_name="diagonal_lines")

    # Fourth Drawing: Intersection
    # Restart Image
    printer.restart_image()

    # Diagonal intersection using two random colors
    # Draw first diagonal
    random_color = printer.get_random_index()
    printer.draw_line(
        x_start=imcr_sizex//3,
        y_start=imcr_sizey//5,
        x_finish=2*imcr_sizex//3,
        y_finish=4*imcr_sizey//5,
        color_index=random_color)

    # Draw second diagonal
    second_random_color = random_color
    while second_random_color == random_color:
        second_random_color = printer.get_random_index()

    printer.draw_line(
        x_start=imcr_sizex//3,
        y_start=4*imcr_sizey//5,
        x_finish=2*imcr_sizex//3,
        y_finish=imcr_sizey//5,
        color_index=second_random_color)

    printer.save_image(file_root_name="diagonal_intersection")

    # Fifth Drawing: Four Line intersection
    # Restart Image
    printer.restart_image()

    # Creates four lines where there are multiple intersections
    # Draw first line
    printer.draw_line(
        x_start=imcr_sizex//3,
        y_start=imcr_sizey//5,
        x_finish=2*imcr_sizex//3,
        y_finish=4*imcr_sizey//5,
        color_index=0)

    # Draw second line
    printer.draw_line(
        x_start=imcr_sizex//3,
        y_start=imcr_sizey//4,
        x_finish=2*imcr_sizex//3,
        y_finish=imcr_sizey//4,
        color_index=1)

    # Draw third line
    printer.draw_line(
        x_start=imcr_sizex//4,
        y_start=4*imcr_sizey//5,
        x_finish=3*imcr_sizex//4,
        y_finish=3*imcr_sizey//5,
        color_index=2)

    # Draw second line
    printer.draw_line(
        x_start=imcr_sizex//2,
        y_start=1*imcr_sizey//5,
        x_finish=imcr_sizex//2,
        y_finish=4*imcr_sizey//5,
        color_index=3)

    printer.save_image(file_root_name="full_intersection")
