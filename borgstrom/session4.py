#
import requests
import getpass
import sys
from dateutil import parser
import datetime
from pandas import Series
from pandas import DataFrame
import calendar

def main():
    data_frame = get_data_frame()
    df = data_frame
    print getWDandH(data_frame)

def get_credentials():
    sys.stdout.write('Please enter your usrname: ')
    usrname = raw_input()
    password = getpass.getpass()
    return [usrname, password]

def get_data_frame():

    [usrname, password] = get_credentials()

    repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(usrname, password))
    repos_data = repos.json()

    allCommitS = {}

    for repo in repos_data:

        commits_time_list = []
        commits_messages_list = []
    
        try: pass#sys.stderr.write( 'processing user: ' + repo['name'] + ' ...\n' )
        except TypeError: print 'Error: probably faulty usrname and password.\n'
        
        # get the commits
        commit_url = repo['commits_url'][:-6] 
        commits = requests.get(commit_url, auth=(usrname, password))
        commits_data = commits.json()
        
        for commit in commits_data:
            try:
                commits_time_list.append(parser.parse(commit['commit']['author']['date']))
                commits_messages_list.append(commit['commit']['message'])
            except TypeError: pass # EMPTY COMMIT LIST

        if len(commits_messages_list): allCommitS[repo['name']] = (Series(commits_messages_list, index = commits_time_list))

    dataframe = DataFrame(allCommitS)
    return dataframe

def getWDandH(df):
    days = df.index.dayofweek
    hours = df.index.hour
    counts = df.count(1)
    days_dict = {}
    hour_dict = {}
    
    for [day,[hour,count]] in zip(days,zip(hours,counts)):
        #print calendar.day_name[day], hour, count
        try: days_dict[calendar.day_name[day]] += count
        except KeyError: days_dict[calendar.day_name[day]] = count
        try: hour_dict[hour] += count
        except KeyError: hour_dict[hour] = count
    
    print 'hours'
    for hour in hour_dict:
        print hour, hour_dict[hour]
        
    print 'days'
    for day in days_dict:
        print day, days_dict[day]
    
    return ''
    
if __name__ == "__main__":
    main()