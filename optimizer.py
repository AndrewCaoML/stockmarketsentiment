import numpy as np
from scipy.optimize import minimize
from csv import reader



# Load a CSV file
def load_csv(filename):
	dataset_int = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset_int.append(row)
	return dataset_int
    
# Load dataset
filename = 'FinalStockPredictions.csv'
dataset = load_csv(filename)


AllStockNames = []
AllStockPrices = []
AllStockReturns = []
AllStockBeta = []



i = 1
while(i<506):
    AllStockNames.append(dataset[i][370])
    AllStockPrices.append(float(dataset[i][3]))
    AllStockReturns.append(-float(dataset[i][371]))
    AllStockBeta.append(float(dataset[i][372]))
    
    i+=1


print(AllStockNames)
print(AllStockPrices)
print(AllStockReturns)
print(AllStockBeta)


i = 1
while(i<len(AllStockReturns)):
    if(AllStockReturns[i] > -0.35):    
        AllStockNames.pop(i)
        AllStockPrices.pop(i)
        AllStockReturns.pop(i)
        AllStockBeta.pop(i)
        i-=1
    i+=1
print(len(AllStockReturns))


print("Done Loading")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

money = 100000000.0
Stock_limit = 20
Stock_limit = money*Stock_limit/100

beta_lower = 0.5
beta_upper = 1.2



#x0+x1+...xn = 40000
#b0/40000*x0+...bn/40000*xn = risk limit
row_one = []
row_two = []
i = 0
while(i<len(AllStockNames)):
    row_one.append(1)
    row_two.append(AllStockBeta[i]/money)
    
    i+=1


def rosen_der(x):
    jac = AllStockReturns
    return jac

    
def rosen_hess(x):
    hess = np.zeros_like(x)

    return hess



def rosen(x):
    #The Rosenbrock function
    return np.matmul(AllStockReturns,x)


from scipy.optimize import Bounds
bound = []
i = 0
while(i<len(AllStockNames)):
    bound.append([0, 7000000])
    i+=1
    

from scipy.optimize import LinearConstraint
linear_constraint = LinearConstraint([row_one, row_two], [money, beta_lower], [money, beta_upper])

x_int = np.zeros(len(AllStockNames))
i= 0
while(i<len(AllStockNames)-1):
    x_int[i] = money/len(AllStockNames)
    i+=1



print(money)
res = minimize(rosen, x_int, method='trust-constr', jac=rosen_der, hess=rosen_hess, constraints=[linear_constraint],bounds = bound)
portfolio = res.x
print(portfolio)

profit = 0

i = 0
avg_beta = 0
while(i<len(AllStockNames)):
    if(portfolio[i]<10):
        portfolio[i] = 0
    else:
        print(AllStockNames[i], round(portfolio[i],2), " = ", round(portfolio[i]/AllStockPrices[i],2))
        profit -= portfolio[i]*AllStockReturns[i]
        avg_beta += portfolio[i]*AllStockBeta[i]/money
        
        
    i+=1

print("Predicted Total Profit:", profit)
print("Yearly returns:",round(100*profit/money,2), "%")
print("Risk (weighted average beta value):", avg_beta)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////


money = float(input("How much money are you wanting to invest at once?"))
Stock_limit = float(input("Diversification? (Maximum % invested in any one stock)"))
Stock_limit = money*Stock_limit/100

beta_lower = float(input("Lower bound for risk?"))
beta_upper = float(input("Higher bound for risk?"))


#x0+x1+...xn = 40000
#b0/40000*x0+...bn/40000*xn = risk limit
row_one = []
row_two = []
i = 0
while(i<len(AllStockNames)):
    row_one.append(1)
    row_two.append(AllStockBeta[i]/money)
    
    i+=1


def rosen_der(x):
    jac = AllStockReturns
    return jac

    
def rosen_hess(x):
    hess = np.zeros_like(x)

    return hess



def rosen(x):
    #The Rosenbrock function
    return np.matmul(AllStockReturns,x)


from scipy.optimize import Bounds
bound = []
i = 0
while(i<len(AllStockNames)):
    bound.append([0, 7000])
    i+=1
    

from scipy.optimize import LinearConstraint
linear_constraint = LinearConstraint([row_one, row_two], [money, beta_lower], [money, beta_upper])

x_int = np.zeros(len(AllStockNames))
i= 0
while(i<len(AllStockNames)-1):
    x_int[i] = money/len(AllStockNames)
    i+=1



res = minimize(rosen, x_int, method='trust-constr', jac=rosen_der, hess=rosen_hess, constraints=[linear_constraint], bounds = bound)
portfolio = res.x
print(portfolio)

profit = 0

avg_beta = 0
i = 0
while(i<len(AllStockNames)):
    if(portfolio[i]<10):
        portfolio[i] = 0
    else:
        print(AllStockNames[i], round(portfolio[i],2), " = ", round(portfolio[i]/AllStockPrices[i],2))
        profit -= portfolio[i]*AllStockReturns[i]
        avg_beta += portfolio[i]*AllStockBeta[i]/money
        
        
    i+=1

print("Predicted Total Profit:", profit)
print("Yearly returns:",round(100*profit/money,2), "%")
print("Risk (weighted average beta value):", avg_beta)
