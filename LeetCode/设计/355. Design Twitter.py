'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-twitter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
from typing import List


class Twitter:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)
        self.totalTweet = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.totalTweet.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        arr = []
        for i in range(len(self.totalTweet) - 1, -1, -1):
            if self.totalTweet[i][0] in self.dic[userId] or self.totalTweet[i][0] == userId:
                arr.append(self.totalTweet[i][1])
            if len(arr) == 10:
                break
        return arr

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.dic[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.dic[followerId]:
            self.dic[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user = {}  # 当前系统用户字典
        self.Tid = 0  # 记录推文绝对id

    def _new_user(self, userId):
        F = {userId}  # 关注者集合，初始时关注自己
        T = collections.deque(maxlen=10)  # 推文列表，长度为10的双端队列，利用其超长即弹出特性
        self.user[userId] = {'F': F, 'T': T}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self._new_user(userId)
        self.user[userId]['T'].append((self.Tid, tweetId))  # 更新推文列表，记录(推文绝对id, 推文id)
        self.Tid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:  # 用户不存在
            return []
        Tlist = []
        for uid in self.user[userId]['F']:
            Tlist.extend(list(self.user[uid]['T']))  # 关注的推文
        T10 = heapq.nlargest(10, Tlist)  # 利用堆的性质取出最大10个
        return [T[1] for T in T10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.user:
            self._new_user(followerId)
        if followeeId not in self.user:
            self._new_user(followeeId)
        self.user[followerId]['F'].add(followeeId)  # 利用集合去重特性，省去重复关注的判断

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # 两个用户均存在，且取关的不是自己
        if followerId in self.user and followeeId in self.user and followeeId != followerId:
            self.user[followerId]['F'].discard(followeeId)


