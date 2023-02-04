from rest_framework import pagination


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    max_limit = 250
    limit_query_description = "Limit on the number of returned results, default - 20, maximum - 250"
    offset_query_description = "Indent by the number of items from which results will be returned"
