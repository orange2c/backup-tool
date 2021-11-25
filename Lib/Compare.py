
#传入两个包含所有文件的列表，找出他们的交集与差集
class find_different(): 
	news = ''	# 1有，2无
	dels = ''	# 1无，2有
	sames = ''	#相同的元素们
	def __init__( self, list1, list2 ) -> None:

		self.sames = set(list1).intersection(set(list2))
		self.news = set(list1) - set( list2 ) #获得需要新增的文件
		self.dels = set(list2) - set(list1) #获得要删除的文件

		if self.sames == set():	self.sames = None
		if self.news == set():	self.news = None
		if self.dels == set():	self.dels = None
