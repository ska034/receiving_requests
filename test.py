# my_dict = {
#     'kind':"1234",
#     'data':{
#         'after':'RUN',
#         'children':[{'autor':'Alex','book':'No name'},{'autor':'Dima','book':'no_name3'}]
#     }
# }
#
# for i in my_dict['data']['children']:
#     print(i['autor'])

# import json
# with open('res.json','r') as inputfile:
#     f = json.loads(eval(inputfile.read()))
#
# print(f["message"])


from date import Date

b = Date(1658016011).date_history()
print(b)