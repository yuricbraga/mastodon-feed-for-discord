import feedparser
from time import sleep
from datetime import datetime
from requests import post as postToDiscord
from json import loads as JSONParse
from pytz import UTC

strptime = datetime.strptime
lastRetrievedPath = 'last-retrieved.txt'
paramsPath = 'params.json'

def parseDate(dateText):
  return strptime(dateText, '%a, %d %b %Y %X %z')

def dateToString(date: datetime):
  return date.strftime('%a, %d %b %Y %X %z')

def JSONToDictFromFile(path=paramsPath):
  file = open(path, 'r')
  fileContent = file.read()
  file.close()

  return JSONParse(fileContent)

def generateHookBody(discordUsername, mastodonUsername, link):
  return {
    'username': discordUsername,
    'content': '{} just [posted]({}) something!'.format(mastodonUsername, link)
  }

def writeMostRecentDate(stringDate, path=lastRetrievedPath):
  file = open(path, 'w')
  file.write(stringDate)
  file.close()

def readFile(path=lastRetrievedPath):
  fileContent = ''

  try:
    file = open(path, 'r')
    fileContent = file.read()

    file.close()
  except:
    fileContent = dateToString(datetime.now(UTC))
    writeMostRecentDate(fileContent)

  if fileContent == '':
    fileContent = dateToString(datetime.now(UTC))
    writeMostRecentDate(fileContent)

  return fileContent

def filterPostsToPublish(entries, lastRetrieved):
  i = 0
  postDate = parseDate(entries[0]['published'])
  posts = []

  while (postDate > lastRetrieved):
    posts.append({
      'link': entries[i]['link'],
      'dateString': entries[i]['published']
    })
    i += 1
    postDate = parseDate(entries[i]['published'])

  return posts

def main():
  params = JSONToDictFromFile()

  # 1. retrieve entries from mastodon
  feed = feedparser.parse(params['rssUrl'])
  entries = feed['entries']

  # 2. compare which position has 'published' newer than 'lastRetrieved'
  lastRetrieved = parseDate(readFile())
  postsToPublish = filterPostsToPublish(entries, lastRetrieved)

  if len(postsToPublish) > 0:
    # 3. rewrite lastRetrieved with published
    writeMostRecentDate(postsToPublish[0]['dateString'])

    # 4. from the index until 0, post all
    for post in postsToPublish[::-1]:
      #post
      sleep(5)
      postToDiscord(params['webhookUrl'], json=generateHookBody(params['botUsername'], params['messageNickname'], post['link']))

if __name__ == "__main__":
  main()