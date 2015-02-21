#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'guowangsun'

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s : %s' % (self.name, self.score)
 
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

class Animal(object):

    def run(self):
        print 'A animal is running...'

class Cat(Animal):

    def run(self):
        print 'A Cat is running...'

class Dog(Animal):

    def run(self):
        print 'A Dog is running...'

class Test(object):

    def test(self, animal):
        animal.run()


