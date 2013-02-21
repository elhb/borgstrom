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
    #df = data_frame
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

    commits_time_list = []
    commits_messages_list = []

#    import pdb; pdb.set_trace()
    for repo in repos_data:
    
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
            except TypeError: print 'repo '+repo['name']+' has no commits, skipping ...', # EMPTY COMMIT LIST
        print 'added all the commits from repo '+repo['name']+' to lists'

    allCommitS = Series(commits_messages_list, index = commits_time_list)
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
    
    maxhour = [0,0]
    print 'hours:'
    for hour in hour_dict:
        print hour, hour_dict[hour]
        if maxhour[0] < hour_dict[hour]:
            maxhour[0] = hour_dict[hour]
            maxhour[1] = hour
    print ''
    maxday = [0,'']
    print 'days'
    for day in days_dict:
        print day, days_dict[day]
        if maxday[0] < days_dict[day]:
            maxday[0] = days_dict[day]
            maxday[1] = day
    print ''
    return 'The day of the week with the most commits is '+maxday[1]+' with '+str(maxday[0])+' commits in total.\n'+'The hour of the day with the most commits is '+str(maxhour[1])+' with '+str(maxhour[0])+' commits in total.\n'
    
if __name__ == "__main__":
    main()