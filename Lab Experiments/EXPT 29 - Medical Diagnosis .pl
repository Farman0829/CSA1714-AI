
% Medical Diagnosis System

symptom(fever).
symptom(cough).
symptom(headache).
symptom(sneezing).
symptom(body_pain).

diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

diagnosis(common_cold) :-
    symptom(sneezing),
    symptom(cough).

diagnosis(malaria) :-
    symptom(fever),
    symptom(headache),
    symptom(body_pain).

diagnose :-
    diagnosis(Disease),
    write('Possible Disease: '),
    write(Disease),
    nl,
    fail.

diagnose.
