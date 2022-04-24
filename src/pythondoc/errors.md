#### 安装python3.10.4是可能遇到的问题
### 1. Failed to build these modules: _ctypes

        sudo yum install libffi-devel python3-devel


#### 2.3 修改python源代码的安装配置文件


#### 安装python3.10.4 dev用户

1. 安装依赖

        yum -y groupinstall "Development tools"
        yum install -y ncurses-devel gdbm-devel xz-devel sqlite-devel tk-devel uuid-devel readline-devel bzip2-devel libffi-devel openssl-devel openssl11 openssl11-devel

2. 下载

        wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz

3. 编译

编译主要需要注意的问题是设置编译FLAG，以便使用最新的openssl库。

        export CFLAGS=$(pkg-config --cflags openssl11)
        export LDFLAGS=$(pkg-config --libs openssl11)

        tar xvzf Python-3.10.4.tgz
        cd Python-3.10.4

        ./configure --enable-optimizations --prefix=/home/dev/python3
        make && make altinstall


4. 配置环境变量

        vim ~/.bashrc
        最后追加
        export PATH=/home/dev/python3/bin:$PATH

        source ~/.bashrc


5. 配置pip源

        mkdir -p ~/.pip
        touch ~/.pip/pip.conf

        vim ~/.pip/pip.conf
        添加下面内容：

        [global]
        index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
        extra-index-url=
                http://pypi.douban.com/simple/
                http://mirrors.aliyun.com/pypi/simple/
        #proxy = [user:passwd@]proxy.server:port
        [install]
        trusted-host=
                pypi.tuna.tsinghua.edu.cn
                pypi.douban.com
                mirrors.aliyun.com
        ssl_verify: false


        上面配置了清华，豆瓣，阿里的源，并且关闭了ssl验证。当然如果有需要还可以设置代理,把注释掉的proxy那行放开即可。

6. 验证

        pip3 install --upgrade pip