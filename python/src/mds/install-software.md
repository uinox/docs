### 1. 安装python3.10.4

1. 安装依赖

        yum -y groupinstall "Development tools"
        yum install -y ncurses-devel gdbm-devel xz-devel sqlite-devel tk-devel uuid-devel readline-devel bzip2-devel libffi-devel 

2. 安装openssl

        下载openssl1.1.1: wget https://www.openssl.org/source/openssl-1.1.1n.tar.gz --no-check-certificate

        tar -zxf openssl-1.1.1n.tar.gz
        cd openssl-1.1.1n

        设置安装目录 可以自定义 但是要记住，后面会用到

        ./Configure --prefix=/usr/local/openssl
        make -j
        make install

2. 安装python3.10.4

        下载python3.10.4: 

        wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz --no-check-certificate

        安装：

        tar xvzf Python-3.10.4.tgz
        cd Python-3.10.4
        ./configure --prefix=/home/dev/python3 --with-openssl=/usr/local/openssl --with-openssl-rpath=auto
        make -j && make altinstall

        配置环境变量：

        ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
        ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3


4. 非必要-配置pip源

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


### 2. 安装sqlite

        删除原有sqlite3
        yum remove sqlite3
        下载sqlite3
        wget https://www.sqlite.org/2022/sqlite-autoconf-3380300.tar.gz
        tar -zxvf sqlite-autoconf-3380300.tar.gz
        cd sqlite-autoconf-3380300
        ./configure --prefix=/usr/local/sqlite
        mv /usr/bin/sqlite3 /usr/bin/sqlite3.bk
        ln -s /usr/local/sqlite/bin/sqlite3 /usr/bin/sqlite3
        mv /usr/include/sqlite3.h /usr/include/sqlite3.h.bak
        mv /usr/include/sqlite3ext.h /usr/include/sqlite3ext.h
        ln -s /usr/local/sqlite/include/sqlite3.h /usr/include/sqlite3.h
        ln -s /usr/local/sqlite/include/sqlite3ext.h /usr/include/sqlite3ext.h

