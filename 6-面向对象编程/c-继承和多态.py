#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     c-继承和多态
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass

'''
对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。

继承有什么好处？最大的好处是子类获得了父类的全部功能。
由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干
，就自动拥有了run()方法：
'''

dog=Dog()
dog.run()
cat=Cat()
cat.run()
'''
继承有什么好处？最大的好处是子类获得了父类的全部功能。
也可以对子类增加一些方法
继承的第二个好处需要我们对代码做一点改进。
子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
这样，我们就获得了继承的另一个好处：多态。

在继承关系中，如果一个实例的数据类型是某个子类，
那它的数据类型也可以被看做是父类。但是，反过来就不行：
'''
class Fish(Animal):
    def run(self):
        print("Fish is running")
    def eat(self):
        print("Fish is eat")

fish=Fish()
fish.run()
fish.eat()

'''
多态的好处就是，当我们需要传入Fish、Pig、Tortoise……时，
我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，
只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
'''
class Pig(Animal):
    def run(self):
        print("Pig is running")
    def eat(self):
        print("Pig is eat")

def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(Animal())
run_twice(Fish())
run_twice(Pig())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())