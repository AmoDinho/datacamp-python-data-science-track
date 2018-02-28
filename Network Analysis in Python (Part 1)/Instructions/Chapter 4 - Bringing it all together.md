# Chapter 4 - Bringing it all together
## Characterizing the network (II)
Let's continue recalling what you've learned before about node importances, by plotting the degree distribution of a network. This is the distribution of node degrees computed across all nodes in a network.
### INSTRUCTIONS
100XP
Plot the degree distribution of the GitHub collaboration network G. Recall that there are four steps involved here:
Calculating the degree centrality of G.
Using the .values() method of G and converting it into a list.
Passing the list of degree distributions to plt.hist().
Displaying the histogram with plt.show().

## Characterizing the network (III)
The last exercise was on degree centrality; this time round, let's recall betweenness centrality!
A small note: if executed correctly, this exercise may need about 5 seconds to execute.
### INSTRUCTIONS
100XP
Plot the betweenness centrality distribution of the GitHub collaboration network. You have to follow exactly the same four steps as in the previous exercise, substituting nx.betweenness_centrality() in place of nx.degree_centrality().

## MatrixPlot
Let's now practice making some visualizations. The first one will be the MatrixPlot. In a MatrixPlot, the matrix is the representation of the edges.
### INSTRUCTIONS
100XP
Make a MatrixPlot visualization of the largest connected component subgraph, with authors grouped by their user group number.
First, calculate the largest connected component subgraph by using the nx.connected_component_subgraphs(G) inside the provided sorted() function. Python's built-in sorted() function takes an iterable and returns a sorted list (in ascending order, by default). Therefore, to access the largest connected component subgraph, the statement is sliced with [-1].
Create the MatrixPlot object h. You have to specify the parameters graph and node_grouping to be the largest connected component subgraph and 'grouping', respectively.
Draw the MatrixPlot object to the screen and display the plot.
## ArcPlot
Next up, let's use the ArcPlot to visualize the network. You're going to practice sorting the nodes in the graph as well.
Note: this exercise may take about 4-7 seconds to execute if done correctly.
### INSTRUCTIONS
100XP
Make an ArcPlot of the GitHub collaboration network, with authors sorted by degree. To do this:
Iterate over all the nodes in G, including the metadata (by specifying data=True).
In each iteration of the loop, calculate the degree of each node nwith nx.degree() and set its 'degree' attribute. nx.degree()accepts two arguments: A graph and a node.
Create the ArcPlot object a by specifying two parameters: the graph, which is G, and the node_order, which is 'degree', so that the nodes are sorted.
Draw the ArcPlot object to the screen.

## CircosPlot
Finally, you're going to make a CircosPlot of the network!
### INSTRUCTIONS
100XP
Make a CircosPlot of the network, again, with GitHub users sorted by their degree, and grouped and coloured by their 'grouping' key. To do this:
Iterate over all the nodes in G, including the metadata (by specifying data=True).
In each iteration of the loop, calculate the degree of each node nwith nx.degree() and set its 'degree' attribute.
Create the CircosPlot object c by specifying three parameters in addition to the graph G: the node_order, which is 'degree', the node_grouping and the node_color, which are both 'grouping'.
Draw the CircosPlot object to the screen.


## Finding cliques (I)
You're now going to practice finding cliques in G. Recall that cliques are "groups of nodes that are fully connected to one another", while a maximal clique is a clique that cannot be extended by adding another node in the graph.
### INSTRUCTIONS
100XP
Count the number of maximal cliques present in the graph and print it.
Use the nx.find_cliques() function of G to find the maximal cliques.
The nx.find_cliques() function returns a generator object. To count the number of maximal cliques, you need to first convert it to a list with list() and then use the len() function. Place this inside a print() function to print it.




## Finding cliques (II)
Great work! Let's continue by finding a particular maximal clique, and then plotting that clique.
### INSTRUCTIONS
100XP
Find the author(s) that are part of the largest maximal clique, and plot the subgraph of that/one of those clique(s) using a CircosPlot. To do this:
Use the nx.find_cliques() function to calculate the maximal cliques in G. Place this within the provided sorted() function to calculate the largest maximal clique.
Create the subgraph consisting of the largest maximal clique using the .subgraph() method and largest_clique.
Create the CircosPlot object using the subgraph G_lc (without any other arguments) and plot it.


## Finding important collaborators
Almost there! You'll now look at important nodes once more. Here, you'll make use of the degree_centrality() and betweenness_centrality() functions in NetworkX to compute each of the respective centrality scores, and then use that information to find the "important nodes". In other words, your job in this exercise is to find the user(s) that have collaborated with the most number of users.
INSTRUCTIONS
0XP
INSTRUCTIONS
0XP
Compute the degree centralities of G. Store the result as deg_cent.
Compute the maximum degree centrality. Since deg_cent is a dictionary, you'll have to use the .values() method to get a list of its values before computing the maximum degree centrality with max().
Identify the most prolific collaborators using a list comprehension:
Iterate over the degree centrality dictionary deg_cent that was computed earlier using its .items() method. What condition should be satisfied if you are seeking to find user(s) that have collaborated with the most number of users? Hint: It has do to with the maximum degree centrality.
Hit 'Submit Answer' to see who the most prolific collaborator(s) is/are
## Characterizing editing communities
You're now going to combine what you've learned about the BFS algorithm and concept of maximal cliques to visualize the network with an ArcPlot.
The largest maximal clique in the Github user collaboration network has been assigned to the subgraph G_lmc.
### INSTRUCTIONS
100XP
Go out 1 degree of separation from the clique, and add those users to the subgraph. Inside the first for loop:
Add nodes to G_lmc from the neighbors of G using the .add_nodes_from() method and .neighbors() methods.
Using the .add_edges_from(), method, add edges to G_lmcbetween the current node and all its neighbors. To do this, you'll have create a list of tuples using the zip() function consisting of the current node and each of its neighbors. The first argument to zip()should be [node]*len(G.neighbors(node)), and the second argument should be the neighbors of node.
Record each node's degree centrality score in its node metadata.
Do this by assigning nx.degree_centrality(G_lmc)[n] to G_lmc.node[n]['degree centrality'] in the second for loop.
Visualize this network with an ArcPlot sorting the nodes by degree centrality (you can do this using the keyword argument node_order='degree centrality').

## Recommending co-editors who have yet to edit together
Finally, you're going to leverage the concept of open triangles to recommend users on GitHub to collaborate!
### INSTRUCTIONS
100XP
Compile a list of GitHub users that should be recommended to collaborate with one another. To do this:
In the first for loop, iterate over all the nodes in G, including the metadata (by specifying data=True).
In the second for loop, iterate over all the possible triangle combinations, which can be identified using the combinations()function with a size of 2.
If n1 and n2 do not have an edge between them, a collaboration between these two nodes (users) should be recommended, so increment the (n1), (n2) value of the recommended dictionary in this case. You can check whether or not n1 and n2 have an edge between them using the .has_edge() method.
Using a list comprehension, identify the top 10 pairs of users that should be recommended to collaborate. The iterable should be the key-value pairs of the recommended dictionary (which can be accessed with the .items() method), while the conditional should be satisfied if countis greater than the top 10 in all_counts. Note that all_counts is sorted in ascending order, so you can access the top 10 with all_counts[-10].

