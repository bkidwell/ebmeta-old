#!/bin/bash

d=`dirname $0`
d=`readlink -f $d/..`

pushd $d >/dev/null

pandoc --standalone README.md>README.html

popd >/dev/null