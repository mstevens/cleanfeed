#!/usr/bin/python
#
# vim: tabstop=4 expandtab shiftwidth=4 autoindent
#
# template.py -- This is a template for new Python programs
#
# Copyright (C) 2005 Steve Crook <steve@mixmin.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

# The threshold at which we consider a URL to be excessive and blacklist it.
threshold = 50

# The file from which to read the default list of logfiles we're going to
# process.
filelist = 'logfile_list'

# A list of URL's to exclude from blacklisting.
exclude = 'exclude_list'

# The filename used to store the persistent dictionary
dbfile = 'badurl.db'

# A dictionary containing variables we need to retain between runs.
varfile = 'vars.db'

backoff_interval = 60
backoff_rate = 1
backoff_ceiling = 1000