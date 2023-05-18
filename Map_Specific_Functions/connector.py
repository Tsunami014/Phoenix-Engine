#This file is meant to be for using in all of your external files. Make a file (like locks.py) and use this structure by importing the file.
#Full documentation on how to use later in the file.

noms = {'FOWExternals': '',}

class EventListener(object):
    def __init__(self, name):
        self.suffix = noms[name]
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
    
    def _run(self, i, otherself):
        try:
            return i(otherself) + ';'
        except Exception as e:
            return '00some error occured with the %s function in externals!! Error: %s;' % (str(i), str(e))
    
    def event(self, type, otherself):
        endcode = ';'
        for t in self.all_funcs.keys():
            if t in type:
                for i in self.all_funcs[t]:
                    end = str(i)[str(i).index(' ')+1:str(i).index(' ', str(i).index(' ')+1)][-1]
                    if end == '2':
                        if self.suffix == '2':
                            endcode += self._run(i, otherself)
                    else:
                        if self.suffix == '':
                            endcode += self._run(i, otherself)
        return endcode[1:-1]
