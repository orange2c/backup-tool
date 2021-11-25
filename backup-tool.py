import os

try: #引入这个模块是为了解析快捷方式文件，找到指向的实际路径
    import win32com.client  
except:
    os.system("pip install pywin32")
    import win32com.client  

import Lib.warehouse as warehouse #这个文件用于创建几个备份所需文件夹
import Lib.move as move             #复制移动文件的主要操作
from  Lib.directory import directory  #这是个用于取文件名，取路径名，列出当前路径下文件等功能的类
from  Lib.Compare import find_different #这个函数比较简单，传入两个列表，返回交集差集
import Lib.log as log

#输入一个快捷方式文件，返回实际地址
def link2path(link):
    shell = win32com.client.Dispatch("WScript.Shell")  
    shortcut = shell.CreateShortCut(link)  
    return shortcut.Targetpath

history_path = move.init( warehouse.WAREHOUSE, warehouse.HISTORY ) #初始化move类需要的路径信息
#log_history = log.creat( 'log.txt' )
log_history = log.creat( history_path + '/log.txt' )

#获取所有快捷方式，并转化为实际路径
roots = []
for link in directory( warehouse.FROM ).ls_files_own :
    roots.append( link2path(link) )
print("待同步：  ",roots)


def walk_tree( pc_path, house_path, mid ):
    print("检测",pc_path)
    pc = directory(pc_path)
    house = directory(house_path )
    the_dirs  = find_different(pc.ls_dirs, house.ls_dirs  )
    the_files = find_different(pc.ls_files, house.ls_files  )
    #print("相同文件们：",the_files.sames)
    
    if the_files.news !=None: 
        log_history.add( pc_path,  list(the_files.news ), file_new=True)
        move.copy_list( the_files.news, pc.my_path, house.my_path,mid)#添加新增文件
    if the_files.dels !=None: 
        log_history.add( house_path,  list(the_files.dels ),file_delete=True)
        move.delete_list( the_files.dels, house.my_path,mid ) #删除失效文件
    if the_dirs.news !=None: 
        log_history.add( pc_path,  list(the_dirs.news ),dir_new=True)
        move.copy_list( the_dirs.news, pc.my_path, house.my_path,mid)#添加新增文件夹
    if the_dirs.dels !=None: 
        log_history.add( house_path,  list(the_dirs.dels ), dir_delete=True)
        move.delete_list( the_dirs.dels, house.my_path,mid ) #删除失效文件夹

    if the_files.sames != None: #遍历所有相同文件，比较最后修改时间是否相同,不同则更新
        all_move = []
        for i in the_files.sames:
            if pc.find_time( i ) != house.find_time( i ):
                all_move.append(i)
                move.copy( pc.own_path(i), house.own_path(i), '' )
        if all_move != [] :  log_history.add( pc_path,  list(all_move ), file_update=True)
                
    if the_dirs.sames != None:
    #遍历所有相同文件夹,  由于修改文件后，上两层外的文件夹仍然会保持以前的修改时间，所以必须进入所有文件夹逐个比较
        for i in the_dirs.sames:
            walk_tree( ( pc.my_path+'/'+i ),  ( house.my_path+'/'+i ), mid+'/'+i  )
                
    
for i in roots:
    print("\n\n\n进入快捷方式：\t",i)
    root_one = directory(i) #用该路径创建一个路径计算类，该类会拆分并计算各种路径名称
    house_find = warehouse.find(root_one.my_name) #寻找仓库内是否有同名文件

    #如果不存在该文件夹，则整体复制，然后continue
    if not house_find : 
        print("不存在文件夹的备份，开始复制",root_one.my_path)
        move.add_root(root_one.my_path) 
        log_history.add( root_one.my_path,   root_house.my_path, root_new=True)
        continue
    root_house = directory( house_find )
    
    #如果存在，则进入遍历比较
    walk_tree( root_one.my_path, root_house.my_path, os.path.basename(root_house.my_path) )

if move.count() == 0:
    print("\n\n\n\t--没有文件变动--\n\n\n\n")

else:
    move.start() #将上面生成的所有操作都执行
    log_history.save()  #将所有操作记录的log保存

os.system('pause')