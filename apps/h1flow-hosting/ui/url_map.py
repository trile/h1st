from .h1flows.home import Home
from .h1flows.execute import Execute
from .h1flows.upload import Upload

URL_MAP = {
    "": Home,
    "upload/": Upload,
    "execute/": Execute,
}