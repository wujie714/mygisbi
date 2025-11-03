from utilmeta import UtilMeta
from utilmeta.core import api
from config.config import configure
import django

service = UtilMeta(
    __name__,
    name='blog',
    backend=django,
    asynchronous=True,
    port=8000
)
configure(service)
# should import API after setup
from domain.blog.api import ArticleAPI
from domain.bidata.api import MyGISBIAPI

@service.mount
@api.CORS(allow_origin='*')
class RootAPI(api.API):
    article: ArticleAPI
    bidata: MyGISBIAPI




app = service.application()

if __name__ == '__main__':
    service.run()
