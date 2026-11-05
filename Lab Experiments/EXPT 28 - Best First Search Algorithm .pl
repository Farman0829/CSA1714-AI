% Best First Search Algorithm

edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(b, e, 1).
edge(c, f, 3).
edge(c, g, 6).
edge(d, h, 2).
edge(e, h, 4).
edge(f, h, 2).
edge(g, h, 1).

heuristic(a, 7).
heuristic(b, 5).
heuristic(c, 4).
heuristic(d, 3).
heuristic(e, 2).
heuristic(f, 2).
heuristic(g, 1).
heuristic(h, 0).

bestfirst(Start, Goal, Path) :-
    search([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

search([[Goal|Path]|_], Goal, [Goal|Path]).

search([[Node|Path]|Rest], Goal, FinalPath) :-
    findall([Next,Node|Path],
        (edge(Node, Next, _),
         \+ member(Next, [Node|Path])),
        Children),
    append(Rest, Children, NewPaths),
    sort_paths(NewPaths, SortedPaths),
    search(SortedPaths, Goal, FinalPath).

sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_heuristic([Node|_], H) :-
    heuristic(Node, H).