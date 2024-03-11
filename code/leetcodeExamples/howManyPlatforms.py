# Input: arr[] = {9, 9.75, 9.8, 11, 15, 18}, dep[] = {9.25, 12, 11.25, 11.5, 19, 20} 
# Output: 3 
# Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

# Input: arr[] = {9, 9.75}, dep[] = {9.25, 12} 
# Output: 1 
# Explanation: Only one platform is needed. 
          
# 9-9.25         |
#       9.75-----|-------12
#         9.8---11.25
#             11-|---11.5
#                |                15----------19  
#                |                         18----20
# ---------------|----------------------------------------------
# 9        10 11         12 13 14 15 16 17 18 19 20

# O(2*(n-1)) -> O(n)

# - max trains = 0
# - Sort arr, dep based off of arrival
# - Create a min heap, and store first departure, create min variable
# - Loop from 1 to n and if current arrival <= min departure, push departure
# - If not, then pop min from queue
