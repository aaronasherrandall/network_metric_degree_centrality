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
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# add a list of friends to each user
# set each user friends's property to an empty list
friendships = {user["id"]: [] for user in users}

# Add loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
	friendships[i].append(j) # add j as a friend of user i
	friendships[j].append(i) # add i as a friend of user j

# What's the average number of connections?
# First, find total number of connections by 
# summing up the lengths of all friends lists

def number_of_friends(user):
	"""how many friends does _user_ have"""
	user_id = user["id"]
	friend_ids = friendships[user_id]
	return len(friend_ids)

total_connections = sum(number_of_friends(user)
						for user in users)       #24

num_users = len(users) # length of the user list
avg_connections = total_connections	/ num_users

# Find the most connected people
# Sort them from "most friends" to "least friends"
# create a list of (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
					for user in users]

num_friends_by_id.sort(									
		key=lambda id_and_friends: id_and_friends[1],   
		reverse=True)								    

# with this,
# we can identify people who are central to the network
# we computed the network metric degree centrality
"""[(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), 
(0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]"""

# creating a "People you may know" suggester
# suggest that a user might know the friends of their friends
# iterate over their friends and collect the friends’ friends
def foaf_ids_bad(user):
	"""foaf is short for "friend of a friend" """
	return [foaf_id
			for friend_id in friendships[user["id"]]
			for foaf_id in friendships[friend_id]]

print(friendships[0]) # [1, 2]
print(friendships[1]) # [0, 1, 2]
print(friendships[2]) # [0, 1, 3]

# produce a count of mutual friends
# exclude people already known to the user:

from collections import Counter

def friend_of_friends(user):
	user_id	= user["id"]
	return Counter(
		foaf_id
		for friend_id in friendships[user_id] # for each of my friends
		for foaf_id	in friendships[friend_id] # find their friends
		if foaf_id != user_id                 # who aren't me
		and foaf_id	not in friendships[user_id] # and aren't my friends
	)

print(friend_of_friends(users[3]))