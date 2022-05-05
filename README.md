# backup-tool
基于文件修改时间对比的备份工具，编写目的是为了下班时将今天产生的所有文件（分布于多个盘），快速备份进指定目录，并能将修改/删除的文件特地标注留一份存档，万一过两天误删误改，可以再回来重新翻出来用
### 用途
- 每天下班时备份今天下载的所有文件文档，各种工作项目文件
- 备份手机里的照片文件资料

### 使用方法
1. 先执行一次backup-tool.py文件，  会在当前目录下生成几个文件夹，并且会尝试安装唯一需要安装的库 pywin32
2. 如果安装pywin32的命令失效，请手动开启命令行用` pip3 install pywin32 `来安装该库
3. 将想要进行备份的文件夹，创建一个快捷方式，然后把快捷方式放进本项目的 《要同步的快捷方式》 文件夹下即可
4. 执行backup-tool.py文件，即会开始搜寻文件并备份存储到项目路径下的 《warehouse》 文件夹内

### 项目介绍
1. 开发环境是python3.7 ，win10 ，不可用于linux（因为移动文件的功能调用了win32的库）
2. 需要额外安装pywin32 ，程序用到了它的一条函数来将快捷方式文件解析成实际路径
3. 主要核心逻辑位于backup-tool.py文件内，Lib文件夹内存放了项目各个功能的底层实现代码
4. history文件夹，在同步时删除的文件都会被移动进history文件夹
