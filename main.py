from cluster import *
import math, csv, ast

'''
Example usage/testing of cluster.py
'''
def test_distance(a, b):
    return abs(a - b)

def calc_centroid(l):
    return sum(l) / float(len(l))

def aggHMDist(a, b):
    return math.sqrt(sum([(a["map"][i][2] - b["map"][i][2])**2 for i in range(0, len(a["map"]))]))

def aggHMCentroid(l):
    cen = []
    for i in range(0, len(l[0]["map"])):
        tot = 0
        for mem in l:
            tot += mem["map"][i][2]
        cen.append( (l[0]["map"][i][0], l[0]["map"][i][1], tot / float(len(l))) )
    return {"map": cen, "treatment": "centroid", "rep": "centroid"}


if __name__ == "__main__":
    big_ol_data = [5, 6, 7, 1, 2, 5, 5, 5, -1, 10, 55, 1, 60, 58, 59, 1, 1, 1, 1]
    kcluster = KMeansCluster(distanceMetric = test_distance, calculateCentroid = calc_centroid, data = big_ol_data, force_k_bins = True)
    results = kcluster.run()
    print "=============== DONE ============="
    print results

    # big_ol_data = [ {"treatment": "t1", "rep": "r1", "map": [(0,0,5),(0,1,1),(1,0,-6),(1,1,2)]}, {"treatment": "t1", "rep": "r2", "map": [(0,0,10),(0,1,-1),(1,0,3),(1,1,4)]}, {"treatment": "t2", "rep": "r1", "map": [(0,0,50),(0,1,40),(1,0,60),(1,1,10)]} ]
    # kcluster = KMeansCluster(distanceMetric = aggHMDist, calculateCentroid = aggHMCentroid, data = big_ol_data, force_k_bins = False)
    # results = kcluster.run(num_bins = 2)
    # print "=========="
    # print "=========="
    # print results
