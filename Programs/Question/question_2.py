import csv
import matplotlib.pyplot as plt


population_data_dict={}
with open("../../Data/population-estimates_csv.csv","r") as file:
	population_data=csv.DictReader(file)
	country_list=["Thailand","Vietnam","Indonesia","Cambodia","Brunei Darussalam","Myanmar","Malaysia","Laos","Philippines","Singapore"]
	for row in population_data:
		if row["Year"]=="2014":
			if row["Region"] in country_list:
				population_data_dict[row["Region"]]=int(float(row["Population"]))


plt.bar(population_data_dict.keys(),population_data_dict.values())
plt.title("ASEAN country population in 2014")
plt.xlabel(r"Country $\longrightarrow$")
plt.ylabel(r"Population $\longrightarrow$")
plt.xticks(rotation=270)
plt.savefig("../Figures/question_2_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.show()