# Cloud Security & DevSecOps Engineering — lesson m03l03 — Static Application Security Testing with Semgrep
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m03l03
# © LearnSome.tech
import ast, sys

def how_built(n, assigned):
    n = assigned.get(getattr(n, "id", None), n)      # a variable? follow it
    if isinstance(n, ast.JoinedStr):
        return "an f-string"
    if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Mod, ast.Add)):
        return "concatenation" if isinstance(n.op, ast.Add) else "% formatting"
    if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "format":
        return ".format()"

for fn in ast.walk(ast.parse(open(sys.argv[1]).read())):
    if isinstance(fn, ast.FunctionDef):
        assigned = {t.id: a.value for a in ast.walk(fn)
                    if isinstance(a, ast.Assign) for t in a.targets
                    if isinstance(t, ast.Name)}
        for call in ast.walk(fn):
            if isinstance(call, ast.Call) and call.args and \
                    getattr(call.func, "attr", "") == "execute":
                if how := how_built(call.args[0], assigned):
                    print(f"{sys.argv[1]}:{call.lineno}  SQL built by {how}")
