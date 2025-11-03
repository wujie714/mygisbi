
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

在浏览器上访问：
https://beta.utilmeta.com/localhost/data?local_node=http://127.0.0.1:8080/ops
