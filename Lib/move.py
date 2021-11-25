
import shutil
import time
import os


PATH_WAREHOUSE = '' #仓库主路径
PATH_HISTORY = ''
PATH_DEL = '' 
PATH_UPDATE = ''


def init(  house_path, history_path ):
	global PATH_WAREHOUSE 
	global PATH_DEL 
	global PATH_UPDATE 
	global PATH_HISTORY

	nowtime = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
	PATH_WAREHOUSE = house_path
	PATH_HISTORY = history_path
	PATH_DEL = history_path + "/" + nowtime + '/delete'
	PATH_UPDATE = history_path + "/" + nowtime + '/update'
	return  history_path + "/" + nowtime


list_todo = [] #待操作列表
class path_todo():
#本类初始化时传入源路径，目标路径，然后执行do方法即会执行复制/移动操作
	is_move = False
	path_from = ''
	path_to = ''
	def __init__(self, path_from, path_to, is_move = False ) -> None:
		self.path_from = os.path.normpath(path_from)
		self.path_to = os.path.normpath(path_to)
		self.is_move = is_move

	def do(self): 
		if os.path.isfile(self.path_from) : #如果是文件
			dir,file=os.path.split(self.path_to) #将目标路径的目录与文件名分离
			if not os.path.isdir(dir): #如果目录不存在
				os.makedirs(dir) #则创建目录
			if self.is_move:
				shutil.move(self.path_from,  self.path_to)
				print("删除：\t%s"%( self.path_from ))
			else:
				print("从 \t%s 复制到\t%s"%( self.path_from, self.path_to ))
				shutil.copy2(self.path_from,  self.path_to)
		else:
			if self.is_move:
				shutil.move(self.path_from,  self.path_to)
				print("删除：\t%s"%( self.path_from ))
			else:
				print("从 \t%s 复制到\t%s"%( self.path_from, self.path_to ))
				shutil.copytree(self.path_from,  self.path_to)


def add_root( path ):
	print('home:',PATH_WAREHOUSE)
	root_name = os.path.basename(path)
	#list_to.append( path_todo(path,PATH_house+'/'+root_name) ) #复制到仓库中
	copy(path, PATH_WAREHOUSE+'/'+root_name, ''  )
	
def update( owm_path1, owm_path2, mid_path ):
	print("发现文件更新：\t",owm_path1)
	list_todo.append( path_todo(owm_path1,owm_path2) ) #复制到仓库中
	list_todo.append( path_todo(owm_path1,PATH_UPDATE +'/' +mid_path +'/' +os.path.basename(owm_path1) ) ) #创建备份

#传入要复制的文件完整路径，目标完整路径，中间路径（用于history存档）
def copy( owm_path1, owm_path2, mid_path ):
	list_todo.append( path_todo(owm_path1,owm_path2) ) #复制到仓库中
	print("\t\t" , owm_path1 )

def copy_list( list,path1, path2, mid_path ):
	print("\t新增文件：")
	for i in list:
		copy( path1+'/'+i, path2+'/'+i, mid_path )

def delete( own_path, mid_path ):
	list_todo.append( path_todo(own_path,PATH_DEL +'/' +mid_path +'/' +os.path.basename(own_path), is_move=True ) ) #创建备份
	print("\t\t",own_path)

def delete_list( list, path, mid_path ):
	print("\t删除文件：")
	for i in list:
		delete(path+'/'+i, mid_path)

def count():
	return len(list_todo)

#开始进行真正的更新工作
def start():
	print("--开始移动--")
	for i in list_todo:
		i.do()

