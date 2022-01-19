from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

def create_bar_chart(id):
    plt.bar(range(len(drinks)), sales)
    ax = plt.subplot()
    ax.set_xticks(range(len(drinks)))
    ax.set_xticklabels((drinks), rotation=20)
    plt.xlabel("drinks")
    plt.ylabel("sales")
    plt.savefig(f"static/{id}.png")
    plt.savefig(f"static/{id}.png")
    plt.close()
