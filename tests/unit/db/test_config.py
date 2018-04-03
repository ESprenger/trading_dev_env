import pytest
from trading_dev_env.db.config import config_setup


def test_config_setup():
    with pytest.raises(Exception):
        config_setup('something', 'else')

    config_dict = config_setup()
    assert config_dict
    assert sorted(config_dict.keys()) == ['database', 'host', 'password', 'user']
