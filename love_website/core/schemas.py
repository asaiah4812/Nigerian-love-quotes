from .models import Category, Quote
from ninja import ModelSchema, Schema
from django.contrib.auth.models import User


class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['id', 'name']
class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['username']


class QuoteSchema(ModelSchema):
    category: CategorySchema | None = None
    author: UserSchema
    class Meta:
        model = Quote
        fields = ['id', 'author','msg', 'translation', 'category']

class QuoteCreateSchema(Schema):
    author:str
    msg:str
    category_id: int | None = None