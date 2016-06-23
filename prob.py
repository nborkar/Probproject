p = collections.Counter(x)
print (p)
count_of_sum = sum(p.values())
for k,v in p.items():
	print("The frequency of number" + str(k) + "is" + str(float(v)/count_of_sum))
	
plt.hist(testlist, histtype="bar")
plt.show()

plt.boxplot(testlist)
plt.show()

plt.figure()
x = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
x = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph