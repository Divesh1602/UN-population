"""
In this case for each year you have to calculate the sum
of the population of all SAARC countries.
Then plot a BAR CHART of Total SAARC population vs. year.
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
            "Afghanistan", "Bangladesh", "Bhutan", "India",
            "Maldives", "Nepal", "Pakistan", "Sri Lanka"
        ]
        for row in population_data:
            if row["Region"] in country_list:
                if row["Year"] in population_data_dict:
                    population_data_dict[
                        int(row["Year"])
                    ] += int(float(row["Population"]))
                else:
                    population_data_dict[
                        int(row["Year"])
                    ] = int(float(row["Population"]))
    return population_data_dict


def plot(population_data_dict):
    """This function is calculating the data needed for ploting the graph"""
    plt.bar(population_data_dict.keys(), population_data_dict.values())
    plt.title("Saarc country total population vs Years")
    plt.xlabel(r"Years $\longrightarrow$")
    plt.ylabel(r"Population $\longrightarrow$")
    plt.savefig(
        "../Figures/question_3_fig.png",
        bbox_inches="tight",
        pad_inches=0.2
    )
    plt.show()


if __name__ == '__main__':
    data_dict = execute()
    plot(data_dict)
