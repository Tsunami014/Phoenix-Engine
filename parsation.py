import game as s

g = s.Game()

while True:
    txt = input('> ')
    for i in g.syns.keys():
        m = g.get_closest_matches(i, txt)
        if len(m) != 0:
            for j in m:
                txt = txt.replace(j, g.syns[i])
                
    doc = s.nlp(txt)
    trees = [g.to_tree(sent.root) for sent in doc.sents]
    for t in trees:       
        if type(t) == tuple:
            if len(s.GCM(t[0], ['help'], cutoff=s.cutoff, n=1)) != 0:
                continue
            elif g.prev_action != None:
                doc = s.nlp("%s %s" % (g.prev_action, t[0]))
                t = [g.to_tree(sent.root) for sent in doc.sents][0]
            else:
                print("Sorry, you need to specify an action.")
                continue
                
        print(g.parse(t))