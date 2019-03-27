from configs.dev_config import DevConfig
from configs.production_config import ProductionConfig
from configs.test_config import TestConfig

config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProductionConfig,
    "default": DevConfig,
}
