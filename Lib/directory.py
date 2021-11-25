
import os
import time
import Lib.warehouse as warehouse



#路径类
class directory:
    
    my_path = ''    #本身所在完整路径
    my_name = ''    #本文件夹名称
    mid_path = ''   #与根文件夹的相对路径

    ls_files = []	#本路径下的所有文件，文件名
    ls_files_own = []	#本路径下的所有文件，完整路径 
    ls_dirs = []	#本路径下的所有文件夹，文件夹名称
    ls_dirs_own = []	#本路径下的所有文件夹，完整路径  
    
    time = ''   #本文件夹修改日期

    #传入本文件夹内文件名，返回其时间
    def find_time(self, file_name):
        file_path = self.my_path + '/' + file_name
        #print("查找时间：",time.localtime(os.stat(file_path).st_mtime))
        return time.localtime(os.stat(file_path).st_mtime)


    #传入本文件夹内文件名，返回其完整路径
    def own_path(self, path_name):
        return self.my_path + '/' + path_name
    
    #返回本文件夹下是不是没东西了
    def is_null(self):
        if self.ls_dirs is not None and self.ls_files is not None:
            return False
        return True

    def __init__(self , mypath)-> None: #传入文件夹路径
        self.my_path = mypath
        self.my_name = os.path.basename(mypath)
        for (dirpath, dirnames, filenames) in os.walk(self.my_path):

            self.ls_files =  filenames
            self.ls_dirs = dirnames

            x = []
            for i in filenames:
                x.append( mypath+'/'+i )
            self.ls_files_own = x  #原来的写法有个bug，新的对象中的own列表出现了上个对象的内容，就加了个x当中转,就好了
            x = []
            for dir in dirnames:
                x.append( mypath+'/'+dir )
            self.ls_dirs_own = x

            break #walk函数会遍历每一个文件夹，在第一个循环后退出，则只查找当前文件夹内的
        
        self.time = time.localtime(os.stat(mypath).st_mtime)
    
    

