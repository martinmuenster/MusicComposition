import csv
import os

sampleTime = 100


def openFiles():
    index = 1;
    directory = os.getcwd() + "\data\\raw_generated"
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            csv = "data/raw_generated/" + file
            with open("data/raw_generated/" + file) as csvfile:
                CSVlist(csvfile, index)
        index = index + 1
    print(filename)


def CSVlist(csvfile, index):
    note_rows = [0]*8
    reader = csv.reader(csvfile)
    time = 0;
    prev_row = ['0'] * 128
    note_rows[0] = [0,0,' Header',1,7,120]
    note_rows[1] = [1, 0, ' Start_track']
    note_rows[2] = [1, 0, ' Title_t', '\"wirugbwr\"']
    note_rows[3] = [1, 0, ' Time_signature', 3, 2, 24, 8]
    note_rows[4] = [1, 0, ' Tempo', 375000]
    note_rows[5] = [1, 0, ' End_track']
    note_rows[6] = [2, 0, ' Start_track']
    note_rows[7] = [2, 0, ' Title_t', '"Piano"']

    for row in reader:


        row = row[0].split()

        pitch = 0
        for velocity in row:
            if velocity != prev_row[pitch]:
                note_row = [0] * 6
                note_row[0] = 2
                note_row[2] = ' Note_on_c'
                note_row[3] = 0
                note_row[1] = time
                note_row[4] = pitch
                if velocity == '1':
                    note_row[5] = 80
                else:
                    note_row[5] = 0
                note_rows.append(note_row)
            pitch += 1
        time += 30
        prev_row = row
    note_rows.append([2, time, ' End_track'])
    note_rows.append([0, 0, ' End_of_file'])

        # aIndex = 0
        # bIndex = 0
        # for a in row:
        #     for b in prev_row:
        #         if aIndex == bIndex and a != b:
        #             note_row[1] = time
        #             note_row[4] = pitch
        #             note_row[5] = a
        #         bIndex += 1
        #     aIndex += 1
        #     pitch += 1
        # time += 30
        # prev_row = row
        # note_rows.append(note_row)

    with open('new' + str(index) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for n in note_rows:
            writer.writerow(n);

    #print(notesOn);


if (__name__ == "__main__"):
    openFiles()
