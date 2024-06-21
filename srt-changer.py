#!/usr/bin/env python

import sys
import datetime
import re

def tc_to_datetime(t):
    """takes a string subtitle time code hh:mm:ss,zeropadded millisecond
    converts to datetime
    """
    e=re.split("[,:]",t)
    e=[int(ee) for ee in e]
    e=[2000,1,1]+e
    e[-1]=e[-1]*1000
    return datetime.datetime(*e)

def change(t, sec, mil, mult=None, multoffset=None):
    """
    removes the sec seconds and mil millisecond
    and returns similar
    """
    tt = tc_to_datetime(t).timestamp()
    if mult:
        tt = tt - multoffset
        tt = tt*mult + multoffset
    
    tt = datetime.datetime.fromtimestamp(tt)
    ntt=tt-datetime.timedelta(seconds=sec, microseconds=mil*1000)
    return datetime_to_tc(ntt)
    
def datetime_to_tc(ntt):
    return ntt.strftime("%H:%M:%S") + "," + str(int(ntt.microsecond/1000)).zfill(3)

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("offset", type=float)
    parser.add_argument("-m", "--multiplier", type=float)
    parser.add_argument("-n", "--noaction", action="store_true")
    args = parser.parse_args()
    #print(args, file=sys.stderr)

    print(f"file: {args.file}", file=sys.stderr)
    print(f"offset (negative): {args.offset}", file=sys.stderr)

    with open(args.file,"r") as f:
        data = f.read()

    print(f"read {len(data)}", file=sys.stderr)
    res=re.findall("\d\d:\d\d:\d\d,\d\d\d",data)
    print(f"timescodes: {len(res)}", file=sys.stderr)

    multoffset = 0
    secc = int(args.offset)
    mill = 1000*(args.offset-secc)

    if args.multiplier:
        first_code = res[0]
        last_code = res[-1]
        multoffset = tc_to_datetime(first_code).timestamp()
        newlast = change(last_code, secc, mill, args.multiplier, multoffset)

        newfirst = change(first_code, secc, mill, args.multiplier, multoffset)
        print(f"first code {first_code}", file=sys.stderr)
        print(f"last code {last_code}", file=sys.stderr)
        print(f"new first code {newfirst}", file=sys.stderr)
        print(f"new last code {newlast}", file=sys.stderr)
    
    print(f"multiplier offset {multoffset}", file=sys.stderr)
    
    if args.noaction:
        print("doing nothing", file=sys.stderr)
        sys.exit(0)

    for t in res:
        data = data.replace(t,
                change(t,secc,mill,args.multiplier,multoffset)
        )

    print(data)


