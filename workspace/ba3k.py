fin = open('data/rosalind_ba3k.txt', 'r')
fout=open('output/rosalind_ba3k.txt', 'w')
adj={}
reverse_adj={}

reads=[]
for line in fin.readlines():
    reads.append(line.replace('\n',''))
k=len(reads[0])
patterns=[]
for r in reads:
    prefix=r[:-1]
    suffix=r[1:]
    if not(prefix in patterns):
        patterns.append(prefix)
    if not(suffix in patterns):
        patterns.append(suffix)
for pattern in patterns:
    adj[pattern]=[]
    reverse_adj[pattern]=[]
for r in reads:
    adj[r[:-1]].append(r[1:])

for v in adj.keys():
    list_temp=adj[v]
    for v1 in list_temp:
        if v1 in reverse_adj.keys():
            reverse_adj[v1].append(v)
        else:
            reverse_adj[v1]=[]
            reverse_adj[v1].append(v)

#print(adj)
#print(reverse_adj)
contig=''
for node0 in adj.keys():
    #print(node0,'node0')
    if (not(adj[node0]==[]) and (not(len(adj[node0])== 1 and len(reverse_adj[node0])==1))):
        for node1 in adj[node0]:
            #print(node1,'node1')
            contig=node0[:]
            contig=contig+node1[-1]
            if not(adj[node1]==[]):
                #print(node1, adj[node1],reverse_adj[node1],'!@1@!')
                if not(len(adj[node1])== 1 and len(reverse_adj[node1])==1):
                    print(contig)
                    fout.write(contig+'\n')
                    continue
                else:
                    node2=adj[node1][0]
                    #print(node2,'node2')
                    contig=contig+node2[-1]
                    #print(node2, adj[node2],reverse_adj[node2],'!@@!')
                    while (not(adj[node2]==[]) and (len(adj[node2])==1) and (len(reverse_adj[node2])==1)):
                        node2=adj[node2][0]
                        contig=contig+node2[-1]
                        #print(node2,'nextnode')
                    fout.write(contig+'\n')
                    print(contig)
            else:
                fout.write(contig+'\n')
                print(contig)
                continue
fin.close()
fout.close()