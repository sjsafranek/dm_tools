'''
import dm_tools

tracker = dm_tools.InitativeTracker()

tracker.add('stefan', 10)
tracker.add('patrick', 15)
tracker.add('drew', 8)

'''

from dm_tools import linked_lists


class InitativeTracker(object):

    def __init__(self):
        self.index = 0
        self.characters = {}
        self._order = []

    def _buildList(self):
        self._order = [
            {
                'name': i,
                'initative': self.characters[i]['initative'],
                'active': self.characters[i]['active']
            } for i in self.characters
        ]
        self._order.sort(key= lambda x: x['initative'])

    def add(self, character, initative):
        self.characters[character] = {
            'active': True,
            'initative': initative
        }
        self._buildList()

    def remove(self, character):
        # del self.characters[character]
        self.characters[character]['active'] = False
        self._buildList()

    def next(self, attempt=1):
        if attempt > len(self._order):
            return None
        if self.index >= len(self._order):
            self.index = 0
        self.index += 1
        if not self._order[self.index-1]['active']:
            return self.next(attempt+1)
        return self._order[self.index-1]
