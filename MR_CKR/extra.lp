:~ instd(X,"DELChild",Context,"main"). [1,X,"DELChild",Context]
:~ instd(X,"ADDChild",Context,"main"). [1,X,"ADDChild",Context]
:~ instd(X,"DELConstructionSign",Context,"main"). [1,X,"DELConstructionSign",Context]
:~ instd(X,"ADDConstructionSign",Context,"main"). [1,X,"ADDConstructionSign",Context]
:~ instd(X,"DELGlidingOnWheels",Context,"main"). [1,X,"DELGlidingOnWheels",Context]
:~ instd(X,"ADDGlidingOnWheels",Context,"main"). [1,X,"ADDGlidingOnWheels",Context]
:~ instd(X,"DELRoadSign",Context,"main"). [1,X,"DELRoadSign",Context]
:~ instd(X,"ADDRoadSign",Context,"main"). [1,X,"ADDRoadSign",Context]
:~ instd(X,"DELRollingContainer",Context,"main"). [1,X,"DELRollingContainer",Context]
:~ instd(X,"ADDRollingContainer",Context,"main"). [1,X,"ADDRollingContainer",Context]
:~ instd(X,"DELSign",Context,"main"). [1,X,"DELSign",Context]
:~ instd(X,"ADDSign",Context,"main"). [1,X,"ADDSign",Context]
:~ instd(X,"DELSmoke",Context,"main"). [1,X,"DELSmoke",Context]
:~ instd(X,"ADDSmoke",Context,"main"). [1,X,"ADDSmoke",Context]
:~ instd(X,"DELStopLineMarking",Context,"main"). [1,X,"DELStopLineMarking",Context]
:~ instd(X,"ADDStopLineMarking",Context,"main"). [1,X,"ADDStopLineMarking",Context]
:~ instd(X,"DELVehicleNotSignaling",Context,"main"). [1,X,"DELVehicleNotSignaling",Context]
:~ instd(X,"ADDVehicleNotSignaling",Context,"main"). [1,X,"ADDVehicleNotSignaling",Context]
:~ instd(X,"DELVehicleSignaling",Context,"main"). [1,X,"DELVehicleSignaling",Context]
:~ instd(X,"ADDVehicleSignaling",Context,"main"). [1,X,"ADDVehicleSignaling",Context]
found_gliding :- instd(X, "GlidingOnWheels", "gliding_diagnosis", "main").
:- not found_gliding.
found_children :- instd(X, "Child", "children_diagnosis", "main").
:- not found_children.
found_rolling_no_human_1 :- instd(X, "RollingContainer", "rolling_no_human_diagnosis", "main").
:- not found_rolling_no_human_1.
found_rolling_no_human_2 :- instd(X, "Human", "rolling_no_human_diagnosis", "main").
:- found_rolling_no_human_2.
found_sign_and_smoke_1 :- instd(X, "Sign", "sign_and_smoke_diagnosis", "main").
:- not found_sign_and_smoke_1.
found_sign_and_smoke_2 :- instd(Y, "Smoke", "sign_and_smoke_diagnosis", "main").
:- not found_sign_and_smoke_2.
found_sign_and_stop_line_1 :- instd(X, "Sign", "sign_and_stop_line_diagnosis", "main").
:- not found_sign_and_stop_line_2.
found_sign_and_stop_line_2 :- instd(X, "StopLineMarking", "sign_and_stop_line_diagnosis", "main").
:- not found_sign_and_stop_line_2.
