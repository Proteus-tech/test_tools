#!/usr/bin/env python
import os,fnmatch
from distutils.core import setup

#
##Copy from Django setup.py
#def fullsplit(path, result=None):
#    """
#    Split a pathname into components (the opposite of os.path.join) in a
#    platform-neutral way.
#    """
#    if result is None:
#        result = []
#    head, tail = os.path.split(path)
#    if head == '':
#        return [tail] + result
#    if head == path:
#        return result
#    return fullsplit(head, [tail] + result)
## Compile the list of packages available, because distutils doesn't have
## an easy way to do this.
#packages, data_files = [], []
#root_dir = os.path.dirname(__file__)
#if root_dir != '':
#    os.chdir(root_dir)
#
#
#for dirpath, dirnames, filenames in os.walk('test_tools'):
#    # Ignore dirnames that start with '.'
#    for i, dirname in enumerate(dirnames):
#        if dirname.startswith('.'): del dirnames[i]
#    if '__init__.py' in filenames:
#        packages.append('.'.join(fullsplit(dirpath)))
#    elif filenames:
#        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
#print 'packages = ', packages
##End
#
### This is a list of files to install, and where:
### Make sure the MANIFEST.in file points to all the right 
### directories too.
### Code borrowed from wxPython's setup and config files
### Thanks to Robin Dunn for the suggestion.
### I am not 100% sure what's going on, but it works!
#def opj(*args):
#    path = os.path.join(*args)
#    return os.path.normpath(path)
#
#def find_data_files(srcdir, *wildcards, **kw):
#    # get a list of all files under the srcdir matching wildcards,
#    # returned in a format to be used for install_data
#    def walk_helper(arg, dirname, files):
#        if '.svn' in dirname:
#            return
#        names = []
#        lst, wildcards = arg
#        for wc in wildcards:
#            wc_name = opj(dirname, wc)
#            for f in files:
#                filename = opj(dirname, f)
#
#                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
#                    names.append(filename)
#        if names:
#            lst.append( (dirname, names ) )
#
#    file_list = []
#    recursive = kw.get('recursive', True)
#    if recursive:
#        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
#    else:
#        walk_helper((file_list, wildcards),
#                    srcdir,
#                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
#    return file_list
#
#files = find_data_files('test_tools/data/', '*.json')
#print 'files = ',files

setup(name='test_tools',
      version='1.1',
      description='test tools for Django',
      author='Proteus Technologies',
      author_email='team@proteus-tech.com',
      url='http://proteus-tech.com',
      include_package_data = True,
      #packages=packages,
      #data_files = files,
      packages = ['test_tools', 'test_tools.data'],
      #package_dir={'test_tools': 'test_tools'},
      #package_data={'test_tools': ['test_tools/data/*.json']},
      #data_files = [('lib/python2.7/site-packages/test_tools/data',['test_tools/data/test_current_iteration_data.json',]),
      #              ]
     )