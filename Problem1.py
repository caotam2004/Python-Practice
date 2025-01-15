# from numpy.lib.shape_base import apply_along_axis
import numpy as np

vector_a = np.array([1,2])
vector_b = np.array([2,1])
vector_c = np.array([-2,-1])

# Tích vô hướng
dot_a_b = np.dot(vector_a,vector_b)
dot_a_c = np.dot(vector_a,vector_c)
print(f"dot_a_b = {dot_a_b}")
print(f"dot_a_c = {dot_a_c}\n")

# Tính cos góc giữa 2 vector
norma = np.linalg.norm(vector_a)
normb = np.linalg.norm(vector_b)
normc = np.linalg.norm(vector_c)

cos_ab = dot_a_b/(norma*normb)
radians_ab = np.arccos(cos_ab)
degree_ab = np.degrees(radians_ab)

cos_ac = dot_a_c/(norma*normc)
radians_ac = np.arccos(cos_ac)
degree_ac = np.degrees(radians_ac)

print(f"cos_ab = {cos_ab}\nradians_ab = {radians_ab}\ndegree_ab = {degree_ab}\n")
print(f"cos_ac = {cos_ac}\nradians_ac = {radians_ac}\ndegree_ac = {degree_ac}\n")

# Tính khoảng cách a,b a,c
dist_ab = np.linalg.norm(vector_a-vector_b)
dist_ac = np.linalg.norm(vector_a-vector_c)
print(f"dist_ab = {dist_ab}\ndist_ac = {dist_ac}")

