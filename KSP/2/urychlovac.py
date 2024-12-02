f = open("01.in")
p_max, num_of_settings, num_of_conversions =  [int(x) for x in f.readline().split()]
print("protonové číslo nejtěžšího prvku, se kterým umí urychlovač pracovat: ", p_max)
print("počet nastavení urychlovače: ", num_of_settings)
print("počet přeměn, na které má Sára čas", num_of_conversions)


graf = [[0 for x in range(num_of_settings)] for i in range(num_of_settings)]
print(graf)

for line in f:
    before, after, goodness = [int(x) for x in line.split()]
    print(before, after, goodness)
    if graf[before][after] < goodness:
        graf[before-1][after-1] = goodness

print(graf)

dist = [1e7] * num_of_settings
dist[0] = 0
sptSet = [False] * num_of_settings

def maxDistance(node, dist, sptSet):
    # Initialize maximum distance for next node
    max = 0
    max_index = -1

    # Search not nearest vertex not in the
    # shortest path tree
    for v in graf[node]:
        if dist[v] > max and sptSet[v] == False:
            max = dist[v]
            max_index = v

    if not max_index == -1:
        return max_index
    else:
        return -1

for cout in range(num_of_settings):

    # Pick the minimum distance vertex from
    # the set of vertices not yet processed.
    # u is always equal to src in first iteration
    u = maxDistance(cout, dist, sptSet)

    if maxDistance == -1:
        continue

    # Put the minimum distance vertex in the
    # shortest path tree
    sptSet[u] = True

    # Update dist value of the adjacent vertices
    # of the picked vertex only if the current
    # distance is greater than new distance and
    # the vertex in not in the shortest path tree
    for v in range(num_of_settings):
        if (graf[u][v] > 0 and
            sptSet[v] == False and
                dist[v] > dist[u] + graf[u][v]):
            dist[v] = dist[u] + graf[u][v]

            print(dist)
