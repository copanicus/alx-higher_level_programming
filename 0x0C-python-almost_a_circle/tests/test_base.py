#!/usr/bin/python3
"""Unit Test Module"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""
    Unittest classes
    TestBaseInstantiation ---------> line 23
    TestBaseToJsonString ----------> line 113
    TestBaseSaveToFile ------------> line 152
    TestBaseFromJsonString --------> line 224
    TestBaseCreate ----------------> line 267
    TestBaseLoadFromFile ----------> line 323
    TestBaseSaveToFileCSV ---------> line 397
    TestBaseLoadFromFileCSV -------> line 485
"""


class TestBaseInstantiation(unittest.TestCase):
    """Unittest for instantiation of the Base class"""

    def test_none_id(self):
        """Test case for None as id"""
        base_1 = Base(None)
        base_2 = Base(None)
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_unique_id(self):
        """Test case for unique id"""
        self.assertEqual(Base(20).id, 20)

    def test_id_public(self):
        """Test case for public id"""
        base = Base(15)
        base.id = 20
        self.assertEqual(base.id, 20)

    def test_nb_instances_private(self):
        """Test case for private attribute id"""
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_str_id(self):
        """Test case for a string"""
        self.assertEqual(Base("hello").id, "hello")

    def test_float_id(self):
        """Test case for a floating point id"""
        self.assertEqual(Base(12.5).id, 12.5)

    def test_complex_id(self):
        """Test case for complex id"""
        self.assertEqual(Base(complex(3)).id, complex(3))

    def test_dict_id(self):
        """Test case for a ductionary id"""
        self.assertEqual(Base({"Jay": 87, "Kay": 78}).id, {'Jay': 87, 'Kay': 78})

    def test_bool_id(self):
        """Test case for a Boolean id"""
        self.assertEqual(Base(False).id, False)

    def test_list_id(self):
        """Test case for a list argument"""
        self.assertEqual(Base([17, 71, 81, 18]).id, [17, 71, 81, 18])

    def test_tuple_id(self):
        """Test case for a tupel argument"""
        self.assertEqual(Base((21, 12, 14, 41)).id, (21, 12, 14, 41))

    def test_set_id(self):
        """Test case for a set argument"""
        self.assertEqual(Base({"a", "b", "c"}).id, {'c', 'a', 'b'})

    def test_frozenset_id(self):
        """Test case for a frozenset argument"""
        self.assertEqual(Base(frozenset({3, 10, -12})).id, frozenset({10, 3, -12}))

    def test_range_id(self):
        """Test case for a range id"""
        self.assertEqual(Base(range(4, 14)).id, range(4, 14))

    def test_bytes_id(self):
        """Test case for bytes argument"""
        self.assertEqual(Base(b'ALX').id, b'ALX')

    def test_bytearray_id(self):
        """Test case for a bytearray argument"""
        self.assertEqual(Base(bytearray(b'uvwxyz')).id, bytearray(b'uvwxyz'))

    def test_memoryview_id(self):
        """Test case for a memory view argument"""
        self.assertEqual(Base(memoryview(b'abcefg')).id, memoryview(b'abcefg'))

    def test_inf_id(self):
        """Test case for an infinit id"""
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_nan_id(self):
        """Test case for a nan id"""
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_two_args(self):
        """Test case for two arguments"""
        with self.assertRaises(TypeError):
            Base(6, 3)


