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

    for fn in sorted(glob.glob('cookbook/*.py')):
        generate(fn)

def generate(fn):
    print("\nConverting %s..." % os.path.basename(fn))
    py_fn = os.path.abspath(fn)
    ipynb_fn = os.path.splitext(py_fn)[0] + '.ipynb'
    rst_fn = os.path.splitext(py_fn)[0] + '.rst'

    with open(py_fn, 'rb') as py_f, open(ipynb_fn, 'wb') as ipynb_f:
        nb = nbformat.read(py_f, 'py')
        nbformat.write(nb, ipynb_f, 'ipynb')
    ret = subprocess.call(['ipython', 'nbconvert', '--to', 'rst', ipynb_fn],
                          cwd=os.path.dirname(ipynb_fn))
    if ret != 0:
        raise RuntimeError("RST conversion failed!")

if __name__ == "__main__":
    main()
