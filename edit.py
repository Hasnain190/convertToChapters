import re
file = open('Chapters.txt', 'r')
with open('added.csv','w') as added:
    chapter_no = 0
    for i in file:
        time_lapse = re.findall(r'\d+:\d+:\d+', i)[0]
        name = i.replace(time_lapse, '')
        brakets = re.findall(r'\(.*?\)', name)
        if brakets:
            for j in brakets:
                name = name.replace(j, '')
        name = name.replace('\n', '')
       

        chapter_no += 1
        added.write('CHAPTER'+str(chapter_no)+','+time_lapse + '\n')
        added.write('CHAPTER'+str(chapter_no)+'NAME'+','+name + '\n')


