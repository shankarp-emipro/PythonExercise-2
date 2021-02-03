import json
emp_dict = {
            101: {'name':  'Anupriya Roy',
                  'depart_id': 1,
                  'attendances': [{'date': 1, 'hours': [3.5,4.5]},{'date': 2, 'hours': [3.2,4.5]},{'date': 3, 'hours': [3.2,4.6]},
                                  {'date': 4, 'hours': [3.0,4.5]},{'date': 5, 'hours': [2.5,4.5]},{'date': 6, 'hours': [1.5,4.5]},
                                  {'date': 7, 'hours': [2,3]},{'date': 8, 'hours': [0,4.5]},{'date': 9, 'hours': [2,3.5]},
                                  {'date': 10, 'hours': [4,3.5]}],
                  'leaves': [{'date': 7, 'no_of_hours': 1.5},{'date': 7, 'no_of_hours': 1.5},{'date': 8, 'no_of_hours': 3}]
                 },
            102:
                 {'name':  'Kadambari Sharma',
                  'depart_id': 1,
                  'attendances': [{'date': 1, 'hours':  [0,4.5]},{'date': 2, 'hours': [3.2,0]},{'date': 3, 'hours': [3.2,4.6]},
                                {'date': 4, 'hours': [1,4.5]},{'date': 5, 'hours': [2.5,2]},{'date': 6, 'hours': [1.5,1]},
                                {'date': 7, 'hours': [2,4]},{'date': 8, 'hours': [1,4.5]},{'date': 9, 'hours': [2,2]},
                                {'date': 10, 'hours': [2,3.5]}],
                  'leaves': [{'date': 1, 'no_of_hours': 3.5},{'date': 2, 'no_of_hours': 2},{'date': 2, 'no_of_hours': 2}]
             },
            103:
                 {'name':  'Abhishek Verma',
                  'depart_id': 1,
                  'attendances': [{'date': 3, 'hours': [3.2,4.6]},{'date': 4, 'hours': [1,4.5]},{'date': 5, 'hours': [2.5,2]},
                            {'date': 6, 'hours': [1.5,1]},{'date': 7, 'hours': [2,4]},{'date': 8, 'hours': [1,4.5]},
                            {'date': 9, 'hours': [2,2]},{'date': 10, 'hours': [2,3.5]}
                ],
                'leaves': [{'date': 1, 'no_of_hours': 3},{'date': 2, 'no_of_hours': 2},{'date': 2, 'no_of_hours': 3}]
            }
}

list1 = []
list2 = []
for emp_id, emp_data in emp_dict.items():
    list1.append({
        'employee_id': emp_id,
        'employee_name': emp_data.get('name'),
        'total_attendance_hours': sum(list(map(lambda each_dict: sum(each_dict.get('hours')), emp_data['attendances']))),
        'total_leave_hours': sum(list(map(lambda each_dict: each_dict.get('no_of_hours'), emp_data['leaves'])))
    })
    list2.append({
        emp_id: {
            'date': list(filter(lambda l1: l1, list(map(lambda l: l.get('date') if sum(l.get('hours')) < 7 else False, emp_data.get('attendances'))))),
            'total_hrs': list(filter(lambda l1: l1, list(map(lambda l: sum(l.get('hours')) if sum(l.get('hours')) < 7 else False, emp_data.get('attendances'))))),
            'remaining_hrs': list(filter(lambda l1: l1, list(map(lambda l: 8 - sum(l.get('hours')) if sum(l.get('hours')) < 7 else False, emp_data.get('attendances')))))
        }
    })

print(json.dumps(list1, indent=2))
print("--------------------------------")
print(json.dumps(list2, indent=2))
