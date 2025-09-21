import boolean;

# SATISFIABILITY TESTS
def test_sat1():
    cnf = "p /\\ (p -> q) /\\ (p -> ~r) /\\ (r \\/ ~s) /\\ (s \\/ ~q)";
    result = boolean.is_satisfiable(cnf);
    assert (not result);

def test_sat2():
    cnf = "p /\\ (p -> q) /\\ (q -> r) /\\ ~r";
    result = boolean.is_satisfiable(cnf);
    assert (not result);
    
def test_sat3():
    cnf = "(~p \\/ q) /\\ (~p \\/ r) /\\ (~q \\/ r) /\\ (p \\/ ~q) /\\ (~p \\/ ~q) /\\ (~p \\/ ~r)";
    result = boolean.is_satisfiable(cnf);
    assert(result);
    
def test_sat4():
    cnf = "(p -> q) /\\ (q -> ~r) /\\ (r -> p)";
    result = boolean.is_satisfiable(cnf);
    assert(result);

def test_sat5():
    cnf = "(p \\/ t) /\\ (p -> q) /\\ (q -> r) /\\ (~r \\/ s) /\\ (~t \\/ z) /\\ ~z /\\ ~s";
    result = boolean.is_satisfiable(cnf);
    assert(not result);
