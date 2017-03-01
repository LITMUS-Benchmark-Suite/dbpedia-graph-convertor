import glob, sys, os
import matplotlib.pyplot as plt
import numpy as np


def build_graph(name_of_file):

    all_files = glob.glob(os.getcwd() + "/z_ttl/*.ttl")
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
        print("Processing file : %s" % each.split("/")[-1])
        _file = open(each, "r")
        for line in _file:
            count+=1        
            if line[0]=='#':
                pass
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
                obj = obj.strip('"')
                dic_props[sub].append((pred, obj))

    #Writing the graph to file now.
    f = open(name_of_file, "w")
    f.write('<graph id="G" edgedefault="undirected">\n')
    #Writing all the nodes which have properties
    for each in dic_props:
        f.write('\t<node id="%d">\n'%(dic_nodes[each]))
        for each_pair in dic_props[each]:    
            f.write('\t\t<data key="%s">%s</data>\n'%(each_pair[0], each_pair[1]))
        f.write('\t</node>\n')
    
    #Writing all the nodes which don't have any properties
    for each in dic_nodes:
        if each not in dic_props:
            f.write('\t<node id="%d"/>\n'%(dic_nodes[each]))

    #Witing all the edges            
    for each in dic_edges:
        f.write('\t<edge id="%d" source="%d" target="%d">\n'%(_id, each[0], each[2]))
        _id+=1
        f.write('\t\t<data key="label">%s</data>\n'%(each[1]))
        f.write('\t</edge>\n')

    f.write("</graph>\n")
    

if __name__ == "__main__":
    build_graph("test.graphML")



"""
m = []
for each in dic_props:
    m.append(len(dic_props))

plt.hist(np.asarray(m))
plt.show()
"""


