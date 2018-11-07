#!/bin/bash -l

cd $HOME/repos/charlesforsyth.github.io/
mkdocs gh-deploy --config-file $HOME/repos/cfweb/mkdocs.yml --remote-branch master
