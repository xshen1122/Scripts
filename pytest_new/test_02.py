# coding: utf-8
import pytest
def setup_module():
    print ("模块级别的setup")

def teardown_module():
    print ("模块级别的teardown")

def setup_function():
    print ("函数级别的setup")

def teardown_function():
    print ("函数级别的teardown")



def test_one():
    print ("this is test one")

class TestClass():
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup_method(self):
        print("方法级别的setup")

    def teardown_method(self):
        print("方法级别的teardown")

    def setup(self):
        print("普通级别的setup")

    def teardown(self):
        print("普通级别的teardown")

    def test_two(self):
        print("this is test two in TestClass")


pytest.main()