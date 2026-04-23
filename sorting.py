import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    seznam_novy = seznam.copy()
    delka = len(seznam_novy)
    for i in range(delka):

        nejmensi = seznam_novy[i]
        nejmensi_index = i

        for index in range(i+1,len(seznam)):
            if seznam_novy[index] < nejmensi:
                nejmensi = seznam_novy[index]
                nejmensi_index = index

        seznam_novy[i], seznam_novy[nejmensi_index] = seznam_novy[nejmensi_index], seznam_novy[i]

    return seznam_novy

def bubble_sort(seznam):
    noovy = seznam.copy()
    delka = len(noovy)
    plt.ion()
    plt.show()
    zmena = True
    while zmena:
        zmena = False
        for i in range(len(noovy)-1):
            if noovy[i] > noovy[i+1]:
                noovy[i], noovy[i+1] = noovy[i+1], noovy[i]
                zmena = True
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return noovy






if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    # print(selection_sort(values))
    print(bubble_sort(values))