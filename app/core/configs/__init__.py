import os

from app.core.configs.dev import DevelopmentConfiguration
from app.core.configs.prod import ProductionConfiguration


settings = ProductionConfiguration()
if os.getenv('env') == 'dev':
    settings = DevelopmentConfiguration()
