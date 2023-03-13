python build.py
cd ckr-datalog-rewriter-d-1.6/
bash mybuild.sh
cd ..
clingo -t 3 MR_CKR/extra.lp ckr-datalog-rewriter-d-1.6/out.lp
