#!/bin/bash

#  aaabca+cbaa -> aabc(aa+1) -> a2bc(a2+1)
# bbbaaaccc+bbbbbbccccaaa -> cccaaabbb(1 + b3c)
echo '################TEST 1################'
python B.py <<EOF
2
equa+
abc+def
anna+an
aaabca+
seventeen+sixteen
EOF

echo '################TEST 1################'
python B.py <<EOF
5
six+seven
sin+cos
race+care
crop+pork
battle+battler
EOF

echo '################TEST 1################'
python B.py <<EOF
5
sixteen+seventeen
sin+cos
race+care
crop+pork
battle+battler
EOF

