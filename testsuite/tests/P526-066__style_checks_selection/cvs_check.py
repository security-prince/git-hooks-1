#! /usr/bin/env python
"""A dummy cvs_check program that passes all files.

It also prints a trace on stdout, in order to allow us to allow us
to verify that the script was called with the correct arguments
for the correct files.
"""
import sys

print "cvs_check: `%s'" % sys.argv[1]
