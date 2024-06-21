# srt-timechanger

Changes srt timestamps by offset and multiplier

# Install

navigate to bin directory of choice

```
wget https://raw.githubusercontent.com/RobinTPotter/srt-timechanger/v1/srt-changer.py
chmod +x srt-changer.py
```

# Usage

```
python srt-changer.py [-h] [-m MULTIPLIER] [-n] file offset
```

# Example

```
python srt-changer.py Blood_Simple.srt 21.5 -m 0.96 -n
```

```-m``` : if the multiplier arg is given an offset is calculated
based on the fist seen timestamp, this is removed prior
to scaling then re-added.

```-n``` : flag is "no action", prints blurb and exits

blurb appears in stderr and _results are written to stdout_


Example blurb:

```
Namespace(file='Blood_Simple.srt', multiplier=0.96, noac
tion=True, offset=21.5)
file: Blood_Simple.srt
offset (negative): 21.5
read 43485
timescodes: 1282
first code 00:00:31,584
last code 01:33:07,501
new first code 00:00:10,084
new last code 01:29:03,764
multiplier offset 946684831.584
doing nothing
```


