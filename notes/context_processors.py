from django.db.models import Count
from .models import Category

def categories_processor(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(user=request.user).annotate(notes_count=Count('notes'))
        return {'categories': categories}
    return {'categories': []}