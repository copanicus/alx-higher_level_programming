#!/usr/bin/python3
"""Rectangle Module Test Case"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInstantiation --------------> line 26
    TestRectangleWidth ----------------------> line 135
    TestRectangleHeight ---------------------> line 234
    TestRectangleX --------------------------> line 333
    TestRectangleY --------------------------> line 422
    TestRectangleArea -----------------------> line 510
    TestRectangleUpdateArgs -----------------> line 537
    TestRectangleUpdateKwargs ---------------> line 664
    TestRectangleToDictionary ---------------> line 785
"""


class TestRectangleInstantiation(unittest.TestCase):
    """Unittest for instantiation of the Rectangle class"""

    def test_rectangle_is_base(self):
        """Test case if rectangle is an instance of base class"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test case for no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test case for one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test case for two arguments"""
        rec_1 = Rectangle(10, 2)
        rec_2 = Rectangle(2, 10)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_three_args(self):
        """Test case for three arguments"""
        rec_1 = Rectangle(2, 2, 4)
        rec_2 = Rectangle(4, 4, 2)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_four_args(self):
        """Test case for four arguments"""
        rec_1 = Rectangle(1, 2, 3, 4)
        rec_2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_five_args(self):
        """Test case for five arguments"""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test case for more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test case for accessing private method, width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test case for accessing private method, height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test case for accessing private method, x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test case for accessing private method, y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test case for getting width of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        """Test case for setting width of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        """Test case for getting the height of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        """Test case for setting the height of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getter(self):
        """Test case for getting the x coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        """Test case for setting the x coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getter(self):
        """Test case for getting the y coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        """Test case for setting the y coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittest for initialization of Rectangle width attribute"""

    def test_negative_width(self):
        """Test case for assigning negative value to width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 9)

    def test_zero_width(self):
        """Test case for assigning a value of zero to width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_none_width(self):
        """Test case for assigning None to width of rectangle"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 8)

    def test_str_width(self):
        """Test case for assigning string of charaters to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("best", 120)

    def test_str_int_width(self):
        """Test case for assigning string of charaters to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("23", 8)

    def test_float_width(self):
        """Test case for assigning float value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.009, 3)

    def test_complex_width(self):
        """Test case for assigning complex value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 5)

    def test_dict_width(self):
        """Test case for assigning a dictionary object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Jay": 78, "Kay": 87}, 9)

    def test_bool_width(self):
        """Test case for assigning a Boolean value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 9)

    def test_list_width(self):
        """Test case for assigning a list object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([23, 32, 14, 41], 9)

    def test_set_width(self):
        """Test case for assigning a set object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({6, 7, 8}, 9)

    def test_tuple_width(self):
        """Test case for assigning a tuple object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((6, 7, 8), 9)

    def test_frozenset_width(self):
        """Test case for assigning a frozenset object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({5, 4, 8, 6, 3, 7}), 9)

    def test_range_width(self):
        """Test case for assigning a range value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(2, 8), 9)

    def test_bytes_width(self):
        """Test case for assigning a byte object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Best Scool', 9)

    def test_bytearray_width(self):
        """Test case for assigning a bytearray object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'uvwxyz'), 9)

    def test_memoryview_width(self):
        """Test case for assigning a memoryview object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'uvwxyz'), 9)

    def test_inf_width(self):
        """Test case for assigning infinit object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 9)

    def test_nan_width(self):
        """Test case for assigning nan object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 9)


class TestRectangleHeight(unittest.TestCase):
    """Unittest for initialization of Rectangle height attribute"""

    def test_negative_height(self):
        """Test case for assigning negative value to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -9)

    def test_zero_height(self):
        """Test case for assigning a value of zero to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, 0)

    def test_none_height(self):
        """Test case for assigning None to height of rectangle"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, None)

    def test_str_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(120, "school")

    def test_str_int_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, "9")

    def test_float_height(self):
        """Test case for assigning float value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 3.009)

    def test_complex_height(self):
        """Test case for assigning complex value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, complex(2))

    def test_dict_height(self):
        """Test case for assigning a dictionary object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"Jay": 78, "Kay": 87})

    def test_bool_height(self):
        """Test case for assigning a Boolean value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, False)

    def test_list_height(self):
        """Test case for assigning a list object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, [23, 32, 14, 41])

    def test_set_height(self):
        """Test case for assigning a set object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {6, 7, 8})

    def test_tuple_height(self):
        """Test case for assigning a tuple object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, (6, 7, 8))

    def test_frozenset_height(self):
        """Test case for assigning a frozenset object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, frozenset({5, 4, 8, 6, 3, 7}))

    def test_range_height(self):
        """Test case for assigning a range value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, range(2, 8))

    def test_bytes_height(self):
        """Test case for assigning a byte object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, b'Best Scool')

    def test_bytearray_height(self):
        """Test case for assigning a bytearray object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, bytearray(b'uvwxyz'))

    def test_memoryview_height(self):
        """Test case for assigning a memoryview object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, memoryview(b'uvwxyz'))

    def test_inf_height(self):
        """Test case for assigning infinit object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('inf'))

    def test_nan_height(self):
        """Test case for assigning nan object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))


