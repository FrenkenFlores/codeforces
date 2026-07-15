#!/bin/bash
# W,H,x,y,w,h
# T
# 1≤|T|≤50
# w≥|T|+3
# h≥3
# x,y≥2
# W≥x+w
# H≥y+h
# W,H≤50

echo '################TEST 1################'
python A.py <<EOF
20 10 3 3 16 4
Helloworld
EOF
echo '################TEST 2################'
python A.py <<EOF
6 5 2 2 4 3
A
EOF
echo '################TEST 3################'
# W,H,x,y,w,h
python A.py <<EOF
60 30 10 3 16 4
A
EOF