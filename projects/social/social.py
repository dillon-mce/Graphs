import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i + 1}')

        # Create friendships

        #  O(n^2) Method
        # possibleFriendships = []
        # for userID in self.users:
        #     for frientID in range(userID + 1, self.lastID + 1):
        #         possibleFriendships.append((userID, frientID))

        # random.shuffle(possibleFriendships)

        # for friendship_index in range(avgFriendships * numUsers // 2):
        #     friendship = possibleFriendships[friendship_index]
        #     self.addFriendship(friendship[0], friendship[1])

        # O(n) Method, way faster. Seems like roughly the same distribution though.
        count = 0
        loops = 0
        limit = avgFriendships * numUsers // 2

        while count < limit:
            loops += 1
            friend1 = random.randint(1, self.lastID)
            friend2 = random.randint(1, self.lastID)

            if friend1 == friend2 or (self.friendships.get(friend1) is not None and friend2 in self.friendships[friend1]):
                continue
            self.addFriendship(friend1, friend2)
            count += 1

        print(f'Took {loops} loops')

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue(userID)

        while q.size() > 0:
            v = q.dequeue()
            visited.setdefault(v, [])
            visited[v].append(v)
            for neighbor in self.friendships[v]:
                if not visited.get(neighbor):
                    visited.setdefault(neighbor, visited[v].copy())
                    q.enqueue(neighbor)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

    # for userID in sg.users:
    #     connections = sg.getAllSocialPaths(userID)
    #     percentage = (len(connections) / len(sg.users)) * 100
    #     average_degrees = 0
    #     for path in connections.values():
    #         average_degrees += len(path) - 1
    #     average_degrees /= len(connections)
        
    #     print(f'User {userID} is connected to {percentage}% of users, with an average of {average_degrees} degrees of separation.')
