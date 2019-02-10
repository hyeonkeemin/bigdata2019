candidate_list = open('./연습생.txt', 'r', encoding='UTF-8')

def show_candidates(candidate_list):
    candidate_name = candidate_list.readlines()
    for candidate_name_list in candidate_name:
        print(candidate_name_list, end='')

def make_idol(candidate_list):
    candidate_name = candidate_list.readlines()
    for candidate_name_list in candidate_name:
        print('신예 아이돌 %s 인기 급상승'%candidate_name_list.strip('\n'))

def make_world_star(candidate_list):
    candidate_name = candidate_list.readlines()
    for candidate_name_list in candidate_name:
        print('아이돌 %s 월드스타 등극'%candidate_name_list.strip('\n'))

