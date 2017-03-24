# Makefile for Sphinx documentation
#

DEPLOY_REPO   = git@github.com:pv/scipy.org-html
DEPLOY_BRANCH = master

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d _build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  make deploy                 to deploy the generated pages"
	@echo "  make html                   to make standalone HTML files"
	@echo "  make linkcheck              to check if external links work"

clean:
	-rm -rf _build/*

deploy: html
	rm -rf build/deploy
	git clone $(DEPLOY_REPO) build/deploy
	git -C build/deploy checkout --orphan tmp
	-git -C build/deploy branch -D $(DEPLOY_BRANCH)
	git -C build/deploy checkout --orphan $(DEPLOY_BRANCH)
	git -C build/deploy reset --hard
	git -C build/deploy clean -f -d -x
	rsync -a _build/html/ build/deploy/
	touch build/deploy/.nojekyll
	git -C build/deploy add .
	git -C build/deploy commit -m "Doc rebuild"
	git -C build/deploy push -f origin $(DEPLOY_BRANCH)

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) _build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in _build/linkcheck/output.txt."
