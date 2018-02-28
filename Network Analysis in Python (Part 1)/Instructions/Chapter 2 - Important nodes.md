# Chapter 2 - Important nodes
## Compute number of neighbors for each node
How do you evaluate whether a node is an important one or not? There are a few ways to do so, and here, you're going to look at one metric: the number of neighbors that a node has.
Every NetworkX graph G exposes a .neighbors(n) method that returns a list of nodes that are the neighbors of the node n. To begin, use this method in the IPython Shell on the Twitter network T to get the neighbors of of node 1. This will get you familiar with how the function works. Then, your job in this exercise is to write a function that returns all nodes that have mneighbors.

### INSTRUCTIONS
100XP
Write a function called nodes_with_m_nbrs() that has two parameters - G and m - and returns all nodes that have mneighbors. To do this:
Iterate over all nodes in G (not including the metadata).
Use the len() function together with the .neighbors()method to calculate the total number of neighbors that node n in graph G has.
If the number of neighbors of node n is equal to m, add n to the set nodes using the .add() method.
After iterating over all the nodes in G, return the set nodes.
Use your nodes_with_m_nbrs() function to retrieve all the nodes that have 6 neighbors in the graph T.

## Compute degree distribution
The number of neighbors that a node has is called its "degree", and it's possible to compute the degree distribution across the entire graph. In this exercise, your job is to compute the degree distribution across T.
### INSTRUCTIONS
100XP
Use a list comprehension along with the .neighbors(n)method to get the degree of every node. The result should be a list of integers.
Use n as your iterator variable.
The output expression of your list comprehension should be the number of neighbors that node n has - that is, its degree. Use the len() function together with the .neighbors() method to compute this.
The iterable in your list comprehension is the all the nodes in T, accessed using the .nodes() method.
Print the degrees.
## Degree centrality distribution
The degree of a node is the number of neighbors that it has. The degree centrality is the number of neighbors divided by all possible neighbors that it could have. Depending on whether self-loops are allowed, the set of possible neighbors a node could have could also include the node itself.
The nx.degree_centrality(G) function returns a dictionary, where the keys are the nodes and the values are their degree centrality values.
The degree distribution degrees you computed in the previous exercise using the list comprehension has been pre-loaded.
### INSTRUCTIONS
100XP
Compute the degree centrality of the Twitter network T.
Using plt.hist(), plot a histogram of the degree centrality distribution of T. This can be accessed using list(deg_cent.values()).
Plot a histogram of the degree distribution degrees of T. This is the same list you computed in the last exercise.
Create a scatter plot with degrees on the x-axis and the degree centrality distribution list(deg_cent.values()) on the y-axis.

## Shortest Path I
You can leverage what you know about finding neighbors to try finding paths in a network. One algorithm for path-finding between two nodes is the "breadth-first search" (BFS) algorithm. In a BFS algorithm, you start from a particular node and iteratively search through its neighbors and neighbors' neighbors until you find the destination node.
Pathfinding algorithms are important because they provide another way of assessing node importance; you'll see this in a later exercise.
In this set of 3 exercises, you're going to build up slowly to get to the final BFS algorithm. The problem has been broken into 3 parts that, if you complete in succession, will get you to a first pass implementation of the BFS algorithm.
### INSTRUCTIONS
100XP
Create a function called path_exists() that has 3 parameters - G, node1, and node2 - and returns whether or not a path exists between the two nodes.
Initialize the queue of cells to visit with the first node, node1. queue should be a list`.
Iterate over the nodes in queue.
Get the neighbors of the node using the .neighbors() method of the graph G.
Check to see if the destination node node2 is in the set of neighbors. If it is, return True.


## Shortest Path II
Now that you've got the code for checking whether the destination node is present in neighbors, next up, you're going to extend the same function to write the code for the condition where the destination node is not present in the neighbors.
All the code you need to write is in the else condition; that is, if node2 is not in neighbors.
### INSTRUCTIONS
100XP
Using the .add() method, add the current node node to the set visited_nodes to keep track of what nodes have already been visited.
Add the neighbors of the current node node that have not yet been visited to queue. To do this, you'll need to use the .extend() method of queue together with a list comprehension. The .extend() method appends all the items in a given list.
The output expression and iterator variable of the list comprehension are both n. The iterable is the list neighbors, and the conditional is if n is not in the visited nodes.


## Shortest Path III
This is the final exercise of this trio! You're now going to complete the problem by writing the code that returns False if there's no path between two nodes.
### INSTRUCTIONS
100XP
Check to see if the queue has been emptied. You can do this by inspecting the last element of queue with [-1].
Place the appropriate return statement for indicating whether there's a path between these two nodes.
## NetworkX betweenness centrality on a social network
Betweenness centrality is a node importance metric that uses information about the shortest paths in a network. It is defined as the fraction of all possible shortest paths between any pair of nodes that pass through the node.
NetworkX provides the nx.betweenness_centrality(G)function for computing the betweenness centrality of every node in a graph, and it returns a dictionary where the keys are the nodes and the values are their betweenness centrality measures.

### INSTRUCTIONS
100XP
Compute the betweenness centrality bet_cen of the nodes in the graph T.
Compute the degree centrality deg_cen of the nodes in the graph T.
Compare betweenness centrality to degree centrality by creating a scatterplot of the two, with list(bet_cen.values()) on the x-axis and list(deg_cen.values()) on the y-axis.


## Deep dive - Twitter network
You're going to now take a deep dive into a Twitter network, which will help reinforce what you've learned earlier. First, you're going to find the nodes that can broadcast messages very efficiently to lots of people one degree of separation away.
NetworkX has been pre-imported for you as nx.
### INSTRUCTIONS
100XP
Write a function find_nodes_with_highest_deg_cent(G) that returns the node(s) with the highest degree centrality using the following steps:
Compute the degree centrality of G.
Compute the maximum degree centrality using the max()function on list(deg_cent.values()).
Iterate over the degree centrality dictionary, deg_cen.items().
If the degree centrality value v of the current node k is equal to max_dc, add it to the set of nodes.
Use your function to find the node(s) that has the highest degree centrality in T.
Write an assertion statement that checks that the node(s) is/are correctly identified. This has been done for you, so hit 'Submit Answer' to see the result!

## Deep dive - Twitter network part II
Next, you're going to do an analogous deep dive on betweenness centrality! Just a few hints to help you along: remember that betweenness centrality is computed using nx.betweenness_centrality(G).

### INSTRUCTIONS
100XP
Write a function find_node_with_highest_bet_cent(G) that returns the node(s) with the highest betweenness centrality.
Compute the betweenness centrality of G.
Compute the maximum betweenness centrality using the max() function on list(bet_cent.values()).
Iterate over the degree centrality dictionary, bet_cent.items().
If the degree centrality value v of the current node k is equal to max_bc, add it to the set of nodes.
Use your function to find the node(s) that has the highest betweenness centrality in T.
Write an assertion statement that you've got the right node. This has been done for you, so hit 'Submit Answer' to see the result!

