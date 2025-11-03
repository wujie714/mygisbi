import utype
from utilmeta.core import orm
# from domain.blog.models import BIData
from domain.blog.api import UserSchema
from domain.bidata.models import BIData

class BIDataSchema(orm.Schema[BIData]):
    id: int
    author: UserSchema
    type: str
    memo: str
    content: str