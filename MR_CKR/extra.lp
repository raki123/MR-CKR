instd(X,"DELCar",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELCar",Context,"main").
instd(X,"DONTDELCar",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELCar",Context,"main").
instd(X,"ADDCar",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDCar",Context,"main").
instd(X,"DONTADDCar",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDCar",Context,"main").
instd(X,"DELChild",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELChild",Context,"main").
instd(X,"DONTDELChild",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELChild",Context,"main").
instd(X,"ADDChild",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDChild",Context,"main").
instd(X,"DONTADDChild",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDChild",Context,"main").
instd(X,"DELGlidingOnWheels",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELGlidingOnWheels",Context,"main").
instd(X,"DONTDELGlidingOnWheels",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELGlidingOnWheels",Context,"main").
instd(X,"ADDGlidingOnWheels",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDGlidingOnWheels",Context,"main").
instd(X,"DONTADDGlidingOnWheels",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDGlidingOnWheels",Context,"main").
instd(X,"DELHuman",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELHuman",Context,"main").
instd(X,"DONTDELHuman",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELHuman",Context,"main").
instd(X,"ADDHuman",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDHuman",Context,"main").
instd(X,"DONTADDHuman",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDHuman",Context,"main").
instd(X,"DELRollingContainer",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELRollingContainer",Context,"main").
instd(X,"DONTDELRollingContainer",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELRollingContainer",Context,"main").
instd(X,"ADDRollingContainer",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDRollingContainer",Context,"main").
instd(X,"DONTADDRollingContainer",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDRollingContainer",Context,"main").
instd(X,"DELSign",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELSign",Context,"main").
instd(X,"DONTDELSign",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELSign",Context,"main").
instd(X,"ADDSign",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDSign",Context,"main").
instd(X,"DONTADDSign",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDSign",Context,"main").
instd(X,"DELSmoke",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELSmoke",Context,"main").
instd(X,"DONTDELSmoke",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELSmoke",Context,"main").
instd(X,"ADDSmoke",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDSmoke",Context,"main").
instd(X,"DONTADDSmoke",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDSmoke",Context,"main").
instd(X,"DELStopLineMarking",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTDELStopLineMarking",Context,"main").
instd(X,"DONTDELStopLineMarking",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DELStopLineMarking",Context,"main").
instd(X,"ADDStopLineMarking",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"DONTADDStopLineMarking",Context,"main").
instd(X,"DONTADDStopLineMarking",Context,"main") :- instd(X,"Named",Context,"main"), not instd(X,"ADDStopLineMarking",Context,"main").
:~ instd(X,"DELCar",Context,"main"). [1,X,"DELCar",Context]
:~ instd(X,"ADDCar",Context,"main"). [1,X,"ADDCar",Context]
:~ instd(X,"DELChild",Context,"main"). [1,X,"DELChild",Context]
:~ instd(X,"ADDChild",Context,"main"). [1,X,"ADDChild",Context]
:~ instd(X,"DELGlidingOnWheels",Context,"main"). [1,X,"DELGlidingOnWheels",Context]
:~ instd(X,"ADDGlidingOnWheels",Context,"main"). [1,X,"ADDGlidingOnWheels",Context]
:~ instd(X,"DELHuman",Context,"main"). [1,X,"DELHuman",Context]
:~ instd(X,"ADDHuman",Context,"main"). [1,X,"ADDHuman",Context]
:~ instd(X,"DELRollingContainer",Context,"main"). [1,X,"DELRollingContainer",Context]
:~ instd(X,"ADDRollingContainer",Context,"main"). [1,X,"ADDRollingContainer",Context]
:~ instd(X,"DELSign",Context,"main"). [1,X,"DELSign",Context]
:~ instd(X,"ADDSign",Context,"main"). [1,X,"ADDSign",Context]
:~ instd(X,"DELSmoke",Context,"main"). [1,X,"DELSmoke",Context]
:~ instd(X,"ADDSmoke",Context,"main"). [1,X,"ADDSmoke",Context]
:~ instd(X,"DELStopLineMarking",Context,"main"). [1,X,"DELStopLineMarking",Context]
:~ instd(X,"ADDStopLineMarking",Context,"main"). [1,X,"ADDStopLineMarking",Context]
#show.
#show added(X, "Car", Context) : instd(X, "ADDCar", Context, "main").
#show deleted(X, "Car", Context) : instd(X, "DELCar", Context, "main").
#show added(X, "Child", Context) : instd(X, "ADDChild", Context, "main").
#show deleted(X, "Child", Context) : instd(X, "DELChild", Context, "main").
#show added(X, "GlidingOnWheels", Context) : instd(X, "ADDGlidingOnWheels", Context, "main").
#show deleted(X, "GlidingOnWheels", Context) : instd(X, "DELGlidingOnWheels", Context, "main").
#show added(X, "Human", Context) : instd(X, "ADDHuman", Context, "main").
#show deleted(X, "Human", Context) : instd(X, "DELHuman", Context, "main").
#show added(X, "RollingContainer", Context) : instd(X, "ADDRollingContainer", Context, "main").
#show deleted(X, "RollingContainer", Context) : instd(X, "DELRollingContainer", Context, "main").
#show added(X, "Sign", Context) : instd(X, "ADDSign", Context, "main").
#show deleted(X, "Sign", Context) : instd(X, "DELSign", Context, "main").
#show added(X, "Smoke", Context) : instd(X, "ADDSmoke", Context, "main").
#show deleted(X, "Smoke", Context) : instd(X, "DELSmoke", Context, "main").
#show added(X, "StopLineMarking", Context) : instd(X, "ADDStopLineMarking", Context, "main").
#show deleted(X, "StopLineMarking", Context) : instd(X, "DELStopLineMarking", Context, "main").
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
:- not found_sign_and_stop_line_1.
found_sign_and_stop_line_2 :- instd(X, "StopLineMarking", "sign_and_stop_line_diagnosis", "main").
:- not found_sign_and_stop_line_2.
