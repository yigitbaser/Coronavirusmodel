import model

m = model.SIR(eons=4000, Susceptible = 3200, Infected= 200, rateIR= 0.003, rateSI= 0.1)
m.run()
m.plot()