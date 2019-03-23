from __future__ import division

# list of users; each represented by a dict
users = [
{"id": 0, "name": "Hero"},
{"id": 1, "name": "Dunn"},
{"id": 2, "name": "Sue"},
{"id": 3, "name": "Chi"},
{"id": 4, "name": "Thor"},
{"id": 5, "name": "Clive"},
{"id": 6, "name": "Hicks"},
{"id": 7, "name": "Devin"},
{"id": 8, "name": "Kate"},
{"id": 9, "name": "Klein"},
]

# friendship data; represented as a list of pairs of ids
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
			   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# add a list of friends to each user
# set each user friends's property to an empty list
for user in users:	
	user["friends"] = []

# populate the list using the friendships data
for i, j in friendships:
	#this works because users[i] is the user whose id is i
	users[i]["friends"].append(users[j]) #add j as a friend of i
	users[j]["friends"].append(users[i]) #add i as a friend of j

# What's the average number of connections?
# First, find total number of connections by summing up the lengths of all friends lists

def number_of_friends(user):
	"how many friends does {} have".format(user)
	return len(user["friends"])						# length of friend_ids list

total_connections = sum(number_of_friends(user)
						for user in users)			# 24	

num_users = len(users) # length of the user list
avg_connections = total_connections	/ num_users

print(avg_connections)

# Find the most connected people
# Sort them from "most friends" to "least friends"
# create a list of (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
					for user in users]

num_friends_by_id.sort(
		key=lambda id_and_friends: id_and_friends[1],
		reverse=True)

print(num_friends_by_id)
