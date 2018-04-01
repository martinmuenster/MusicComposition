import csv
import os

sampleTime = 100


def openFiles():
    index = 1;
    directory = os.getcwd() + "\data\csv"
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            csv = "data/csv/" + file
            with open("data/csv/" + file) as csvfile:
                CSVlist(csvfile, index)
        index = index + 1
    print(filename)


def CSVlist(csvfile, index):
    notes_on_c = []
    tracks = {}

    reader = csv.reader(csvfile)
    for row in reader:
        if row[2] == ' Note_on_c':
            notes_on_c.append(row)
        elif row[2] == ' Header':
            division = row[5]
        elif row[2] == ' Tempo':
            tempo = 1000 / int(row[3])
    maxNotes = 0
    for note in notes_on_c:
        track = note[0]
        channel = note[3]
        if track not in tracks.keys():
            tracks[track] = {}
        if channel not in tracks[track].keys():
            tracks[track][channel] = []
        if len(tracks[track][channel]) + 1 > maxNotes:
            maxNotes = len(tracks[track][channel])
            maxChannel = channel
            maxTracks = track

        del note[3]
        del note[2]
        del note[0]

        note[0] = int(note[0]) / int(division) / tempo
        tracks[track][channel].append(note)
    notes = tracks[maxTracks][maxChannel]
    notesOn = []

    time = sampleTime
    noteOn = [0] * 128
    myNote = list(noteOn)
    for note in notes:
        if int(note[0]) < time:
            myNote[int(note[1])] = int(note[2])
        else:
            notesOn.append(myNote)
            time += sampleTime
            myNote = list(myNote)
            myNote[int(note[1])] = int(note[2])

    for i in range(0, 50):
        notesOn.append([0] * 128)
    with open(str(index) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for n in notesOn:
            writer.writerow(n);

    #print(notesOn);


if (__name__ == "__main__"):
    openFiles()
