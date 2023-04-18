#This file is meant to be for using in all of your external files. Make a file (like locks.py) and use this structure by importing the file.
#Full documentation on how to use later in the file.

"""events:
type: int - event code, unique to whether you are pushing something or going somewhere
"""

class EventListener(object):
    all_funcs = {}
    def wait(self, types):
        def main(func):
            for typ in types:
                try:
                    self.all_funcs[typ].append(func)
                except:
                    self.all_funcs[typ] = [func]
            return func
        return main
    def event(self, type):
        endcode = ';'
        if type in self.all_funcs.keys():
            for i in self.all_funcs[type]:
                endcode += i() + ';'
        return endcode[1:-1]

#if __name__ == '__main__':
    