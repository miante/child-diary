from .generic import Settings


class ProductionConfiguration(Settings):
    DEBUG: int = False
