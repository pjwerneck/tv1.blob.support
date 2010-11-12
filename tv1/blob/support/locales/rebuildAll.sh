#!/bin/bash
# kudos to Products.Ploneboard for the base for this file
# ensure that when something is wrong, nothing is broken more than it should...
set -e

# first, create some pot containing anything
i18ndude rebuild-pot --pot tv1.blob.support.pot --create tv1.blob.support --merge manual.pot ..

# finally, update the po files
i18ndude sync --pot tv1.blob.support.pot  `find . -iregex '.*tv1.blob.support\.po$'|grep -v plone`

