from rest_framework.pagination import PageNumberPagination


class PaginateByPageNumber(PageNumberPagination):
    page_size = 25
    