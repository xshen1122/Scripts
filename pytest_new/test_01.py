# coding: utf-8
import pytest
@pytest.fixture(params=[1,2,3])
def data(request):
    print ("这是一个数据")
    return request.param


def test_01(data):
    print ('这是第一个用例')
    tmp='zc'
    print (data)
    # assert 1==2
    # pytest.assume(1==2)
    # pytest.assume(False)

