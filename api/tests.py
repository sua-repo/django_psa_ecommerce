import pickle
from django.test import TestCase

# Create your tests here.

# dev_28 : Serialization의 이해


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


class ObjectAPITest(TestCase):
    def setUp(self):
        pass

    def test_path(self):

        dict = {
            "add": add,
            "sub": sub,
        }

        url = "add"
        print(dict[url](1, 2))

        url = "sub"
        print(dict[url](1, 2))

    # # 사각형 rect 객체를 직렬화 (Serialization)
    # def test_serialization(self):
    #     rect = Rectangle(10, 20)

    #     # 직렬화
    #     with open("rect.data", "wb") as f:
    #         pickle.dump(rect, f)

    #     # 역직렬화
    #     with open("rect.data", "rb") as f:
    #         r = pickle.load(f)

    #     print(r.width, r.height)
