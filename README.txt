This repository contains the Sphinx source for the SciPy website
(http://www.scipy.org/).

After cloning this repository, run

    $ git submodule init
    $ git submodule update

to get the Sphinx theme used.

The source is in the `www` directory, `cd` there, then the following
commands apply:

To make a local build of the website

    $ make html

To build and upload the site (requires push access to deployment repo on github).

    $ make deploy

To test external links from the site

    $ make linkcheck


CI setup
--------

The deployment is set up following instructions at 
https://developer.github.com/guides/managing-deploy-keys/
http://docs.travis-ci.com/user/encrypting-files/

To re-create the setup: first, create ssh deployment key:

    $ cd .ci
    $ ssh-keygen -f deploy-key    # <- press enter to give empty password

Then, add deploy-key.pub public key as a deployment key to the *deployment repo*.
(Note that this repository is a different one than this source repository.)

Install travis utility (needs ruby):

    $ gem install travis

Remove any old keys from Travis-CI (via the web interface -- More options ->
Settings -> Environment variables).

Encrypt keyfile and remove the unencrypted one:

    $ travis encrypt-file -r pv/scipy.org-new deploy-key
    $ rm deploy-key

Edit .travis.yml and update the openssl environment variable names.

See .travis.yml for the rest.
Finally, commit everything:

    $ git add .travis.yml .ci/deploy-key.enc .ci/deploy-key.pub
    $ git commit

