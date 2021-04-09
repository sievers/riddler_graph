import numpy as np
def check_graph(mat):
    #figure out if there's a path from the first node to the last
    #node in a given ordered graph, with connections defined by the
    #2D matrix mat. 
    vec=np.zeros(mat.shape[0])
    vec[0]=1 #light up the first node
    while(True):
        #light up nodes connected to currently active nodes
        vec_new=mat@vec  
        vec_new[vec_new>0]=1
        #print(vec_new)
        if vec_new[-1]>0: #if the last node lights up, we won and can get to work.
            return True
        if np.sum(np.abs(vec_new-vec))==0: #if no new nodes light up, we've lost
            return False
        vec=vec_new #update


#set up a graph with nodes connected as per the puzzler
nnode=9
links=[[0,1],[1,2],[0,3],[1,4],[2,5],[3,4],[4,5],[3,6],[4,7],[5,8],[6,7],[7,8]]
nedge=len(links)
ngood=0
nbad=0

#loop through all possible directions of the graph
for i in range(2**nedge):
    mat=np.eye(nnode) #we start with eye since once a node is active, it stays active
    
    #loop through all possible orderings of the graph.  We'll take the binary 
    #representation of i which direction each edge points
    for j in range(nedge):
        if ( (i>>j)&1): #this is a fast way to get the jth binary digit of i.
            mat[links[j][1],links[j][0]]=1
        else:
            mat[links[j][0],links[j][1]]=1
    if check_graph(mat):
        ngood=ngood+1
    else:
        nbad=nbad+1
        
print('we can get to work ',ngood/(ngood+nbad)*100,' percent of the time, or ',ngood,' out of ',ngood+nbad,' ways.')
