/usr/bin/time -f "Building %U" python build.py $1 $2 > /dev/null
cd ckr-datalog-rewriter-d-1.6/
/usr/bin/time -f "Translating %U" bash mybuild.sh > /dev/null
cd ..
(/usr/bin/time -f "Solving %U" clingo -t 3 MR_CKR/extra.lp ckr-datalog-rewriter-d-1.6/out.lp > /dev/null) 2>&1 | grep "Solving"