#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# load JSON data to Mongo database

import os
import json
import pymongo
from pymongo import MongoClient

# Making Connection
uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

# database : db4
database = client["db4"]

# Created or Switched to collection
# names: worldcup2022
collection = database["worldcup2022"]

f=open('C:\\Users\\Lenovo\\worldcup2022.json')

for line in f:
    print(line)
    database = json.loads(line)
    x=collection.insert_one(database)


# In[ ]:


# 1.Create
def create_func():
    import PySimpleGUI as sg

    sg.theme('Light Green 1')  # please make your windows colorful

    layout = [
                [sg.Text('Please enter all information')],
                [sg.Text('Match Number', size=(15, 1)), sg.InputText('65', key='-MATCH-')],
                [sg.Text('Round Number', size=(15, 1)), sg.InputText('8', key='-ROUND-')],
                [sg.Text('Date UTC', size=(15, 1)), sg.InputText('2022-12-25 19:00:00Z', key='-DATE-')],
                [sg.Text('Location', size=(15, 1)), sg.InputText('Oldtrafford Stadium', key='-LOCATION-')],
                [sg.Text('Home Team', size=(15, 1)), sg.InputText('Manchester Utd', key='-HOME-')],
                [sg.Text('Away Team', size=(15, 1)), sg.InputText('Liverpool', key='-AWAY-')],
                [sg.Text('Group', size=(15, 1)), sg.InputText('Group Z', key='-GROUP-')],
                [sg.Text('Home Team Score', size=(15, 1)), sg.InputText('9', key='-HSC-')],
                [sg.Text('Away Team Score', size=(15, 1)), sg.InputText('0', key='-ASC-')],
                [sg.Submit(), sg.Cancel()]
                ]

    window = sg.Window('Mode: Create Data', layout)
    event, values = window.read()
    window.close()

    sg.Popup(event, values, values['-MATCH-'], values['-ROUND-'], values['-DATE-'],
            values['-LOCATION-'], values['-HOME-'], values['-AWAY-'],
            values['-GROUP-'], values['-HSC-'], values['-ASC-'])

    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]
    
    document = { "MatchNumber": values['-MATCH-'],
                "RoundNumber": values['-ROUND-'],
                "DateUtc": values['-DATE-'],
                "Location": values['-LOCATION-'],
                "HomeTeam": values['-HOME-'],
                "AwayTeam": values['-AWAY-'],
                "Group": values['-GROUP-'],
                "HomeTeamScore": values['-HSC-'],
                "AwayTeamScore": values['-ASC-'] }

    x = collection.insert_one(document)

# 2.Retrive All
def retriveall_func()
    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    for x in collection.find():
        print(x)
        print()

# 3.Retrive
def retrive_func()
    import PySimpleGUI as sg

    sg.theme('Dark Blue 1')  # please make your windows colorful

    layout = [
                [sg.Text('Please select criteria to specify information')],
                [sg.Text('Match Number', size=(15, 1)), sg.InputText('65', key='-MATCH-')],
                [sg.Text('Round Number', size=(15, 1)), sg.InputText('8', key='-ROUND-')],
                [sg.Text('Date UTC', size=(15, 1)), sg.InputText('2022-12-25 19:00:00Z', key='-DATE-')],
                [sg.Text('Location', size=(15, 1)), sg.InputText('Oldtrafford Stadium', key='-LOCATION-')],
                [sg.Text('Home Team', size=(15, 1)), sg.InputText('Manchester Utd', key='-HOME-')],
                [sg.Text('Away Team', size=(15, 1)), sg.InputText('Liverpool', key='-AWAY-')],
                [sg.Text('Group', size=(15, 1)), sg.InputText('Group Z', key='-GROUP-')],
                [sg.Text('Home Team Score', size=(15, 1)), sg.InputText('9', key='-HSC-')],
                [sg.Text('Away Team Score', size=(15, 1)), sg.InputText('0', key='-ASC-')],
                [sg.Submit(), sg.Cancel()]
                ]

    window = sg.Window('Mode: Retrive Specific Data', layout)
    event, values = window.read()
    window.close()

    sg.Popup(event, values, values['-MATCH-'], values['-ROUND-'], values['-DATE-'],
            values['-LOCATION-'], values['-HOME-'], values['-AWAY-'],
            values['-GROUP-'], values['-HSC-'], values['-ASC-'])

    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    query = { "MatchNumber": values['-MATCH-'],
                "RoundNumber": values['-ROUND-'],
                "DateUtc": values['-DATE-'],
                "Location": values['-LOCATION-'],
                "HomeTeam": values['-HOME-'],
                "AwayTeam": values['-AWAY-'],
                "Group": values['-GROUP-'],
                "HomeTeamScore": values['-HSC-'],
                "AwayTeamScore": values['-ASC-'] }
    documents = collection.find(query)

    for x in documents:
        print(x)
        print()

