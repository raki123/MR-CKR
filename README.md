# Scene Modification with MR-CKR and ASP
To install the necessary requirements use
```
pip install -r requirements.txt
```
Additionally, the ckrewriter needs Java to run. See https://github.com/dkmfbk/ckrew.

To build the inputs for the ckrewriter run
```
python build.py
```
To build the ASP representation of the MR-CKR run
```
cd ckr-datalog-rewriter-d-1.6/
bash mybuild.sh
cd ..
```
This produces an ASP file called `out.lp`. 
To combine the MR-CKR represented by `out.lp` with the danger enforcing constraints and the similarity enforcing weak constraints use
```
clingo MR_CKR/extra.lp ckr-datalog-rewriter-d-1.6/out.lp
```
