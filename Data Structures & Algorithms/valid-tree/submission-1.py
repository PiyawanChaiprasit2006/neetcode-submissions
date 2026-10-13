class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        edges.sort()
        seen = set()

        links = defaultdict(list)

        def dfs(node, parent):
            seen.add(node)

            for link in links[node]:
                if link == parent:
                    continue

                if link in seen:
                    return False

                if not dfs(link, node):
                    return False
            return True

        for e in edges:
            node = e[0]
            link = e[1]

            links[node].append(link)
            links[link].append(node)

        return dfs(0, -1) and len(seen) == n




        