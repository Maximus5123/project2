#from bs4 import BeautifulSoup
import praw

#import requests

#html_text=requests.get('https://www.reddit.com/r/movies/comments/155ag1m/official_discussion_oppenheimer_spoilers/').text
    
#log in to app:
reddit = praw.Reddit(client_id ='4iuS6Vi6nMblW8NXKFudrQ',  client_secret = '4kkKBJ4_rkD4Bh6ijoiAqQd1MPoTYQ', user_agent = 'Maximus<red>')

#hot for submission on subreddit[top ten redits hots for oppenheimer]
#subs = reddit.subreddit('Oppenheimer').hot(limit =10)
#for summit in subs:
    #print(summit.title)
    #code to retrive comment section 
    
post_url = "https://www.reddit.com/r/movies/comments/155ag1m/official_discussion_oppenheimer_spoilers/"

#post_id = post_url.split('/')[-2]

#post = reddit.submission(id=post_id)


post = reddit.submission(url = post_url)  
    #print(f"Post Content:\n{post.selftext}")
#print(f"Title: {post.title}")
#print("----------------------------------------------------")
#print(f"Post Content:\n{post.selftext}")
#print("----------------------------------------------------")
#print(f"Upvotes: {post.ups}")
    #print(f"Downvotes: {post.downs}")
#print(f"Number of Comments: {post.num_comments}")
    #print(f"Posted by: {post.author}")
    #print(f"Posted on: {post.created_utc}")
#except praw.exceptions.PRAWException as e:
 #  print("-------------------------------------")
#    print("The post has no upvotes.")

submission = reddit.submission(url=post_url)
comment_list = []

# Access the comments
submission.comments.replace_more(limit=5)  # This loads all the comments
comments = submission.comments.list()

 #Print the comments
for comment in comments:
    output = comment.body

    comment_list.append(output)
print(comment_list)     
with open ("output.txt", 'w',encoding='utf-8') as file:  
    for cmt in comment_list:
       file.write(f'{cmt} \n ')
      
      
