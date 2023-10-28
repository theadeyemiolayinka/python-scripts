'''
Reddit Reply Bot
-------------------------------------------------------------
pip install praw pyenchant
'''


import praw
import enchant


def reddit_bot(sub, trigger_phrase):
   reddit = praw.Reddit(
       client_id='your_client_id',
       client_secret='your_client_secret',
       username='your_username',
       password='your_pw',
       user_agent='your_user_agent'
   )

   subreddit = reddit.subreddit(sub)
   dict_suggest = enchant.Dict('en_US')

   for comment in subreddit.stream.comments():
       if trigger_phrase in comment.body.lower():
           word = comment.body.replace(trigger_phrase, '')
           reply_text = ''
           similar_words = dict_suggest.suggest(word)
           for similar in similar_words:
               reply_text += (similar + ' ')
           comment.reply(reply_text)


if __name__ == '__main__':
   reddit_bot(sub='Python', trigger_phrase='useful bot')