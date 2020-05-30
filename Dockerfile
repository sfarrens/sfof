FROM ubuntu

LABEL Description="SFoF"

ARG DEBIAN_FRONTEND=noninteractive
ARG CC=gcc-9
ARG CXX=g++-9

RUN apt-get update && \
    apt-get install -y gcc-9 g++-9 && \
    apt-get install -y git cmake libboost-all-dev libcfitsio-dev && \
    apt-get clean

RUN cd home && \
    git clone https://github.com/sfarrens/sfof  && \
    cd sfof && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install
