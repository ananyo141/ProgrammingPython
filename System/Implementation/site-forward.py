#!/usr/bin/env python3
# Create redirection page for all the html files in a site directory
import os, shutil

homeDir    = os.environ.get('HOME')
assert homeDir, "home directory not found"
SERVER     = 'www.taste-movies.webnode.in'
SITE_DIR   = homeDir + '/playground/'
OUTPUT_DIR = homeDir + '/betaCode/site_relocation/'
TEMPLATE   = homeDir + '/betaCode/template.html'
SITE_DIR, OUTPUT_DIR, TEMPLATE = map(os.path.normpath, (SITE_DIR, OUTPUT_DIR, TEMPLATE))
print(f"{homeDir = }, {SITE_DIR = }, {OUTPUT_DIR = }, {TEMPLATE = }")

template = open(TEMPLATE).read().replace('$server$', SERVER)
for dirname, subdirs, filenames in os.walk(SITE_DIR):
    os.makedirs(os.path.join(OUTPUT_DIR, os.path.relpath(dirname, SITE_DIR)), exist_ok=True)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        relpath  = os.path.relpath(filepath, SITE_DIR)
        newpath  = os.path.join(OUTPUT_DIR, relpath)
        print(f'Updating {newpath}...')
        if filename.endswith('.html') or filename.endswith('.htm'):
            with open(newpath, 'w') as file:
                substitution = template.replace('$file$', filename)
                substitution = substitution.replace('$filepath$', relpath)
                file.write(substitution)
        else: shutil.copy(filepath, newpath)
print("Site folder updated at %s" % OUTPUT_DIR)

