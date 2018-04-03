from trading_dev_env.general.utils import Singleton


def test_singleton():
    class A(metaclass=Singleton):
        pass

    a = A()
    b = A()
    assert a is b
