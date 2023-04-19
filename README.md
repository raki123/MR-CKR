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
It reads in the input scene together with the basic ontology axioms from `with_scene.owl`.
Afterwards it produces the MR-CKR representing the different types of danger/diagnosis that should be present in the folder `MR_CKR`.
Additionally, it produces the file `MR_CKR/extra.lp` which contains 
    * weak constraints that ensure the generation of scenes that are as similar as possible to the input, and
    * strong constraints that ensure that in each context the corresponding danger/diagnosis is derived.

Next, to build the ASP representation of the MR-CKR run
```
cd ckr-datalog-rewriter-d-1.6/
bash mybuild.sh
cd ..
```
This produces an ASP file called `out.lp` containing the desired ASP representation.

To combine the MR-CKR represented by `out.lp` with the danger enforcing constraints and the similarity enforcing weak constraints use
```
clingo -t 4 MR_CKR/extra.lp ckr-datalog-rewriter-d-1.6/out.lp
```
This outputs the modifications necessary in each context to ensure the corresponding danger/diagnosis.

## Used modules
The module in `context.py` provides a python interface to build contexts from ground up and add (defeasible) axioms to them.
The module in `mr_ckr.py` provides a python interface to build an MR-CKR from a base ontology and different contexts that can be related in terms of specicifity. 
Additionally, it allows writing the produces MR-CKR into a folder in a format that the ckrewriter understands.
The script `build.py` build the corresponding model as explained above for our prototype to generate scenes for the autonomous driving application.
Notably, it contains a function `change_and_basic_from_ontology(onto, exchangeable_concepts)` that builds the `change` and `basic` context from the base ontology `onto` and the names of the concepts which are exchangable in `exchangeable_concepts`.

