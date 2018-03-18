import csv
import os

def openFiles():
    directory = os.getcwd() + "\data\csv"
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            csv = "data/csv/" + file
            with open("data/csv/" + file) as csvfile:
                CSVlist(csvfile)


def CSVlist(csvfile):
    notes_on_c = []
    tracks = {}

    # directory = os.getcwd() + "\data\csv"
    # for file in os.listdir(directory):
    #     print(file)
    # #     filename = os.fsdecode(file)
    # #     if filename.endswith(".asm") or filename.endswith(".py"):
    # #         # print(os.path.join(directory, filename))
    # #         continue
    # #     else:
    # with open("data/csv/AfterYou.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[2] == ' Note_on_c':
            notes_on_c.append(row)


    maxNotes = 0
    for note in notes_on_c:
        track = note[0]
        channel = note[3]
        if track not in tracks.keys():
            tracks[track] = {}
        if channel not in tracks[track].keys():
            tracks[track][channel] = []
        if len(tracks[track][channel])+1 > maxNotes:
            maxNotes = len(tracks[track][channel])
            maxChannel = channel
            maxTracks = track

        del note[3]
        del note[2]
        del note[0]
        tracks[track][channel].append(note)
    notes = tracks[maxTracks][maxChannel]
    print(notes)
    print("\n\n")






if( __name__ == "__main__" ):
    openFiles()