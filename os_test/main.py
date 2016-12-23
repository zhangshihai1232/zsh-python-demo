from os.path import join, dirname, abspath, pardir, exists

base = dirname(__file__)
print __file__

parent = abspath(join(base, pardir))
print pardir
print base
print join(base, pardir)
print parent
# includes = [parent] + [join(parent, base, subdir) for subdir in ('utils',)]
# if exists(join(parent, base, 'include')):
#     includes.append(join(parent, base, 'include'))