class TestBaseToJsonString(unittest.TestCase):
    """Unittest for to_json_string method of Base class"""

    def test_to_json_string_rectangle_type(self):
        """Test case for rectangle initialisation"""
        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(type(Base.to_json_string([rec.to_dictionary()])), str)

    def test_to_json_string_square_type(self):
        """Test case for square initialisation"""
        square = Square(10, 2, 3, 4)
        self.assertEqual(type(Base.to_json_string([square.to_dictionary()])), str)

    def test_to_json_string_square_two_dicts(self):
        """Test case for two squares"""
        square_1 = Square(10, 2, 3, 4)
        square_2 = Square(4, 5, 21, 2)
        list_dicts = [square_1.to_dictionary(), square_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 164)

    def test_to_json_string_empty_list(self):
        """Test case with an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test case for a None argument"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        """Test case for no argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """Test case for more than one argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittest for save_to_file method of the Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        """Test case for saving a rectangle object to file"""
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_one_square(self):
        """Test case for saving a square object to file"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_cls_name_for_filename(self):
        """Test case for saving a object by cls"""
        square = Square(10, 7, 2, 8)
        Base.save_to_file([square])
        with open("Base.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_overwrite(self):
        """Test case for overwriting previous data"""
        square = Square(9, 2, 39, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_none(self):
        """Test case for saving a None to file"""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        """Test case for saving an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_args(self):
        """Test case for saving to file with an empty argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """Test case for saving with more than one argument"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for from_json_string method of Base class"""

    def test_from_json_string_type(self):
        """Test case for the type of returned object"""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_rectangle(self):
        """Test case for returning a json string from a rectangle object"""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        """Test case for returning a square object from a json string"""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_none(self):
        """Test case for assinging None as parameter"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test case for assigning an empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test case for assigning no parameter"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """Test case for assigning more than one argument"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreate(unittest.TestCase):
    """Unittest for create method of Base class"""

    def test_create_rectangle_original(self):
        """Test case for creating a rectangle object"""
        rec_1 = Rectangle(3, 5, 1, 2, 7)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec_1))

    def test_create_rectangle_new(self):
        """Test case for creating a rectangle"""
        rec_1 = Rectangle(3, 5, 1, 2, 7)
        rec_1_dict = rec_1.to_dictionary()
        rec_2 = Rectangle.create(**rec_1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec_2))

    def test_create_rectangle_is(self):
        """Test case for testing two rectangles"""
        rec_1 = Rectangle(3, 5, 1, 2, 7)
        rec_1_dict = rec_1.to_dictionary()
        rec_2 = Rectangle.create(**rec_1_dict)
        self.assertIsNot(rec_1, rec_2)

    def test_create_rectangle_equals(self):
        """Test case for testing two rectangles"""
        rec_1 = Rectangle(3, 5, 1, 2, 7)
        rec_1_dict = rec_1.to_dictionary()
        rec_2 = Rectangle.create(**rec_1_dict)
        self.assertNotEqual(rec_1, rec_2)

    def test_create_square_original(self):
        """Test case for creating a square"""
        sq_1 = Square(3, 5, 1, 7)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq_1))

    def test_create_square_new(self):
        """Test case for creating a new square"""
        sq_1 = Square(3, 5, 1, 7)
        sq_1_dict = sq_1.to_dictionary()
        sq_2 = Square.create(**sq_1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq_2))

    def test_create_square_is(self):
        """Test case for comparing squares"""
        sq_1 = Square(3, 5, 1, 7)
        sq_1_dict = sq_1.to_dictionary()
        sq_2 = Square.create(**sq_1_dict)
        self.assertIsNot(sq_1, sq_2)

    def test_create_square_equals(self):
        """Test case for creating two equal squares"""
        sq_1 = Square(3, 5, 1, 7)
        sq_1_dict = sq_1.to_dictionary()
        sq_2 = Square.create(**sq_1_dict)
        self.assertNotEqual(sq_1, sq_2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittest for load_from_file_method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        """Test case for loading first rectangle from file"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec_1, rec_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec_1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        """Test case for loading second rectangle from file"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec_1, rec_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec_2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        """Test case for the types of object loaded from file"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec_1, rec_2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_first_square(self):
        """Test case for loading first square instance from file"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq_1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        """Test case for loading second square instance from file"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq_2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        """Test case for the types of object loaded from file"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        output = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_no_file(self):
        """Test case for loading no file"""
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """Test case for loading more than one file"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """Unittest for save_to_file_csv method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        """Test case for saving one rectangle to csv file"""
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("5,10,7,2,8", file.read())

    def test_save_to_file_csv_two_rectangles(self):
        """Test case for saving two rectangles to csv file"""
        rec_1 = Rectangle(10, 7, 2, 8, 5)
        rec_2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rec_1, rec_2])
        with open("Rectangle.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", file.read())

    def test_save_to_file_csv_one_square(self):
        """Test case for saving one square instance to csv file"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_two_squares(self):
        """Test case for saving two square instances to a csv file"""
        sq_1 = Square(10, 7, 2, 8)
        sq_2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sq_1, sq_2])
        with open("Square.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("8,10,7,2\n3,8,1,2", file.read())

    def test_save_to_file_csv_cls_name(self):
        """Test case for saving to csv vile by cls"""
        square = Square(10, 7, 2, 8)
        Base.save_to_file_csv([square])
        with open("Base.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_overwrite(self):
        """Test case for overwriting csv file"""
        square = Square(9, 2, 39, 2)
        Square.save_to_file_csv([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r", encoding="UTF-8") as file:
            self.assertTrue("8,10,7,2", file.read())

    def test_save_to_file_csv_none(self):
        """Test case for saving None to csv file"""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_empty_list(self):
        """Test case for saving empty list to csv file"""
        Square.save_to_file_csv([])
        with open("Square.csv", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_no_args(self):
        """Test case for saving empty argument to csv file"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        """Test case for passing more than one argument to function"""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Unittest for load_from_file_csv method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        """Test case for loading first rectangle from csv file"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec_1, rec_2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec_1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        """Test case for loading second rectangle from csv file"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec_1, rec_2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec_2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        """Test case for accessing the type of rectangle object"""
        rec_1 = Rectangle(10, 7, 2, 8, 1)
        rec_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec_1, rec_2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle)) for obj in output)

    def test_load_from_file_csv_first_square(self):
        """Test case for loading first square instance from csv file"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq_1, sq_2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq_1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        """Test case for loading second square instance from csv file"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq_1, sq_2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq_2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        """Test case for accessing the type of square instance object"""
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq_1, sq_2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_csv_no_file(self):
        """Test case for loading no file"""
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        """Test case for passing more than one argument to function"""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


#   =======================================================================

if __name__ == "__main__":
    unittest.main()
