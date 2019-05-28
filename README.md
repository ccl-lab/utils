# Slice Video Script

## Usage
Place in the same folder as the video files. Video files should only contain date and kid ID, and reads from compiledValues.csv, with filename, verb, and onset information. Creates new videos, 5 seconds long, with the naming format of "(verb)_(kidID)_(utteranceCount)_(length).mov".

Requires FFmpeg


# CSV Joiner Script

Place in same folder as cleaned csv files, finds files that have "verbonset_cleaned" in the name and copies the data into a new array, which is then written to the file compiledValues.csv.