class TestRectangleX(unittest.TestCase):
    """Unittest for initialization of the x attribute"""

    def test_negative_x(self):
        """Test case for assigning a negative value to coordinate x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 7, -8, 9)

    def test_none_x(self):
        """Test case for assigning a None object to coordindate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, None)

    def test_str_x(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, "best", 9)

    def test_float_x(self):
        """Test case for assigning a float object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, 8.8, 9)

    def test_complex_x(self):
        """Test case for assigning a complex object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, complex(9))

    def test_dict_x(self):
        """Test case for assigning a dictionary object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, {"Jay": 78, "Kay": 87}, 9)

    def test_bool_x(self):
        """Test case for assigning a Boolean object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, False, 9)

    def test_list_x(self):
        """Test case for assigning a list object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, [6, 7, 8], 9)

    def test_set_x(self):
        """Test case for assigning a set object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, {6, 7, 8}, 9)

    def test_tuple_x(self):
        """Test case for assigning a tuple object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (6, 7, 8), 9)

    def test_frozenset_x(self):
        """Test case for assigning a frozenset object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_x(self):
        """Test case for assigning a range value to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, range(4, 9))

    def test_bytes_x(self):
        """Test case for assigning a byte object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, b'Best School')

    def test_bytearray_x(self):
        """Test case for assigning a bytearray object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_x(self):
        """Test case for assigning memoryview object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, memoryview(b'uvwxyz'))

    def test_inf_x(self):
        """Test case for assigning an infinit object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('inf'), 9)

    def test_nan_x(self):
        """Test case for assigning a Nan object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('nan'), 9)


class TestRectangleY(unittest.TestCase):
    """Unittest for initialization of the y attribute"""

    def test_negative_y(self):
        """Test case for assigning a negative value to coordinate y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 7, 8, -9)

    def test_none_y(self):
        """Test case for assigning a None object to coordindate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, None)

    def test_str_y(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, "best")

    def test_float_y(self):
        """Test case for assigning a float object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, 9.9)

    def test_complex_y(self):
        """Test case for assigning a complex object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, complex(9))

    def test_dict_y(self):
        """Test case for assigning a dictionary object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, {"Jay": 78, "Kay": 87})

    def test_bool_y(self):
        """Test case for assigning a Boolean object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, False)

    def test_list_y(self):
        """Test case for assigning a list object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, [7, 8, 9])

    def test_set_y(self):
        """Test case for assigning a set object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, {7, 8, 9})

    def test_tuple_y(self):
        """Test case for assigning a tuple object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (7, 8, 9))

    def test_frozenset_y(self):
        """Test case for assigning a frozenset object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_y(self):
        """Test case for assigning a range value to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, range(5, 9))

    def test_bytes_y(self):
        """Test case for assigning a byte object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, b'Best School')

    def test_bytearray_y(self):
        """Test case for assigning a bytearray object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_y(self):
        """Test case for assigning memoryview object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, memoryview(b'uvwxyz'))

    def test_inf_y(self):
        """Test case for assigning an infinit object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('inf'))

    def test_nan_y(self):
        """Test case for assigning a Nan object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('nan'))


