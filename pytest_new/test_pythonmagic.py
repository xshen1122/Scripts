# coding: utf-8
'''
python-magic is a Python interface to the libmagic file
type identification library. libmagic identifies file types by
checking their headers according to a predefined list of file types.
This functionality is exposed to the command line
by the Unix command file.


'''
import magic
f = magic.Magic(uncompress=True)
f.from_file('testdata/test.gz')
f = magic.Magic(mime=True, uncompress=True)
f.from_file('testdata/test.gz')
