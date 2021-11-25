'''
负责创建log
'''
import time
import json
import os
class KEY_NAME():
    root_new = "新的同步文件夹"
    file_new = "新增文件"
    dir_new = "新增路径"
    file_delete = "删除文件"
    dir_deletr = "删除路径"
    file_update = '更新文件'


#日志文件类
class creat():
    logname = '' #log文件路径
    count_update_file = 0 
    text = {
        "time" : time.strftime("%Y-%m-%d  %H:%M", time.localtime())
    }

    def __init__(self, filename) -> None:
        self.logname = filename

    def save(self):
        print(self.text)
        json_log = json.dumps(self.text, indent=4,ensure_ascii=False)
        print("\n",json_log, "\n")
        with open(self.logname, 'w') as f:
            f.write(json_log)

    def add(self, path, name, root_new=False, file_new=False, dir_new=False, file_delete=False, dir_delete=False, file_update=False):
        if root_new: my_type = KEY_NAME.root_new
        if file_new: my_type = KEY_NAME.file_new
        if file_delete: my_type = KEY_NAME.file_delete
        if dir_new: my_type = KEY_NAME.dir_new
        if dir_delete: my_type = KEY_NAME.dir_deletr
        if file_update: my_type = KEY_NAME.file_update

        if my_type not in self.text:  self.text[my_type] = []
        i = { os.path.normpath(path) : name}
        self.text[my_type].append(i)
        
def log_read(file): #传入文件名，将其读出并以数组方式存储
    with open(file,'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data
