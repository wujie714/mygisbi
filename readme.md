
本项目为通用的API接口开发项目，开发的接口用于 大屏显示系统（www.jiudingmap.com），根据大屏系统所需要的数据来开发接口

一、下载项目
>git clone https://github.com/wujie714/mygisbi.git

二、安装依赖
>pip install uv
>cd mygisbi
>uv sync

三、运行项目
到指定环境：linux
>source .venv/bin/activate
windows
>.venv\Scripts\activate

>cd server
>meta migrate
>meta run

接口可以 浏览器上访问和调试：
https://beta.utilmeta.com/localhost/data?local_node=http://127.0.0.1:8000/ops

四、映射外网地址
>cd frp
修改：frpc.toml 中的：name、customDomains中对应的值

[[proxies]]
name = "001"
type = "http"
localIP = "127.0.0.1"
localPort = 8000
customDomains = ["001.frp.fahua.vip"]

>runfrpc.bat

注意：
env.py 中 DJANGO_ALLOWED_HOSTS 中添加 001.frp.fahua.vip

五、登录 www.jiudingmap.com 进行开发


六、关于数据结构调整：
修改完成数据结构后：

>meta makemigrations
>meta migrate