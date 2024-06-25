from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar.plugins import InitPluginProtocol
from litestar.plugins.structlog import StructlogPlugin

from treasuretrouble.configs.alchemy import cfg as alchemy_cfg
from treasuretrouble.configs.structlog import cfg as structlog_cfg
from treasuretrouble.server.builder import ApplicationConfigurator

structlog_plugin = StructlogPlugin(config=structlog_cfg)
alchemy_plugin = SQLAlchemyPlugin(config=alchemy_cfg)
app_plugin = ApplicationConfigurator()

active_plugins: list[InitPluginProtocol] = [
    app_plugin,
    alchemy_plugin,
    structlog_plugin,
]
