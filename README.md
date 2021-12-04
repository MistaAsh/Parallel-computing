## Wec_Systems_Parallel_computing
My submission for the Parallel Computing problem in the WeC recruitments. Ashish Bharath (201CS208)

<br>

For the completion of this track I have chosen to use the `multiprocessing` module of Python of module over the equally viable Cuda and OpenMP.

<br>

# **Task 1:** Finding sum of an array

My approach to calculating the sum of an array using multiprocessing involved slicing the array into 'k' (in code, 4) sub-arrays.

These sub-arrays were then individually passed through to different processes which serially calculated the sum of the respective sub-arrays.

The sums of these individual sub-arrays were then added to a `multiprocessing.Value` object which acts like a wrapper communicating between different processes and helps gather the sums of the different sub-arrays to give the required output.

<br>

# **Task 2:** Finding shortest distance from a given node

**Without multiprocessing:** my approach to solve a question like this would be to use the `breadth first search (bfs)` method. 
In the bfs method, we first create a dictionary of lists with each key in the dictionary representing a node and the corresponding list an array of it's immediate neighbours. As we traverse to each of it's neighbours, we mark the node as visited and evaluate it's distance from the source as the `distance[prev] + 1`.

**With multiprocessing:** to include multiprocessing, we will be using the `multiprocessing.Pool` class which helps to create and manage multiple processes at the same time. Here, we use the same basic algorithm of BFS, but with each level of the graph we traverse, we call a seperate pool to calculate the distances of its immediate neighbours. 

To make sure the data we update the individual changes to the *visited* and *distance* arrays, we use the `multiprocessing.Array` class which, similar to 'Value', acts as a wrapper around the different pools, communicating between every runiing pool