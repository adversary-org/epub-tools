#!/bin/bash4

# Must be run from inside the top of the epub directory.

find . -name .DS_Store -exec rm -vf "{}" +
zip -X0 "$@" mimetype
zip -Xur9D "$@" * -x mimetype
