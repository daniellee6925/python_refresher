import queue


def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        node = q.get()  # q.pop(0)
        if node not in visited:  # if we haven't visited the node
            order.append(node)  # append the node to the visit order
            visited.add(node)  # append the node to the visited set
            for neighbor in graph[node]:  # loop through all neighbor nodes
                if (
                    neighbor not in visited
                ):  # if we haven't visited the node, add it to the queue
                    q.put(neighbor)

    return order


def order_dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    order = []
    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            order.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


def order_dfs_recursive(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs_recursive(graph, node, visited))

    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(order_bfs(graph, "A"))
    print(order_dfs(graph, "A"))
