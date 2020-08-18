from pyomo.environ import * 
from pyomo.opt import SolverFactory, OptSolver

model = AbstractModel()
model.nVars = Param(initialize=4)
model.N = RangeSet(model.nVars)
model.x = Var(model.N, within=Binary)
def objectivo(model):
    return (summation(model.x))
model.obj = Objective(rule=objectivo,sense=minimize)
model.cuts = ConstraintList()
 #instanciando el modelo
mdl=model.create_instance()
SolverFactory('glpk').solve(mdl)

#ENSAYO  2 para diferenciar
for i in range(5):
    expr = 0
    for j in mdl.x:
        if value(mdl.x[j]) < 0.5:
            expr += mdl.x[j]
        else:
            expr += (1 - mdl.x[j])
    mdl.cuts.add( expr >= 1 )
    results = SolverFactory('glpk').solve(mdl)
    print ("\n===== iteration",i)
    mdl.x.pprint()

    print ("funcion objetiv0",value(mdl.obj))

