Installation on Mac OSX
==================

@author Samuel Farrens

Compiler
-

At the time of writing this the current default c/c++ compiler on OSX is clang. To install this code it is highly reccommended to instead use  GNU GCC. This can be installed directly from the <a href="https://gcc.gnu.org/" target="_blank">source</a>, or using packages like <a href="https://www.macports.org/" target="_blank">MacPorts</a> or <a href="http://brew.sh/" target="_blank">Homebrew</a>.

Boost
-

If GCC is used then the Boost libraries also need to be built with GCC. This can be done (tested for boost v.1.58.0) as follows:

* Download the Boost <a href="http://sourceforge.net/projects/boost/files/boost/1.58.0/boost_1_58_0.tar.gz/download" target="_blank">source</a>.

* Unzip and untar the downloaded file.

* Inside the boost\_1\_58\_0 directory run the *bootstrap.sh* script specifying a path to where the libraries are to be installed as follows:

> ./bootstrap.sh --prefix=<PATH> --with-toolset=gcc

`e.g. >> ./bootstrap.sh --prefix=/home/boost --with-toolset=gcc`

* Upon completion a file called *project-config.jam* will be generated. Edit line 13 (*using gcc ;*) of this file as follows:

` using gcc : <VERSION> : <PATH>g++-<VERSION> : <linker-type>darwin ; `

`e.g.  using gcc : 4.9.0 : /usr/bin/g++-4.9.0 : <linker-type>darwin ; `

* Run the b2 script as follows:

> ./b2 install

Installing fof\_cluster\_finder
-

After building the Boost libraries simply run cmake and specifying the use of GCC and the path to Boost as follows:

> cmake -DBOOST_ROOT=<PATH>

`e.g. >> CC=/usr/bin/gcc-4.9.0 CXX=/usr/bin/g++-4.9.0 cmake -DBOOST_ROOT=/home/boost`
