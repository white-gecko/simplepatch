# Simple Patch

This is some simple (and possibly ugly) patch script.

The requirements for the files are, that the content is sorted. Maybe you have to use `sort` before. The patch file also has to be sorted according to the addion and deletion lines, but not all `+` and `-` grouped.

To apply such a patch call it with (where `outfile.txt` is generated)

    ./simplepatch.py -m patch -i infile.txt -p patchfile.txt -o outfile.txt

To generate a patch/diff call it with (where `patchfile.txt` is generated)

    ./simplepatch.py -m diff -i infile.txt -o outfile.txt -p patchfile.txt

See also: https://stackoverflow.com/questions/31395250/simple-diff-patch-script-for-sorted-unique-file

License: GPLv3 or newer, if you want
