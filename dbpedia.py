import glob, sys

all_files = glob.glob("*.ttl")

dic_shortcuts = {":" : "http://dbpedia.org/resource/"}

dic_shortcuts_rec = {"http://dbpedia.org/resource" : ":"}
_id = 0
dic_nodes = {}
dic_nodes_rev = {}
dic_edges = []
dic_props = {}
debug = False
count = 0
for each in all_files:
    _file = open(each, "r")
    for line in _file:
        count+=1        
        if line[0]=='#':
            pass
        if count==10000000:
            break
        if count%10000 == 0:
            print(count, sys.getsizeof(dic_nodes) + sys.getsizeof(dic_nodes_rev) + sys.getsizeof(dic_edges) + sys.getsizeof(dic_props)) 
        m = line.split(" ")
        start = None
        sub = None
        obj = None
        pred = None
        try:     
            start = dic_shortcuts_rec["/".join(m[0][1:-1].split("/")[:-1])]
            sub = start + "/" + m[0][1:-1].split("/")[-1]
        except Exception as e:
            sub = m[0]        
        
        try:
            start = dic_shortcuts_rec["/".join(m[1][1:-1].split("/")[:-1])]
            pred = start + "/" + m[1][1:-1].split("/")[-1]
        except Exception as e:
            pred = m[1]        

        try:
            start = dic_shortcuts_rec["/".join(m[2][1:-1].split("/")[:-1])]
            obj = start + "/" + m[2][1:-1].split("/")[-1]
        except Exception as e:
            obj = m[2]     

     
        debug and print(sub, "$" , pred, "$", obj)
        if sub not in dic_nodes:
        
            dic_nodes[sub] = _id
            dic_nodes_rev[_id] = sub
            _id +=1

        
        if "http" in obj:
            if obj not in dic_nodes:
                dic_nodes[obj]=_id
                dic_nodes_rev[_id] = obj
                _id+=1
            dic_edges.append((dic_nodes[sub], pred, dic_nodes[obj]))
        else:
            if sub not in dic_props:
                dic_props[sub] = []
            dic_props[sub].append((pred, obj))


