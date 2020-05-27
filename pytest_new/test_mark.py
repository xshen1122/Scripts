# coding: utf-8
import pytest
@pytest.mark.skip(reason='It is only for IOS')
@pytest.mark.apitest
def test_a():
    print ("this is test a")

@pytest.mark.httptest
def test_b():
    print ('this is test b')