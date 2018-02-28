# Chapter 3 - Structures

## Identifying triangle relationships
Now that you've learned about cliques, it's time to try leveraging what you know to find structures in a network. Triangles are what you'll go for first. We may be interested in triangles because they're the simplest complex clique. Let's write a few functions; these exercises will bring you through the fundamental logic behind network algorithms.
In the Twitter network, each node has an 'occupation' label associated with it, in which the Twitter user's work occupation is divided into celebrity, politician and scientist. One potential application of triangle-finding algorithms is to find out whether users that have similar occupations are more likely to be in a clique with one another.
### INSTRUCTIONS
100XP
Import combinations from itertools.
Write a function is_in_triangle() that has two parameters - G and n - and checks whether a given node is in a triangle relationship or not.
combinations(iterable, n) returns combinations of size n from iterable. This will be useful here, as you want combinations of size 2 from G.neighbors(n).
To check whether an edge exists between two nodes, use the .has_edge(node1, node2) method. If an edge exists, then the given node is in a triangle relationship, and you should return True.
## Finding nodes involved in triangles
NetworkX provides an API for counting the number of triangles that every node is involved in: nx.triangles(G). It returns a dictionary of nodes as the keys and number of triangles as the values. Your job in this exercise is to modify the function defined earlier to extract all of the nodes involved in a triangle relationship with a given node.
### INSTRUCTIONS
100XP
Write a function nodes_in_triangle() that has two parameters - G and n - and identifies all nodes in a triangle relationship with a given node.
In the for loop, iterate over all possible triangle relationship combinations.
Check whether the nodes n1 and n2 have an edge between them. If they do, add both nodes to the set triangle_nodes.
Use your function in an assert statement to check that the number of nodes involved in a triangle relationship with node 1 of graph T is equal to 35.


## Finding open triangles
Let us now move on to finding open triangles! Recall that they form the basis of friend recommendation systems; if "A" knows "B" and "A" knows "C", then it's probable that "B" also knows "C".
### INSTRUCTIONS
100XP
Write a function node_in_open_triangle() that has two parameters - G and n - and identifies whether a node is present in an open triangle with its neighbors.
In the for loop, iterate over all possible triangle relationship combinations.
If the nodes n1 and n2 do not have an edge between them, set in_open_triangle to True, break out from the if statement and return in_open_triangle.
Use this function to count the number of open triangles that exist in T.
In the for loop, iterate over all the nodes in T.
If the current node n is in an open triangle, increment num_open_triangles.


## Finding all maximal cliques of size "n"
Now that you've explored triangles (and open triangles), let's move on to the concept of maximal cliques. Maximal cliques are cliques that cannot be extended by adding an adjacent edge, and are a useful property of the graph when finding communities. NetworkX provides a function that allows you to identify the nodes involved in each maximal clique in a graph: nx.find_cliques(G). Play around with the function by using it on T in the IPython Shell, and then try answering the exercise.
### INSTRUCTIONS
100XP
Write a function maximal_cliques() that has two parameters - G and size - and finds all maximal cliques of size n.
In the for loop, iterate over all the cliques in G using the nx.find_cliques() function.
If the current clique is of size size, append it to the list mcs.
Use an assert statement and your maximal_cliques()function to check that there are 33 maximal cliques of size 3 in the graph T.

## Subgraphs I
There may be times when you just want to analyze a subset of nodes in a network. To do so, you can copy them out into another graph object using G.subgraph(nodes), which returns a new graph object (of the same type as the original graph) that is comprised of the iterable of nodesthat was passed in.
matplotlib.pyplot has been imported for you as plt.

### INSTRUCTIONS
100XP
Write a function get_nodes_and_nbrs(G, nodes_of_interest) that extracts the subgraph from graph G comprised of the nodes_of_interest and their neighbors.
In the first for loop, iterate over nodes_of_interest and append the current node n to nodes_to_draw.
In the second for loop, iterate over the neighbors of n, and append all the neighbors nbr to nodes_to_draw.
Use the function to extract the subgraph from T comprised of nodes 29, 38, and 42 (contained in the pre-defined list nodes_of_interest) and their neighbors. Save the result as T_draw.
Draw the subgraph T_draw to the screen.


## Subgraphs II
In the previous exercise, we gave you a list of nodes whose neighbors we asked you to extract.
Let's try one more exercise in which you extract nodes that have a particular metadata property and their neighbors. This should hark back to what you've learned about using list comprehensions to find nodes. The exercise will also build your capacity to compose functions that you've already written before.

### INSTRUCTIONS
100XP
Using a list comprehension, extract nodes that have the metadata 'occupation' as 'celebrity' alongside their neighbors:
The output expression of the list comprehension is n, and there are two iterator variables: n and d. The iterable is the list of nodes of T (including the metadata, which you can specify using data=True) and the conditional expression is if the 'occupation' key of the metadata dictionary d equals 'celebrity'.
Place them in a new subgraph called T_sub. To do this:
Iterate over the nodes, compute the neighbors of each node, and add them to the set of nodes nodeset by using the .union() method. This last part has been done for you.
Use nodeset along with the T.subgraph() method to calculate T_sub.
Draw T_sub to the screen.

