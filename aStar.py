import pywikibot as pw
import node
from heapq import *

site = pw.Site('en', 'wikipedia')  # The site we want to run our bot on
site.login()

def runAStar(start, end, qw):    # start/end are nodes for a*
    self = set();
    start = node.Node(start, None, qw)
    start.calcFn(qw)
    start.totalPathWeight = 0      # distance from start    
    open = [start]
    closed = set()
    # print(end.title())
    while open:
        curr = heappop(open)    # gets current node by getting max f(n)
        if curr.page == end:         # if neighbor = goal, return the path
                return getPath(curr)
        elif set(linked_page.title() for linked_page in curr.page.linkedPages()).__contains__(end.title()):
                print("checked for link:P")
                endN = node.Node(end, curr, qw)
                return getPath(endN)
        closed.add(curr)        # add curr to closed

        # print("CURR: ", curr)

        for neighbor in getNeighbors(curr, qw):
            if neighbor.page == end:         # if neighbor = goal, return the path
                return getPath(neighbor)
            if neighbor in closed:      # if curr has already been visited go next
                continue
            if set(ne_page.title() for ne_page in neighbor.page.linkedPages()).__contains__(end.title()):
                print("checked for link in neighbors:P")
                lastNode = node.Node(end, neighbor, qw)
                return getPath(lastNode)
            else:
                # neighbor.totalPathWeight = neighbor.parent.totalPathWeight + calculateCost(neighbor)
                try:
                    #if in heap and neigh f val is less, change neighbor.
                    ind = open.index(neighbor)
                    neighbor.calcFn()
                    if neighbor.f < open[ind].f:
                        open[ind] = neighbor
                except:
                    #if not in heap, add it to heap.
                    heappush(open, neighbor)
    
                

def getNeighbors(root, qw):
    neighbors = []
    links = root.page.linkedPages()
    for aLink in links:
        neigh = node.Node(aLink, root, qw)
        neigh.calcFn(qw)
        nam = neigh.name.lower()
        if (not nam.startswith("list") 
            and not nam.startswith("category:") 
            and not nam.startswith("help:") 
            and not nam.startswith("template:") ):
            neighbors.append(neigh)
    neighbors.sort()
    return neighbors;

def getPath(node):
    totPath = []
    totPath.append(node)
    while(node.parent is not None):
        totPath.append(node.parent)
        node = node.parent
    return totPath