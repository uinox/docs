### rust环境安装
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    source $HOME/.cargo/env
### mdbook安装
    cargo install mdbook

### 初始化一本书
    mdbook init [my-first-book]

### 开发环境
    mdbook serve [path] [-p 8080] [-n 0.0.0.0]
    
### 生产环境
    mdbook build

### 清理
    mdbook clean