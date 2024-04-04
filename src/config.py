from typing import cast

from miose_toolkit_common.config import Config, Env


class ConfigTemplate(Config):
    """Config template"""

    


config = cast(ConfigTemplate, ConfigTemplate.load_config(create_if_not_exists=True))
config.dump_config([Env.Dev.value, Env.Prod.value])
