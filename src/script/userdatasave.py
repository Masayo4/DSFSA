import csv

def user_data_save(user_dir,video_list,ranking_data):
    csvfilename = user_dir +"result.csv"
    with open(csvfilename,'w') as csv_file:
        fieldnames = ['Number','video_path', 'ranking_score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(5):
            writer.writerow({'Number': i+1, 'video_path': video_list[i],'ranking_score': ranking_data[i]})
        print("save csvdata.")
    return 0


if __name__ == '__main__':
    dir = "test/"
    video_list =['../data/output_video/smile_video20191117195306.mp4',
    '../data/output_video/smile_video20191117210526.mp4',
    '../data/output_video/smile_video20191118102738.mp4',
    '../data/output_video/smile_video20191118103109.mp4',
    '../data/output_video/smile_video20191118103339.mp4']
    ranking = [3,4,5,2,1]

    user_data_save(dir,video_list,ranking)
