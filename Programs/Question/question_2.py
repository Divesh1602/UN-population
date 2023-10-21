"""
ASEAN is a collection of South East Asian countries.
Plot a Bar Chat of the population of these countries.
Only use data for the year 2014
"""
import csv
import matplotlib.pyplot as plt


def execute():
    """This function is calculating the data needed for ploting the graph"""
    population_data_dict = {}
    with open(
        "../../Data/population-estimates_csv.csv",
        "r",
        encoding='utf-8'
     ) as file:
        population_data = csv.DictReader(file)
        country_list = [
            "Thailand", "Vietnam", "Indonesia", "Cambodia",
            "Brunei Darussalam", "Myanmar", "Malaysia", "Laos",
            "Philippines", "Singapore"
         ]
        for row in population_data:
            if row["Year"] == "2014":
                if row["Region"] in country_list:
                    population_data_dict[
                        row["Region"]
                    ] = int(float(row["Population"]))
    return population_data_dict


def plot(population_data_dict):
    """This function is calculating the data needed for ploting the graph"""
    plt.bar(population_data_dict.keys(), population_data_dict.values())
    plt.title("ASEAN country population in 2014")
    plt.xlabel(r"Country $\longrightarrow$")
    plt.ylabel(r"Population $\longrightarrow$")
    plt.xticks(rotation=270)
    plt.savefig(
        "../Figures/question_2_fig.png",
        bbox_inches="tight",
        pad_inches=0.2
    )
    plt.show()


if __name__ == '__main__':
    data_dict = execute()
    plot(data_dict)
