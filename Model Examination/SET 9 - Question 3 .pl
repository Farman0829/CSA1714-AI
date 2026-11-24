% Family Facts

father(john, paul).
father(john, lisa).
father(george, paul).
father(george, mike).
father(paul, tom).
father(mike, jack).

mother(susan, paul).
mother(susan, lisa).
mother(helen, paul).
mother(helen, mike).
mother(anna, tom).
mother(rita, jack).

male(john).
male(george).
male(paul).
male(mike).
male(tom).
male(jack).

female(susan).
female(helen).
female(lisa).
female(anna).
female(rita).

% Parent Rules

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Sibling Rules

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

% Uncle and Aunt Rules

uncle(X, Y) :-
    brother(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    sister(X, Z),
    parent(Z, Y).

% Cousin Rule

cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).