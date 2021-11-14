
"""Import important libraries"""
import pandas as pd
import json
import numpy
"""File load & """
files = ['result1.json',"result2.json","result3.json","result4.json"]
my_dict = []
for filenumber in files:
    with open(filenumber, encoding='utf-8') as json_file:
        data  =  json.load(json_file)

        for i in range (0, 80000):


            """All id need to append in id_list"""
            try:
                id = data['messages'][i]['id']
                # id =id

            except:
                id = None
                pass


            '''all type append in type_list'''
            try:
                type = data['messages'][i]['type']
                # type = type
            except :
                type = None
                pass


            """All dates of messageing"""
            try:
                date = data['messages'][i]['date']
                # date = date
            except:
                date = None
                pass


            '''all type append in actor_list'''
            try:
                actor = data['messages'][i]['actor']
                # actor = actor
            except:
                actor = (None)
                pass


            """All Actor ID"""

            try:
                actor_id = data['messages'][i]['actor_id']
            except:
                actor_id = None
                pass


            """All actions taken"""

            try:
                actions = data['messages'][i]['action']
            except:
                actions = None
                pass


            """All titles inside chat"""
            try:
                titles = data['messages'][i]['title']
            except:
                titles = None
                pass


            """actions mentions text"""
            try:
                text = data['messages'][i]['text']
            except:
                text = None
                pass


            """Finding Sender details"""
            try:
                sender = data['messages'][i]['from']
            except:
                sender = None
                pass


            """Findind Sender_ID"""
            try:
                sender_id = data['messages'][i]['from_id']
            except:
                sender_id = None
                pass


            """Links inside text"""
            try:
                links = data['messages'][i]['text'][0]['type']
            except:
                links = None
                pass


            """link_details"""
            try:
                links_details = data['messages'][i]['text'][0]['text']
            except:
                links_details = None
                pass


            """Replying to communication"""
            try:
                reply_to_sender  = data['messages'][i]['reply_to_message_id']
            except:
                reply_to_sender = None
                pass


            """edited messages"""
            try:
                edited_time = data['messages'][i]['edited']
            except:
                edited_time =  None
                pass

            """taged messages"""

            try:
                tag_to = data['messages'][i]['text'][0]["text"]
                taged_to_id = data['messages'][i]["text"][0]['user_id']
            except:
                tag_to = None
                taged_to_id = None
                pass

            """invited Members"""

            try:
                members_join_remove = data['messages'][i]['text'][0]["text"]

            except:
                members_join_remove = None

                pass

            details = {'id': id, "type":type, 'date':date, 'actor':actor,
                       'actor_id': actor_id, "action_taken": actions,  'title':titles,
                      'sender':sender, "sender_id":sender_id,  "messages": text, "links":links, "links_details":links_details,
                       "reply_to_sender": reply_to_sender, "edited_time":edited_time,'members_join_remove':members_join_remove,'taged_to': tag_to
                       , "tagged_id":taged_to_id,}
            my_dict.append(details)
            # print(text)

        a = pd.DataFrame(my_dict)
        a.to_csv('myfile.csv')

        print(len(my_dict))