class TestRectangleArea(unittest.TestCase):
    """Unittest for area of the rectangle"""

    def test_area_small(self):
        """Test case for an area of small value"""
        rec = Rectangle(9, 6, 0, 0, 0)
        self.assertEqual(rec.area(), 54)

    def test_area_large(self):
        """Test case for a large area"""
        rec = Rectangle(9999999999, 9999999999, 0, 0, 1)
        self.assertEqual(rec.area(), 99999999980000000001)

    def test_area_changed_attributes(self):
        """Test case for an area with altered values"""
        rec = Rectangle(9, 7, 1, 1, 1)
        rec.width = 3
        rec.height = 8
        self.assertEqual(rec.area(), 24)

    def test_area_one_arg(self):
        """Test case for an area with one argument"""
        rec = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittest for update argument method of the Rectangle class"""

    def test_update_args_zero(self):
        """Test case for update method without any arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update()
        self.assertEqual(str(rec), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_args_one(self):
        """Test case for update method with one argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(str(rec), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args_two(self):
        """Test case for update method with two arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 3)
        self.assertEqual(str(rec), "[Rectangle] (89) 10/10 - 3/10")

    def test_update_args_three(self):
        """Test case for update method with three arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3)
        self.assertEqual(str(rec), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_args_four(self):
        """Test case for update method with four arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4)
        self.assertEqual(str(rec), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args_five(self):
        """Test case for update method with five arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rec), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_more_than_five(self):
        """Test case for update method with more than five arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(rec), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_none_id(self):
        """Test case for update method with None as argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None)
        res = f"[Rectangle] ({rec.id}) 10/10 - 10/10"
        self.assertEqual(str(rec), res)

    def test_update_args_none_id_and_more(self):
        """Test case for update method with none and more arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None, 4, 5, 2)
        res = f"[Rectangle] ({rec.id}) 2/10 - 4/5"
        self.assertEqual(str(rec), res)

    def test_update_args_twice(self):
        """Test case for update method with double updating"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5, 6)
        rec.update(9, 4, 3, 5, 3, 7)
        self.assertEqual(str(rec), "[Rectangle] (9) 5/3 - 4/3")

    def test_update_args_invalid_width_type(self):
        """Test case for update method with an invalid argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(98, "best")

    def test_update_args_width_zero(self):
        """Test case for update method with zero argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(89, 0)

    def test_update_args_width_negative(self):
        """Test case for update method with a negative argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(89, -9)

    def test_update_args_invalid_height_type(self):
        """Test case for update method with an invalid height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(89, 9, "best")

    def test_update_args_height_zero(self):
        """Test case for update method with a zero height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(89, 9, 0)

    def test_update_args_height_negative(self):
        """Test case for update method with a negative height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(89, 8, -9)

    def test_update_args_invalid_x_type(self):
        """Test case for update method with an invalid x value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(89, 8, 9, "school")

    def test_update_args_x_negative(self):
        """Test case for update method with a negative x value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(89, 7, 8, -9)

    def test_update_args_invalid_y(self):
        """Test case for update method with an invalid y value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(89, 7, 8, 9, "best")

    def test_update_args_y_negative(self):
        """Test case for update method with a negative y value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(89, 1, 2, 3, -6)


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittest for update argument method of the Rectangle class"""

    def test_update_kwargs_zero(self):
        """Test case for update method without any arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update()
        self.assertEqual(str(rec), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_one(self):
        """Test case for update method with one argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=9)
        self.assertEqual(str(rec), "[Rectangle] (10) 10/10 - 10/9")

    def test_update_kwargs_two(self):
        """Test case for update method with two arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=9, width=4)
        self.assertEqual(str(rec), "[Rectangle] (10) 10/10 - 4/9")

    def test_update_kwargs_three(self):
        """Test case for update method with three arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=9, width=4, x=3)
        self.assertEqual(str(rec), "[Rectangle] (10) 3/10 - 4/9")

    def test_update_kwargs_four(self):
        """Test case for update method with four arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=9, width=4, x=3, y=4)
        self.assertEqual(str(rec), "[Rectangle] (10) 3/4 - 4/9")

    def test_update_kwargs_five(self):
        """Test case for update method with five arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rec), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs_none_id(self):
        """Test case for update method with None as argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None)
        res = f"[Rectangle] ({rec.id}) 10/10 - 10/10"
        self.assertEqual(str(rec), res)

    def test_update_kwargs_none_id_and_more(self):
        """Test case for update method with none and more arguments"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None, height=4, width=9, x=2)
        res = f"[Rectangle] ({rec.id}) 10/10 - 10/10"
        self.assertEqual(str(rec), res)

    def test_update_kwargs_twice(self):
        """Test case for update method with double updating"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=9, height=4, x=3, y=4, id=5)
        rec.update(width=4, height=8, x=6, y=6, id=6)
        self.assertEqual(str(rec), "[Rectangle] (6) 6/6 - 4/8")

    def test_update_kwargs_invalid_width_type(self):
        """Test case for update method with an invalid argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="best", height=9)

    def test_update_kwargs_width_zero(self):
        """Test case for update method with zero argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0, height=4)

    def test_update_kwargs_width_negative(self):
        """Test case for update method with a negative argument"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-9, height=4)

    def test_update_kwargs_invalid_height_type(self):
        """Test case for update method with an invalid height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(width=9, height="best")

    def test_update_kwargs_height_zero(self):
        """Test case for update method with a zero height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(width=9, height=0)

    def test_update_kwargs_height_negative(self):
        """Test case for update method with a negative height value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(width=9, height=-9)

    def test_update_kwargs_invalid_x_type(self):
        """Test case for update method with an invalid x value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(width=9, height=4, y=9, x="school")

    def test_update_kwargs_x_negative(self):
        """Test case for update method with a negative x value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(width=9, height=4, y=8, x=-9)

    def test_update_kwargs_invalid_y(self):
        """Test case for update method with an invalid y value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(width=9, height=3, x=8, id=9, y="best")

    def test_update_kwargs_y_negative(self):
        """Test case for update method with a negative y value"""
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(width=9, id=3, height=2, x=3, y=-6)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittest for to_dictionary method of the Rectangle class"""

    def test_to_dictionary_output(self):
        """Test case for dictionary object output"""
        rec = Rectangle(10, 2, 1, 9, 5)
        res = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(res, rec.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Test case for no object output"""
        rec_1 = Rectangle(10, 2, 1, 9, 5)
        rec_2 = Rectangle(5, 9, 1, 2, 10)
        rec_2.update(**rec_1.to_dictionary())
        self.assertNotEqual(rec_1, rec_2)

    def test_to_dictionary_arg(self):
        """Test case for to_dictionary arg"""
        rec = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
