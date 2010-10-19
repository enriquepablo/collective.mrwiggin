from OFS.Traversable import Traversable, _marker


old_unrestrictedTraverse = Traversable.unrestrictedTraverse

def patched_unrestrictedTraverse(self, path, default=_marker, restricted=False):
    """ """

    if isinstance(path, str):
        # Unicode paths are not allowed
        path = path.split('/')
    else:
        path = list(path)

    if path and path[-1] == 'main_template':
        path[-1] = '@@main_template'

    return old_unrestrictedTraverse(self, path, default, restricted)
