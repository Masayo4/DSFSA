import math

def get_index(dif_list):
    index_list =[]
    add_indexlist = list(enumerate(dif_list))
    get_index_list = sorted(enumerate(dif_list), key=lambda x: x[1])
    print(get_index_list)

    median_upper = math.ceil(len(get_index_list)/2)
    medien_lower = math.floor(len(get_index_list)/2)

    #print(get_index_list[-1][0]) #一番遠い人
    index_list.append(get_index_list[-1][0])
    #print(get_index_list[median_upper][0]) #中央上
    index_list.append(get_index_list[median_upper][0])
    #print(get_index_list[medien_lower][0]) #中央下
    index_list.append(get_index_list[medien_lower][0])
    #print(get_index_list[1][0]) #一番近い人
    index_list.append(get_index_list[1][0])
    #print(get_index_list[0][0]) #自分の表示
    index_list.append(get_index_list[0][0])
    #[遠い人、２番目遠い人、２番目近い人、一番近い人、自分]でリターンする
    return index_list


if __name__ == '__main__':
    difference = [1,2,3,0,4,0,0.01]
    video_list = ['２番目近い',
    '真ん中小',
    '真ん中大',
    '../data/output_video/ユーザー.mp4',
    '../data/output_video/ 遠い２番目.mp4',
    '../data/output_video/ 遠い.mp4',
    '../data/output_video/ 一番近い.mp4']
    index_list = get_index(difference)
    print(index_list)
    choice_video_list = []
    for i in index_list:
        choice_video_list.append(video_list[i])
    print(choice_video_list)
