from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
  # set the maximum value to 8 ()=== max 8 entries per page)
  max_limit = 8
