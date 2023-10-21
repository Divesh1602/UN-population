"""
Grouped Bar Chart - ASEAN population vs. years
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
            "Brunei Darussalam", "Myanmar", "Malaysia",
            "Laos", "Philippines", "Singapore"
        ]
        for row in population_data:
            if int(row["Year"]) >= 2004 and int(row["Year"]) <= 2014:
                if row["Region"] in country_list:
                    if int(row["Year"]) in population_data_dict:
                        population_data_dict[
                            int(row["Year"])
                        ][row["Region"]] = int(
                                float(row["Population"])
                            )
                    else:
                        population_data_dict[int(row["Year"])] = {}
                        population_data_dict[
                            int(row["Year"])
                        ][row["Region"]] = int(
                                float(row["Population"])
                            )
    return population_data_dict


def transform(population_data_dict):
    """
    This function is extracting the data needed by
    matplotlib from the population data dict
    """
    years_list = list(population_data_dict.keys())
    population_data = []
    country_list = []
    for _, country in population_data_dict.items():
        country_list = list(country.keys())
        population_data.append(list(country.values()))
    plot(years_list, country_list, population_data)


def plot(years_list, country_list, population_data):
    """This function is calculating the data needed for ploting the graph"""
    bar_width = 0.1
    colors = [
        'red', 'green', 'blue', 'orange',
        'purple', 'cyan', 'magenta', 'yellow'
    ]
    _, axis = plt.subplots()
    for i in range(8):
        plt.bar(0, 0, label=country_list[i], color=colors[i])
    bar_offset = 0
    for i in enumerate(years_list):
        for j in enumerate(population_data[i[0]]):
            axis.bar(
                bar_offset,
                population_data[i[0]][j[0]],
                width=bar_width,
                color=colors[j[0]]
            )
            bar_offset += bar_width
        bar_offset += bar_width * 2
    bar_positions = list(range(len(years_list)))
    for i in enumerate(bar_positions):
        bar_positions[i[0]] += bar_width * 3
    axis.set_title("Population of ASEAN countries over the years 2004 - 2014")
    axis.set_xlabel(r"Years $\longrightarrow$")
    axis.set_ylabel(r"Population $\longrightarrow$")
    axis.set_xticks(bar_positions, years_list)
    plt.legend(loc=(0.92, 0.55))
    plt.savefig(
        "../Figures/question_4_fig.png",
        bbox_inches="tight",
        pad_inches=0.2
    )
    plt.show()


if __name__ == '__main__':
    data_dict = execute()
    transform(data_dict)
