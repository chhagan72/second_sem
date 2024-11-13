import numpy as np
# Create 3x3 matrix
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
total_sum =np.sum(m)
print("\n Sum of all elements: ", total_sum)

col_wise_sum = np.sum(m,axis=0)
print("\n The column wise sum of matrix: ", col_wise_sum)

row_wise_sum = np.sum(m,axis=1)
print("\n The row wise sum of matrix: ", row_wise_sum)

CREATE TABLE IF NOT EXISTS `order_details` (  `id` int NOT NULL AUTO_INCREMENT,  `fname` text NOT NULL,  `lname` text NOT NULL,  `email` text NOT NULL,  `mobil` int NOT NULL,  `address1` text NOT NULL,  `address2` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,  `city` text NOT NULL,  `state` text NOT NULL,  `zip` int NOT NULL,  `pname` text NOT NULL,  `pprice` int NOT NULL,  PRIMARY KEY (`id`)) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;