# 4.Update
def update_func()
    import PySimpleGUI as sg

    sg.theme('Dark Blue 1')  # please make your windows colorful

    layout = [
                [sg.Text('Please select match number to change')],
                [sg.Text('Match Number', size=(15, 1)), sg.InputText('65', key='-MATCH-')],
                [sg.Submit(), sg.Cancel()]
                ]

    window = sg.Window('Mode: Update Specific Data', layout)
    event, values = window.read()
    window.close()


    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    query = { "MatchNumber": values['-MATCH-']}

    layout2 = [
                [sg.Text('Please input new match number')],
                [sg.Text('New Match Number', size=(15, 1)), sg.InputText(' ', key='-MATCH2-')],
                [sg.Submit(), sg.Cancel()]
                ]
    window2 = sg.Window('Mode: Input New Data', layout2)
    event2, values2 = window2.read()
    window2.close()

    sg.Popup(event2, values2, values2['-MATCH2-'])
    #print(values2['-MATCH2-'])
    newvalue = { "$set": {"MatchNumber": values2['-MATCH2-']} }

    collection.update_one(query, newvalue)

    documents = collection.find().sort("MatchNumber")

    for x in documents:
        print(x)
        print()
        
# 5.Delete All
def deleteall_func()
    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    x = collection.delete_many({})

    print(x.deleted_count, " documents deleted.")

        
# 6.Delete
def delete_func()
    import PySimpleGUI as sg

    sg.theme('Dark Red 1')  # please make your windows colorful

    layout = [
                [sg.Text('Please select match number to delete')],
                [sg.Text('Match Number To Delete', size=(15, 1)), sg.InputText('65', key='-MATCH-')],
                [sg.Submit(), sg.Cancel()]
                ]

    window = sg.Window('Mode: Delete Specific Data', layout)
    event, values = window.read()
    window.close()


    import pymongo
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    query = { "MatchNumber": values['-MATCH-']}

    collection.delete_one(query)

    documents = collection.find().sort("MatchNumber")

    for x in documents:
        print(x)
        print()

# 7.Report
def report_func()
    import pymongo
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # Connect to Database
    uri = "mongodb+srv://surawich:10AreeratNp*@cluster0.k7k2ihc.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    database = client["db4"]
    collection = database["worldcup2022"]

    group = ['Group A', 'Group B','Group C', 'Group D','Group E', 'Group F','Group G', 'Group H', ]
    score = []

    score_a = 0
    score_b = 0
    score_c = 0
    score_d = 0
    score_e = 0
    score_f = 0
    score_g = 0
    score_h = 0

    # Retrieving and Formatting Data
    for document in collection.find():
        hts = document["HomeTeamScore"]
        ats = document["AwayTeamScore"]

        if type(hts) == int: 
            t_score = hts + ats
            grp = document["Group"]
            if grp == 'Group A':
                score_a = score_a + t_score
            elif grp == 'Group B':
                score_b = score_b + t_score
            elif grp == 'Group C':
                score_c = score_c + t_score
            elif grp == 'Group D':
                score_d = score_d + t_score
            elif grp == 'Group E':
                score_e = score_e + t_score
            elif grp == 'Group F':
                score_f = score_f + t_score
            elif grp == 'Group G':
                score_g = score_g + t_score
            else:
                score_h = score_h + t_score
        else:
            score.append(score_a)
            score.append(score_b)
            score.append(score_c)
            score.append(score_d)
            score.append(score_e)
            score.append(score_f)
            score.append(score_g)
            score.append(score_h)
            break
        
    print(group)
    print(score)


    plt.figure(figsize=[10,6], dpi=100)
    plt.bar(group,score,color='blue',align='center',width=0.5)
    plt.savefig('Worldcup2022.png')
    plt.title('Total Score Per Group in World Cup 2022',fontsize=18,color='blue')
    plt.xlabel('Group',fontsize=14,color='blue')
    plt.ylabel('Total Score',fontsize=14,color='blue')
    plt.grid(linestyle='--',axis='x')
    lines = plt.plot(group,score)
    plt.setp(lines, color='red',linewidth=2.0, linestyle='--', marker='D')
    plt.show()
        
        
        
# 0.Initial Screen

import PySimpleGUI as sg

layout = [[sg.Text('Please select your action')],
          [sg.Text('Click CRUD button, Report button or the Exit button')],
          [sg.Button('1.Create'),sg.Button('2.Retrive All'),sg.Button('3.Retrive')
           ,sg.Button('4.Update'),sg.Button('5.Delete All'),sg.Button('6.Delete')
           ,sg.Button('7.Report'), sg.Button('8.Exit')]]

window = sg.Window('Welcome to worldcup 2022 !', layout, enable_close_attempted_event=True)


while True:
    event, values = window.read()
    print(event, values)
    if event == '1.Create':
        print("1")
        create_func()
    elif event == '2.Retrive All':
        print("2")
        retriveall_func()
    elif event == '3.Retrive':
        print("3")
        retrive_func()
    elif event == '4.Update':
        print("4")
        update_func()
    elif event == '5.Delete All':
        print("5")
        deleteall_func()
    elif event == '6.Delete':
        print("6")
        delete_func()
    elif event == '7.Report':
        print("7")
        report_func()
    else:
        print("8")
        
        
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == '8.Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
        
window.close()

