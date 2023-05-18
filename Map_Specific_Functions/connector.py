#This file is meant to be for using in all of your external files. Make a file (like locks.py) and use this structure by importing the file.
#Full documentation on how to use later in the file.

class EventListener(object):
    def __init__(self, name):
        if name == 'FOWExternals':
            try:
                import FOWExternals
            except:
                import Map_Specific_Functions.FOWExternals
        elif name == 'Ancient Egypt':
            try:
                import Ancient_Egypt
            except:
                import Map_Specific_Functions.Ancient_Egypt
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
                    except Exception as e:
                        endcode += '00some error occured with the %s function in externals!! Error: %s;' % (str(i), str(e))
        return endcode[1:-1]
