candidate_list = open('./연습생.txt', 'r', encoding='UTF-8')
candidate_name = candidate_list.readlines()

def show_candidates(candidate_list):
    for candidate_name_list in candidate_name:
        print(candidate_name_list.strip('\n'))

def make_idol(candidate_list):
    for candidate_name_list in candidate_name:
        print('신예 아이돌 %s 인기 급상승'%candidate_name_list.strip('\n'))

def make_world_star(candidate_list):
    for candidate_name_list in candidate_name:
        print('아이돌 %s 월드스타 등극'%candidate_name_list.strip('\n'))

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)

candidate_list.close()