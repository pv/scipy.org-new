# <markdowncell>

# Mayavi: Install python stuff from source
# ======================================================================
#
# Following <http://www.enthought.com/enthought/wiki/GrabbingAndBuilding>,
# you have to build/install VTK 5.0 and a few python extensions from
# sources.
# 
# All needed installation information for a given python module or VTK can
# be reached on its webpage.
# 
# For the impatient, these informations are resumed here.
# 
# Note about configure script: If you don't specify the destination where
# the packages will be installed, they will be installed by defaut in
# /usr/local.
# 
# We make the choice here to install them in a personnal directory, say
# \~/Mayavi2. So we set the environment variable DESTDIR to \~/Mayavi2,
# and will refer it later as DESTDIR:
# 
# Under sh shell-like, type:
# 
# <codecell>


export DESTDIR=~/Mayavi2

# <markdowncell>

# Under csh shell-like, type:
# 
# <codecell>


setenv DESTDIR ~/Mayavi2

# <markdowncell>

# Is is also supposed that you download and uncompress all tarball sources
# in a specific directory, named src/, for example.
# 
# ### Installing python2.3/python2.4
# 
# Download Python-2.3.5.tar.bz2 at
# <http://www.python.org/download/releases/2.3.5> or Python-2.4.3.tar.bz2
# at <http://www.python.org/download/releases/2.4.3> and untar it in src/:
# 
# <codecell>


cd src && tar xvfj Python-2.4.3.tar.bz2

# <markdowncell>

# Then run:
# 
# <codecell>


cd Python-2.4.3/ && ./configure --enable-shared --enable-unicode=ucs4 --prefix=$DESTDIR

# <markdowncell>

# Then you can make & make install:
# 
# <codecell>


make && make install

# <markdowncell>

# ### Installing VTK 5.0
# 
# Download vtk-5.0.0.tar.gz and vtkdata-5.0.0.tar.gz at
# <http://public.kitware.com/VTK/get-software.php> and untar them in src/:
# 
# <codecell>


cd src/ && tar xvfz vtk-5.0.0.tar.gz && tar xvfz vtkdata-5.0.0.tar.gz

# <markdowncell>

# Note: cmake package must be installed before proceed.
# 
# Run:
# 
# <codecell>


cd VTK && ccmake .

# <markdowncell>

# to create the required Makefile.
# 
# Press on "c" to configure.
# 
# Then press "enter" on the selected item to toggle flag.
# 
# You should specify some information, notably about some libraries
# location (tcl/tk libs + dev packages and python2.3/python2.4 you have
# just installed) if ccmake does not find them, and the destination (set
# it to DESTDIR).
# 
# Don't forget to set flag "VTK\_WRAP\_PYTHON" to on (and "VTK\_WRAP\_TCL"
# if you want to use Tcl/Tk):
# 
# <codecell>


BUILD_EXAMPLES                   ON
BUILD_SHARED_LIBS                ON
CMAKE_BACKWARDS_COMPATIBILITY    2.0
CMAKE_BUILD_TYPE
CMAKE_INSTALL_PREFIX             DESTDIR
VTK_DATA_ROOT                    DESTDIR/VTKData
VTK_USE_PARALLEL                 OFF
VTK_USE_RENDERING                ON
VTK_WRAP_JAVA                    OFF
VTK_WRAP_PYTHON                  ON
VTK_WRAP_TCL                     ON

# <markdowncell>

# Press "c" to continue configuration:
# 
# <codecell>


PYTHON_INCLUDE_PATH             *DESTDIR/include/python2.4
PYTHON_LIBRARY                  *DESTDIR/lib/libpython2.4.so
TCL_INCLUDE_PATH                */usr/include/tcl8.4
TCL_LIBRARY                     */usr/lib/libtcl8.4.so                                            
TK_INCLUDE_PATH                 */usr/include/tcl8.4
TK_LIBRARY                      */usr/lib/libtk8.4.so
VTK_USE_RPATH                   *OFF
BUILD_EXAMPLES                   ON
BUILD_SHARED_LIBS                ON
CMAKE_BACKWARDS_COMPATIBILITY    2.0
CMAKE_BUILD_TYPE                 
CMAKE_INSTALL_PREFIX             DESTDIR
VTK_DATA_ROOT                    DESTDIR/VTKData
VTK_USE_PARALLEL                 OFF
VTK_USE_RENDERING                ON
VTK_WRAP_JAVA                    OFF
VTK_WRAP_PYTHON                  ON
VTK_WRAP_TCL                     ON

# <markdowncell>

# Note: you can press "t" to get more configuration options.
# 
# Press "c" and then "g" to exit configuration, then type:
# 
# <codecell>


make && make install

# <markdowncell>

# ### Installing wx-Python2.6
# 
# Download wxPython-src-2.6.3.2.tar.gz at
# <https://sourceforge.net/project/showfiles.php?group_id=10718> and untar
# it in src/:
# 
# <codecell>


cd src/ && tar xvfz wxPython-src-2.6.3.2.tar.gz

# <markdowncell>

# Note: You should have GTK 2 installed i.e. you should have libgtk-2.6.\*
# \`and\` libgtk2.6.\*-dev packages installed.
# 
# Then run:
# 
# <codecell>


cd wxPython-src-2.6.3.2/ && ./configure --enable-unicode --with-opengl --prefix=$DESTDIR

# <markdowncell>

# Then you can do:
# 
# <codecell>


make; make -C contrib/src/animate; make -C contrib/src/gizmos; make -C contrib/src/stc

# <markdowncell>

# or follow instructions on wx-Python2.6 webpage, creating a little script
# which runs automatically the commands above.
# 
# Then install all:
# 
# <codecell>


make install; make -C contrib/src/animate install ; make -C contrib/src/gizmos install; make -C contrib/src/stc install

# <markdowncell>

# To build python modules:
# 
# <codecell>


cd wxPython

# <markdowncell>

# and run:
# 
# <codecell>


./setup.py build_ext --inplace --debug UNICODE=1

# <markdowncell>

# and install them:
# 
# <codecell>


./setup.py install UNICODE=1 --prefix=$DESTDIR

# <markdowncell>

# ### Installing scipy 0.5 & numpy 1.0
# 
# Download scipy-0.5.1.tar.gz at <http://www.scipy.org/Download>
# 
# Before installing scipy, you have to download and install:
# 
# `* numpy-1.0.tar.gz (http://sourceforge.net/project/showfiles.php?group_id=1369&package_id=175103)`
# 
# `* Atlas libraries (you could install it with your packages manager, no need to build it in src/)`
# 
# No special option are required to install these python extensions.
# 
# To install these packages in our \$DESTDIR, simply change directory and
# type:
# 
# <codecell>


./setup.py install --prefix=$DESTDIR

# <markdowncell>

# ### That's all, folks !
# 
# Before installing !MayaVi2, you have to set some environment variables,
# to tell !MayaVi2 where python extensions can be found.
# 
# Under sh shell-like, type:
# 
# <codecell>


export PYTHONPATH=$DESTDIR:$PYTHONPATH
export LD_LIBRARY_PATH=$DESTDIR:$LD_LIBRARY_PATH

# <markdowncell>

# Under csh shell-like, type:
# 
# <codecell>


setenv PYTHONPATH ${DESTDIR}:${PYTHONPATH}
setenv LD_LIBRARY_PATH ${DESTDIR}:${LD_LIBRARY_PATH}

# <markdowncell>

# * * * * *
# 
# CategoryInstallation
# 
