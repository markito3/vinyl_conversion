#!/usr/bin/python

import glob
import os

artist = "Carole King"
album = "Tapestry"
file = open("tracks.txt", 'r')
tracknumber = 0
while True:
    title = file.readline()
    if not title:
        break
    tracknumber += 1
    tags = open("tags.tmp", "w")
    tags.write("ARTIST=" + artist + "\n")
    tags.write("ALBUM=" + album + "\n")
    tags.write("TRACKNUMBER=" + str(tracknumber) + "\n")
    tags.write("TITLE=" + title.strip() + "\n")
    tags.close()
    tracknumber_str = str(tracknumber).rjust(2, '0')
    oggfiles = glob.glob(tracknumber_str + "-Sound *.ogg")
    oggfile_in = oggfiles[0].replace(" ", "\ ")
    #print(oggfiles)
    title_escaped = title
    print(title_escaped)
    title_escaped = title.replace(" ", "_")
    print(title_escaped)
    title_escaped = title_escaped.replace("'", "_")
    print(title_escaped)
    title_escaped = title_escaped.replace("&", "and")
    title_escaped = title_escaped.replace("(", "\(")
    title_escaped = title_escaped.replace(")", "\)")
    oggfile_out = tracknumber_str + "-" + title_escaped
    vc_command = "vorbiscomment -w -c tags.tmp " + oggfile_in + " " + oggfile_out.strip() + ".ogg"
    print(vc_command)
    os.system(vc_command)

file.close()
