from secrets import reddit

count = 1
for submission in reddit.subreddit('entrpreneur').top(limit=10, time_filter='week'):
	print("%d.\t%s" % (count, submission.title))
	count += 1
