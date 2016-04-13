from cluster import *

'''
Example usage/testing of cluster.py
'''
def test_distance(a, b):
    return abs(a - b)

def calc_centroid(l):
    return sum(l) / float(len(l))

if __name__ == "__main__":
    big_ol_data = [5, 6, 7, 1, 2, 5, 5, 5, -1, 10, 55, 1, 60, 58, 59, 1, 1, 1, 1]
    kcluster = KMeansCluster(distanceMetric = test_distance, calculateCentroid = calc_centroid, data = big_ol_data, force_k_bins = True)
    results = kcluster.run()
    print "=============== DONE ============="
    print results
