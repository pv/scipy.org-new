#!/usr/bin/env python
"""
cookbook.py

Generate RST and IPYNB source files for IPython cookbook

"""
import os
import glob
import argparse
import subprocess
import shutil

import IPython.nbformat.current as nbformat


def main():
    p = argparse.ArgumentParser(usage=__doc__.lstrip())
    args = p.parse_args()

    files = list(sorted(glob.glob('cookbook/source/*.py')
                        + glob.glob('cookbook/source/*.ipynb')))
    for fn in files:
        generate(fn)

    with open('cookbook/index.rst', 'wb') as f:
        f.write('========\n'
                'Cookbook\n'
                '========\n\n')
        f.write('.. toctree::\n'
                '   :maxdepth: 1\n\n')
        for fn in files:
            f.write("   %s\n" % os.path.splitext(os.path.basename(fn))[0])


def generate(fn):
    bn = os.path.splitext(os.path.basename(fn))[0]

    py_fn = os.path.join('cookbook', bn + '.py')
    ipynb_fn = os.path.join('cookbook', bn + '.ipynb')
    rst_fn = os.path.join('cookbook', bn + '.rst')

    if os.path.isfile(rst_fn):
        if os.stat(rst_fn).st_mtime > os.stat(fn).st_mtime:
            return

    print("\nConverting %s..." % os.path.basename(fn))

    if fn.endswith('.py'):
        shutil.copyfile(fn, py_fn)
        with open(py_fn, 'rb') as py_f, open(ipynb_fn, 'wb') as ipynb_f:
            py = py_f.read().decode('utf-8')
            nb = nbformat.reads(py, 'py')
            nbformat.write(nb, ipynb_f, 'ipynb')
    elif fn.endswith('.ipynb'):
        shutil.copyfile(fn, ipynb_fn)
        with open(ipynb_fn, 'rb') as ipynb_f, open(py_fn, 'wb') as py_f:
            nb = nbformat.read(ipynb_f, 'ipynb')
            py_f.write(nbformat.writes(nb, 'py').encode('utf-8'))

    ret = subprocess.call(['ipython', 'nbconvert', '--to', 'rst', os.path.basename(ipynb_fn)],
                          cwd=os.path.dirname(ipynb_fn))
    if ret != 0:
        raise RuntimeError("RST conversion failed!")

    COOKBOOK_PRE = """
.. raw:: html

   <div style="float: right;">

:download:`[py] <%(py)s>` :download:`[ipynb] <%(ipynb)s>`

.. raw:: html

   </div>
"""

    pre = COOKBOOK_PRE % dict(py=os.path.basename(py_fn),
                              ipynb=os.path.basename(ipynb_fn))

    with open(rst_fn, 'rb') as f:
        txt = f.read()

    txt = pre + "\n\n" + txt

    with open(rst_fn, 'wb') as f:
        f.write(txt)


if __name__ == "__main__":
    main()
