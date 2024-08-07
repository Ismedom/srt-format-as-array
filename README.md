# srt-format-as-array

This Python script reads a SubRip Subtitle (SRT) file, parses its content, and converts the subtitles into a list of dictionaries. Each dictionary represents a subtitle entry with `index`, `time_start`, `time_end`, and `text` properties. The `time_start` and `time_end` properties are converted from the `HH:MM:SS,mmm` format to seconds.
1
00:00:01,000 --> 00:00:04,000
This is the first subtitle.

2
00:00:05,000 --> 00:00:08,000
This is the second subtitle.

3
00:00:09,000 --> 00:00:12,000
This is the third subtitle.
