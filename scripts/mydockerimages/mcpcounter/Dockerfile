FROM debian:bullseye

# 安装 R 以及相关依赖
RUN apt-get update && apt-get install -y \
    r-base \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev

# 设置环境变量
ENV SRC /usr/local/src
ENV BIN /usr/local/bin

WORKDIR $SRC

# 安装 R 包
RUN Rscript -e 'Sys.setenv("R_REMOTES_NO_ERRORS_FROM_WARNINGS" = "true")' && \
    Rscript -e 'install.packages("matrixStats")' && \
    Rscript -e 'install.packages("textshaping")' && \
    Rscript -e 'install.packages("pkgdown")' && \
    Rscript -e 'install.packages(c("curl","remotes"))' && \
    Rscript -e 'require("remotes");remotes::install_github("ebecht/MCPcounter", ref="master", subdir="Source")'

# 拷贝脚本文件
COPY mcpcounter.r /bin

ENV HOME /bin
WORKDIR /bin

VOLUME ['/tmp']
