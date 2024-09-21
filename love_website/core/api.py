from ninja import NinjaAPI
from .models import Quote, Category
from .schemas import CategorySchema, QuoteSchema, QuoteCreateSchema
from django.shortcuts import get_object_or_404
api = NinjaAPI()


@api.get("quotes/", response=list[QuoteSchema])
def get_quotes(request):
    return Quote.objects.all()

@api.get("quotes/{id}/", response=QuoteSchema)
def get_quote(request, id: str):
    quote = get_object_or_404(Quote, id=id)
    return quote

@api.get('categories/', response=list[CategorySchema])
def get_categories(request):
    return Category.objects.all()

@api.post("quotes/", response=QuoteSchema)
def create_device(request, quote: QuoteCreateSchema):
    if quote.category_id:
        category_exists = Category.objects.filter(id=quote.category_id).exists()
        if not category_exists:
            return 404, {'message': 'Category not found'}
    quote_data = quote.model_dump()
    quote_model = Quote.objects.create(**quote_data)
    return quote_model


