
import os


#创建指定文件夹
FROM = '要同步的快捷方式'  #存储所有要同步的电脑文件夹的快捷方式
WAREHOUSE = 'warehouse'  #仓库
HISTORY = 'history'  #存储备份，日志

mkdir_list = [
    FROM, WAREHOUSE, HISTORY
]

#创建基础文件夹
for i in mkdir_list:
    try:
        os.makedirs(i)
    except:
        pass
try:
    os.makedirs(FROM)
    print("请在 《",FROM,"》 文件夹中放置要同步文件夹的快捷方式")
    os.exit()
except:
    pass



#传入相对路径，查找仓库内是否有同名路径，有则返回该路径，没有则返回False
def find(mid_path):
    own_path = WAREHOUSE+'/'+mid_path
    if os.path.exists(own_path):
        return own_path
    else:
        return False


