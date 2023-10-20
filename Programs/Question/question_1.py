import csv
import matplotlib.pyplot as plt


population_data_dict={}
with open("../../Data/population-estimates_csv.csv","r") as file:
	population_data=csv.DictReader(file)
	for row in population_data:
		if row["Region"]=="India":
			population_data_dict[int(row["Year"])]=int(float(row["Population"]))


plt.bar(population_data_dict.keys(),population_data_dict.values())
plt.title("Indian population vs Years")
plt.xlabel(r"Years $\longrightarrow$")
plt.ylabel(r"Population $\longrightarrow$")
plt.savefig("../Figures/question_1_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.show()