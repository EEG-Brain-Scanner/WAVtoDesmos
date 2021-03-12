import parselmouth

sound = parselmouth.Sound("/Users/evanskrukwa/Desktop/trim.wav")
sound.pre_emphasize()

pitch = sound.to_pitch()
pitch_values = pitch.selected_array['frequency']



text_file = open("Output.txt", "w")

text_file.write("\left\{")

for x in range(len(pitch_values)):
    if x < len(pitch_values) - 1:
        text_file.write(str(x) + "\le x\le" + str(x+1) + ":" + str( str(pitch_values[x]).split(".")[0]) + ",")
    else:
        text_file.write(str(x) + "\le x\le" + str(x+1) + ":" + str( str(pitch_values[x]).split(".")[0]) + "\\right\}")

text_file.close()

print("x: ", len(pitch_values))
print("y: ", max(pitch_values))
