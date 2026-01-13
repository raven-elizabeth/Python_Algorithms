from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    # Returns dictionary containing each node with its value being the shortest possible distance to it from source node
    def find_shortest_distances(self, source_node):
        if source_node not in self.graph:
            return None

        # Create dictionary to track distance from start node
        # Set all to infinity initially as currently unknown
        distances_from_source_node = {node: float("inf") for node in self.graph}
        # Initialize root node as 0 (already at start)
        distances_from_source_node[source_node] = 0

        # Create priority queue to sort distance values (heapify converts tuple list to pq)
        priority_queue = [(0, source_node)]
        heapify(priority_queue)

        ## Track already visited nodes with a set
        visited_nodes = set()

        ## Use while loop to search neighbouring nodes
        # while pq is not empty...
        while priority_queue:
            # heappop finds min distance and removes from pq
            curr_distance, curr_node = heappop(priority_queue)

            # Track visited nodes
            if curr_node not in visited_nodes:
                visited_nodes.add(curr_node)

            # Search neighbouring nodes to find smallest distance
            for neighbour, weight in self.graph[curr_node].items():
                # Set current distance from start
                new_distance_from_node1 = curr_distance + weight

                # Check if new distance is shorter than what is already recorded for this neighbour
                if new_distance_from_node1 < distances_from_source_node[neighbour]:
                    # If so, replace old distance to recognise shorter possible route
                    distances_from_source_node[neighbour] = new_distance_from_node1
                    # Then re-add this node to the pq so this new possible route can be checked
                    heappush(priority_queue, (new_distance_from_node1, neighbour))

        return distances_from_source_node

    # Find each node's preceding node in its shortest route from source (returns dictionary)
    def find_predecessors(self, distances_from_source_node):
        predecessors = {node: None for node in self.graph}

        # For each node's shortest distance from source...
        for node, distance in distances_from_source_node.items():
            # For each node's neighbour...
            for neighbor, weight in self.graph[node].items():
                # If the distance + neighbour's weight (next poss step) is equal to the shortest distance for that neighbour...
                if distance + weight == distances_from_source_node[neighbor]:
                    # Mark this node as that neighbour's predecessor
                    predecessors[neighbor] = node

        return predecessors