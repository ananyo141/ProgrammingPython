#!/usr/bin/env python3
# Code a searcher by overloading the candidate method of the Searcher class

import mimetypes
from visitor import SearchVisitor

class MimeSearcher(SearchVisitor):
    testexts = skipexts = []
    
    def __init__(self, search_key, filetype='text', trace=2):
        SearchVisitor.__init__(self, search_key, trace)
        self.filetype=filetype
        self.matches = []
    def candidate(self, filename):
        content_type, encoding = mimetypes.guess_type(filename)
        return (content_type and
                content_type.split('/')[0] == self.filetype and
                encoding is None)
    def visitmatch(self, filepath, text):
        SearchVisitor.visitmatch(self, filepath, text)
        self.matches.append(filepath)

if __name__ == '__main__':
    import sys
    try:
        search_key, filetype, directory = sys.argv[1:]
    except ValueError:
        sys.exit("Usage: mimesearcher.py search_key filetype directory")

    mime = MimeSearcher(search_key, filetype, trace=2)
    mime.run(directory)
    print('-' * 60)
    print(f"Found {mime.scount} matches out of {mime.fcount} files")
    for match in mime.matches: print(repr(mime.context), '=>', match)

