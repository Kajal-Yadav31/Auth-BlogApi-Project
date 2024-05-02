from rest_framework.throttling import UserRateThrottle


class BlogListViewThrottle(UserRateThrottle):
    scope = "blog-list"


class BlogCreateViewThrottle(UserRateThrottle):
    scope = "blog-create"
