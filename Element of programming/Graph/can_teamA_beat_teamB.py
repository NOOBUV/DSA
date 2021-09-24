import collections
"""basically this question is of simple dfs the question asks whether,
     teamA can reach teamB or not?"""
"""dfs and bfs both can be used code is below"""


def can_teamA_beat_teamB(matches, teamA, teamB):
    def buildGraph():
        winning_team = 0
        losing_team = 1
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match[winning_team]].add(match[losing_team])
        return graph

    def dfs(graph, start, dest, visited=set()):
        if start == dest:
            return True
        elif start in visited or start not in graph:
            return False
        visited.add(start)
        return any(dfs(graph, team, dest, visited) for team in graph[start])

    def bfs(graph, start, dest, visited=set()):
        visited.add(start)
        queue = [start]
        while queue:
            curr_team = queue.pop(0)
            if curr_team == dest:
                return True
            for team in graph[curr_team]:
                if team not in visited:
                    visited.add(team)
                    queue.append(team)
        return False

    return (dfs(buildGraph(), teamA, teamB))
