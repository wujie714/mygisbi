from utilmeta.core import api, orm, request, response
from .schema import BIDataSchema
from .models import BIData
from domain.blog.models import User


class MyGISBIAPI(api.API):
    @api.get
    async def get_bi_data(self, id: int) -> BIDataSchema:
        return await BIDataSchema.ainit(id)

    @api.post
    async def create_bi_data(self, author_id: int, content: str) -> BIDataSchema:
        # 检查用户是否存在
        user = await User.objects.aget(pk=author_id)
        # 创建新的BIData记录
        bidata = await BIData.objects.acreate(author=user, content=content)
        # 返回创建的记录
        return await BIDataSchema.ainit(bidata)

    @api.put
    async def update_bi_data(self, id: int, content: str) -> BIDataSchema:
        # 查找并更新记录
        bidata = await BIData.objects.aget(pk=id)
        bidata.content = content
        await bidata.asave()
        # 返回更新后的记录
        return await BIDataSchema.ainit(bidata)

    @api.delete
    async def delete_bi_data(self, id: int) -> dict:
        # 查找并删除记录
        await BIData.objects.filter(pk=id).adelete()
        # 返回删除成功的消息
        return {
            'success': True,
            'message': f'BIData with id {id} has been deleted'
        }

    @api.handle(get_bi_data, orm.EmptyQueryset)
    def handle_error(self, e):
        return self.response({
            'error': 'bidata not found',
        }, status=404)

    # @api.handle(create_bi_data, orm.ObjectDoesNotExist)
    # def handle_user_not_found(self, e):
    #     return self.response({
    #         'error': 'User not found'
    #     }, status=404)