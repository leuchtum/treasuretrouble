from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from treasuretrouble import __version__
from treasuretrouble.settings import get_settings

settings = get_settings()
config = OpenAPIConfig(
    title=settings.app.NAME,
    version=__version__,
    use_handler_docstrings=True,
    render_plugins=[ScalarRenderPlugin()],
)
