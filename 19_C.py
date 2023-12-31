import re

get_line_as_tuple = lambda regex_match: (regex_match.group(1))
match_line = lambda line: re.match(r'(\w+){', line)

input = [part for part in open("input.txt", "r").read().split('\n\n')]

workflows = {}

cat_to_ind = lambda cat: 'xmas'.index(cat)

for line in input[0].splitlines():
    name = re.match(r'(\w+){', line).group(1)
    interior = re.search(r'\{(.+?)}', line)
    rules = re.split(r',', interior.group(1))
    workflow_to_add = []
    for rule in rules:
        if '<' in rule or '>' in rule:
            parsed_rule = re.match(r'([xmas])([<>])(\d+):(\w+)', rule)
            category, gt_lt, number, dest = parsed_rule.groups()
            workflow_to_add.append((category, gt_lt, int(number), dest))
        else:
            # append terminals
            workflow_to_add.append(rule)
    workflows[name] = workflow_to_add

queues = {'A': [],
          'R': [],
          'in': []}

for key in workflows.keys():
    queues[key] = []

for part in input[1].splitlines():
    queues['in'].append([int(match.group(2)) for match in re.finditer(r'(\w)=(\d+)', part)])

part_len = len(queues['in'])

print(workflows)


def process_queue(q):
    workflow = workflows[q[0]]
    for item in q[1]:
        try:
            queues[q[0]].remove(item)
        except Exception:
            pass
        for rule in workflow:
            if '<' not in rule and '>' not in rule:
                queues[rule].append(item)
            else:
               category, gt_lt, number, dest = rule
               start, end = item[category]
               if gt_lt == '<':
                       new_item = {**item}
                       new_item[category] = (start, number - 1)
                       if new_item[category][0] <= new_item[category][1]:
                           queues[dest].append(new_item)
                       item[category] = (number, end)
               else:
                       new_item = {**item}
                       new_item[category] = (number + 1, end)
                       if new_item[category][0] <= new_item[category][1]:
                           queues[dest].append(new_item)
                       item[category] = (start, number)
               if item[category][1] <= item[category][0]:
                   break

def check_empty_values(my_dict):
    for key, value in my_dict.items():
        if key not in ['A', 'R'] and value != []:
            return False
    return True

queues['in'] = [{key: (1, 4000) for key in "xmas"}]

while not check_empty_values(queues):
    for q in queues.items():
        if q[0] not in ['A', 'R']:
            process_queue(q)

print(queues['A'])
sum_ans = 0
for tool in queues['A']:
    answer = 1
    for key in 'xmas':
        answer *= (tool[key][1] - tool[key][0] + 1)
    sum_ans += answer


print(sum_ans)


