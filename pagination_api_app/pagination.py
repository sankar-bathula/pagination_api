from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
class MyPagination(PageNumberPagination):
	page_size = 5 #max_number of records for page
	page_query_param = 'mypage' # http://127.0.0.1:8000/api/?mypage=10
	page_size_query_param = 'num'
	max_page_size = 11
	last_page_strings = ('end_page',)

class MyPagination2(LimitOffsetPagination):
	default_limit = 10
	limit_query_parm = 'mylimit'#http://127.0.0.1:8000/api/?limit=5&offset=20
	offset_query_parm = 'myoffset'
	max_limit = 20
	page_size = 10
class MyPagination3(CursorPagination):
	ordering = 'esal'
	page_size = 8
	cursor_query_param = 'mycursor'