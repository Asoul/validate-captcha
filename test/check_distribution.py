import os

FOLDER = 'img1-segment'
file_names = os.listdir(FOLDER)
index_dict = {str(i).zfill(4): 0 for i in range(10000)}
pic_index_dict = {str(i): 0 for i in range(10)}
for file_name in file_names:
    index, pic_index = file_name[:-4].split('-')
    index_dict[index] += 1
    pic_index_dict[pic_index] += 1

dist = {i: 0 for i in range(10)}
for i in range(10000):
    fill_i = str(i).zfill(4)
    dist[index_dict[fill_i]] += 1

for i in range(10):
    print 'Contain', i, 'letters: ', dist[i]

for i in range(10):
    print i, '-th char', pic_index_dict[str(i)]
