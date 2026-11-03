% Family Tree Program

% Facts
male(john).
male(robert).
male(james).
female(mary).
female(lisa).
female(anna).

% Parent relationships
parent(john, robert).
parent(mary, robert).
parent(john, lisa).
parent(mary, lisa).
parent(robert, james).
parent(lisa, anna).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

child(X, Y) :-
    parent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.