class Tree:
    def __init__(self, root):
        """
        Initialize a Tree with a root node.
        `root` should be a dictionary with keys: 'tag_name', 'id', 'text_content', and 'children'.
        """
        self.root = root

    def breadth_first_traversal(self):
        """
        Perform a breadth-first traversal (level-order) and return
        a list of node 'id' or any other attribute values in order.
        """
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            result.append(node.get('id'))
            nodes_to_visit.extend(node.get('children', []))

        return result

    def depth_first_traversal(self):
        """
        Perform an iterative depth-first (preorder) traversal and return a
        list of node 'id' values in preorder.
        """
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            result.append(node.get('id'))
            # Preorder depth-first: add children to the front so we dive deep.
            nodes_to_visit = node.get('children', []) + nodes_to_visit

        return result

    def get_element_by_id(self, target_id):
        """
        Find and return the node whose 'id' matches target_id using
        depth-first search. Returns None if no match found.
        """
        return self._dfs_search(self.root, target_id)

    def _dfs_search(self, node, target_id):
        # Check the current node
        if node.get('id') == target_id:
            return node
        # Recurse through children
        for child in node.get('children', []):
            found = self._dfs_search(child, target_id)
            if found:
                return found
        return None

    def get_element_by_id_bfs(self, target_id):
        """
        Alternate finder using breadth-first search.
        """
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node.get('id') == target_id:
                return node
            nodes_to_visit.extend(node.get('children', []))

        return None
