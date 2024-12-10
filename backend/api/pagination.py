from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    default_limit = settings.DEFAULT_PAGE_SIZE
    limit_query_param = 'limit'

