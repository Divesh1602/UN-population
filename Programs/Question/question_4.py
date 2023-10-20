import csv
import matplotlib.pyplot as plt


population_data_dict={}
with open("../../Data/population-estimates_csv.csv","r") as file:
	population_data=csv.DictReader(file)
	country_list=["Thailand","Vietnam","Indonesia","Cambodia","Brunei Darussalam","Myanmar","Malaysia","Laos","Philippines","Singapore"]
	for row in population_data:
		if int(row["Year"]) >= 2004 and int(row["Year"]) <= 2014:
			if row["Region"] in country_list:
				if int(row["Year"]) in population_data_dict:
					population_data_dict[int(row["Year"])][row["Region"]]=int(float(row["Population"]))
				else:
					population_data_dict[int(row["Year"])]={}
					population_data_dict[int(row["Year"])][row["Region"]]=int(float(row["Population"]))


years_list=list(population_data_dict.keys())
population_data=[]
country_list=[]
for year,country in population_data_dict.items():
	country_list=list(country.keys())
	population_data.append(list(country.values()))




bar_width = 0.1


colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

fig, ax = plt.subplots()
# fig.figure(figsize=(10,5))
for i in range(8):
	plt.bar(0,0,label=country_list[i],color=colors[i])
	bar_offset=0
for i in range(len(years_list)):
    for j in range(len(population_data[i])):
        bar = population_data[i][j]
        ax.bar(bar_offset, bar, width=bar_width,color=colors[j])
        bar_offset+=bar_width
    bar_offset+=bar_width*2
bar_positions=list(range(len(years_list)))
for i in range(len(bar_positions)):
	bar_positions[i]+=bar_width*3

ax.set_title("Population of ASEAN countries over the years 2004 - 2014")
ax.set_xlabel(r"Years $\longrightarrow$")
ax.set_ylabel(r"Population $\longrightarrow$")
ax.set_xticks(bar_positions,years_list)
plt.legend(loc=(0.92,0.55))
plt.savefig("../Figures/question_4_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.show()
