#!/usr/bin/env python
"""
cookbook.py

Generate RST and IPYNB source files for IPython cookbook

"""
import os
import glob
import argparse
import IPython.nbformat.current as nbformat
import subprocess


def main():
    p = argparse.ArgumentParser(usage=__doc__.lstrip())
    args = p.parse_args()

    files = list(sorted(glob.glob('cookbook/*.py')))
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
    print("\nConverting %s..." % os.path.basename(fn))
    py_fn = os.path.abspath(fn)
    ipynb_fn = os.path.splitext(py_fn)[0] + '.ipynb'
    rst_fn = os.path.splitext(py_fn)[0] + '.rst'

    if os.path.isfile(rst_fn):
        if os.stat(rst_fn).st_mtime > os.stat(py_fn).st_mtime:
            print("Already up-to-date.")
            return

    with open(py_fn, 'rb') as py_f, open(ipynb_fn, 'wb') as ipynb_f:
        py = py_f.read().decode('utf-8')
        nb = nbformat.reads(py, 'py')
        nbformat.write(nb, ipynb_f, 'ipynb')

    ret = subprocess.call(['ipython', 'nbconvert', '--to', 'rst', ipynb_fn],
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
