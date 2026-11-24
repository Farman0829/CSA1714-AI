% Knowledge Base Facts

human(socrates).
human(plato).
human(aristotle).

parent(john, mary).
parent(mary, sam).
parent(john, peter).
parent(peter, david).

student(alex).
student(brain).

teacher(mr_smith).

% Inference Rules

mortal(X) :-
    human(X).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

eligible(X) :-
    student(X).

can_teach(X) :-
    teacher(X).

% Inference Engine

infer(Query) :-
    call(Query),
    write('Conclusion: '),
    write(Query),
    nl.