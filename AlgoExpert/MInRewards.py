# https://www.algoexpert.io/questions/Min%20Rewards
# solution 1
# O(n)  time | O(n) space
def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in range(len(scores))]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in reversed(range(len(scores) - 1)):
		if scores[i] > scores[i + 1]:
			rewards[i] = max(rewards[i], rewards[i+1] + 1)
	return sum(rewards)

#solution 2

# O(n^2) time | O(n) space
def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in scores]
	for i in range(1, len(scores)): #to compare with previous element
		j = i - 1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1 # if current element > previous, increase count by 1
		else:
			while j >= 0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j], rewards[j+1] + 1) #if reward is equql to prev and cur update prev by 1
				j -= 1
	#return max(rewards)
	return sum(rewards)