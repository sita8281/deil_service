import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main_db.sqlite3')
    SECRET_KEY = 'S_DEIL_PASSW_$102394'
    DEIL_API_CRYPTO = b'xYYntA1G42M-XLK-VryRfGRPsCOHcaldYCuFhfYd1S8='


class DevelopementConfig(BaseConfig):
    DEBUG = True
    ICMP_DAEMON = False
    NAS_DAEMON = False
    FORWARD_GATEWAY_DAEMON = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    ICMP_DAEMON = True
    NAS_DAEMON = True
    FORWARD_GATEWAY_DAEMON = True


class DisableIcmpConfig(BaseConfig):
    DEBUG = True
    ICMP_DAEMON = False
    NAS_DAEMON = True
    FORWARD_GATEWAY_DAEMON = True
