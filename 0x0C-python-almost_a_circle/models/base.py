#!/usr/bin/python3
"""Base module"""
import json
import csv
import turtle


class Base:
    """The base class

    Description:
        This class will manage the id attribute
        for all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise the class"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string

        Description:
            This method creates a json string representation
            of the argument

        Args:
            list_dictionaries (list of dictionaries): a list
            of dictionary data

        Returns:
            A json string representation of the parameter
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries, indent=4)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON

        Description:
            This method writes the JSON string representation
            of an object to a file

        Args:
            list_objs (json): a json object
        """
        f = cls.__name__ + ".json"

        with open(f, "w", encoding="UTF-8") as save_json:
            if list_objs is None:
                save_json.write("[]")
            else:
                list_of_dicts = []
                for item in list_objs:
                    list_of_dicts.append(item.to_dictionary())

                save_json.write(Base.to_json_string(list_of_dicts))

    def from_json_string(json_string):
        """Load from JSON

        Description:
            This method creates a list representation of a json string

        Args:
            json_string (json): a JSON string

        Returns:
            A list representation
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create new object

        Description:
            This method creates an instance of either a rectangle
            or square object based on the arguments provided. The
            arguments are passed in a form of a dictionary object

        Args:
            dictionary (dict): an object of key/value pairs

        Returns:
            An instance of either a Rectangle or Square obejct with
            all attributes set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            elif cls.__name__ == "Square":
                instance = cls(1)

            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Load from file

        Description:
            This method loads an instance of either a Rectangle
            or Square object from a JSON file

        Returns"
            A list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="UTF-8") as json_file:
                list_dict = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to CSV file

        Description:
            This method serializes a CSV file

        Args:
            list_objs (list): a list of objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="UTF-8") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load from CSV file

        Description:
            This method deserialises an object from a CSV file

        Returns:
            A list of instantiated objects
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="UTF-8") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw with turtle module

        Description:
            This method draws Rectangles and Squares using the
            turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """

        turt = turtle.Turtle()
        turt.screen.bgcolor("#154360")
        turt.pensize(5)
        turt.shape("turtle")

        turt.color("#FFC300")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(3):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#FF5733")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(3):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
