#This file is meant to be for using in all of your external files. Make a file (like locks.py) and use this structure by importing the file.
#Full documentation on how to use later in the file.

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
    
    def event(self, type, otherself):
        endcode = ';'
        for t in self.all_funcs.keys():
            if t in type:
                for i in self.all_funcs[t]:
                    try:
                        endcode += i(otherself) + ';'
                    except:
                        endcode += '00some error occured with the %s function in externals!!;' % str(i)
        return endcode[1:-1]
