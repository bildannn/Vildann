# from dataclasses import dataclass, field
# from pprint import pprint
#
#
# class Thing:
#     def __init__(self, name, weight, price=0, dims=[]):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f'{self.__dict__}'
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float = 0
#     dims: list = field(default_factory=list)
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#
# th = Thing('name', 15, 1500)
# print(th)
# td = ThingData('name2', 12, 2.5)
# td.dims.append(10)
# print(td)
# td2 = ThingData('name2', 12, 2.5)
# print(td2)








#
# from dataclasses import dataclass, field, InitVar
#
#
# class Vector3D:
#
#     def __init__(self, x, y, z, calc_len: bool = True):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.lenght = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0
#
#
# @dataclass
# class VectorData:
#     x: int
#     y: int = field(compare=False)
#     z: int = field(default=0)
#     calc_len: InitVar[bool] = True
#     lenght: float = field(init=False, default=0)
#     pi: float = field(init=False)
#
#     def __post_init__(self, calc_len):
#         if calc_len:
#             self.lenght = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#         self.pi = 3.14
#
#
# v = Vector3D(1, 2, 3, False)
# print(v.__dict__)
# vd = VectorData(1, 4)
# # vd2 = VectorData(1, 2)
# # print(vd == vd2)
# print(vd)
# # print(vd2)










# from dataclasses import dataclass, field, InitVar
# from random import randint
# from typing import Any
#
#
# @dataclass
# class Goods:
#     current_uil = 0
#
#     uid: int = field(init=False)
#     price: Any
#     weight: Any
#
#     def __post_init__(self):
#         print('Goods')
#         Goods.current_uil += 1
#         self.uid = Goods.current_uil
#
#
# class GoodMeassureFactory:
#
#     @staticmethod
#     def get__init_meassure():
#         return [0, 0, 0]
#
# @dataclass
# class Book(Goods):
#     title: str
#     author: str
#     price: int
#     weight: float
#     meassure: list = field(default_factory=GoodMeassureFactory)
#
#
#     def __post_init__(self):
#         super().__post_init__()
#         print('Book')
#
#
# g = Goods(1222, 2.4)
# print(g)
# g1 = Goods(1222, 2.4)
# print(g1)
# b = Book(2000, 2.6, 'jkhkhlkjk', 'ssasaw')
# for item in b.meassure:
#     b.meassure[i] = randint(10, 20)
# print(b)










# from dataclasses import dataclass, field, make_dataclass
# from typing import Any
#
#
# class Car:
#
#     def __init__(self, model, max_speed, price):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed
#
#
# @dataclass
# class CarD:
#     model: str
#     max_speed: int | float
#     price: int = field(default=0)
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_price(self):
#         return self.price
#
#
# CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', int, field(default=0))],
#                          namespace={'get_max_speed': lambda self: self.max_speed,
#                                     'get_price': lambda self: self.price})
#
# cd = CarData('Lada Priora', 120, 788888)
# print(cd.get_max_speed())
# print(cd.get_price())





# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





# Задачи
# from dataclasses import dataclass, field, make_dataclass
#
#
# @dataclass(order=True)
# class AirCastle:
#     height: int
#     blocks: int
#     color: str
#
#     def change_height(self, value):
#         self.height = value if value > -1 else 0
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('oshibka')
#         self.blocks = self.blocks + other
#         self.height = self.height + other // 5
#
#         return AirCastle(self.height, self.blocks, self.color)
#
#     def visible(self, visible):
#         return f'Видимость замка: {self.height // visible * self.blocks}'
#
#
#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.height} meters is {self.color} with {self.blocks} clouds'
#
#
# v = AirCastle(553, 233, 'wite')
# v1 = AirCastle(503, 175, 'Black')
# print(v)
# v = v + 10
# print(v1)
# print(v1 < v)
# print(v1 > v)
# print(v1 <= v)
# print(v1 >= v)
# print(v1 != v)
# print(v1 == v)










# from dataclasses import dataclass
#
#
# @dataclass(order=True)
# class Wizard:
#     name: str
#     rating: int
#     age: int
#
#     def change_rating(self, value):
#         if value > 0:
#             self.rating = min(self.rating + value, 100)
#             self.age = max(self.age - abs(value) // 10, 18)
#         else:
#             self.rating = max(self.rating + value, 1)
#             self.age = min(self.age + abs(value) // 10, 100)
#
#     def __iadd__(self, string):
#         self.rating += len(string)
#         self.age = max(self.age - len(string) // 10, 18)
#         return self
#
#     def __call__(self, number):
#         return (number - self.age) * self.rating
#
#     def __str__(self):
#         return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"
#
#
# wd = Wizard("Gandalf", 80, 50)
# wd.change_rating(20)
# print(wd)
# wd += "powerful"
# print(wd)
# print(wd(60))
#
# wd1 = Wizard("Merlin", 90, 35)
# print(wd < wd1)