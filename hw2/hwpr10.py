#!/usr/bin/env python

def partb():
    #import pudb
    #pudb.set_trace()
    pts = []
    x = 0.0
    while x < 1.0:
        y = 0.0
        while y < 1.0:
            if x + y > .5 and x + y < 1.5:
                pts.append("{0},{1}".format(x,y))
            y += .01
        x += .01
    f = open("results.csv","w")
    i = 0
    while True:
        if len(pts) <= i:
            break
        f.write(pts[i] + '\n')
        i += 1
    f.close()

if __name__=="__main__":
    partb()
