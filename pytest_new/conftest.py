# coding: utf-8
import pytest

@pytest.fixture(scope="session")
def login():
    print ("这是一个登录方法a")

