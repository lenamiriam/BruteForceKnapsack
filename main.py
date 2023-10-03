# Wczytanie danych z pliku
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        k, n = map(int, lines[0].split(' '))
        masses = list(map(int, lines[1].split(',')))
        values = list(map(int, lines[2].split(',')))
    return k, n, masses, values


# Funkcja brute force
def brute_force_knapsack(k, n, masses, values):
    # Inicjalizacja danych
    best_value = 0
    best_weight = 0
    best_combination = []

    # Obliczenie liczby iteracji (tyle ile kombinacji), 2 do potęgi n
    num_iterations = 2 ** n

    # Pętla iterująca aż do osiągnięcia ostatniej iteracji
    for i in range(num_iterations):
        # Przekształcenie liczby i na jej reprezentację binarną o długości n i zapisanie jej w zmiennej combination
        # bin(i) zamienia i na jej reprezentację binarną, [2:] wycina 2 pierwsze znaki, czyli 0b,
        # zfill(n) dodaje zera na początku sekwencji bitów tak aby osiągnąć długość docelową n
        combination = bin(i)[2:].zfill(n)
        current_value = 0
        current_weight = 0

        # Pętla iterująca po wektorze
        for j in range(n):
            # Jeśli któraś z wartości sładowych wektora to 1 to dodajemy
            # do current_value i current_weight odpowiednie wartości z list
            if combination[j] == '1':
                current_value += values[j]
                current_weight += masses[j]

        # Sprawdzenie czy obecna current_weight jest mniejsza/równa maksymalnej wadze i czy current_value
        # jest większa od najlepszej wartości i aktualizacja wartości zmiennych
        if current_weight <= k and current_value > best_value:
            best_weight = current_weight
            best_value = current_value
            # Utworzenie listy z kombinacji
            best_combination = list(combination)

        print(f"Iteration number: {i}, Best value: {best_value}, Best weight: {best_weight}, Best combination {best_combination}")

    return best_combination


# Wczytanie ścieżki do pliku
while True:
    try:
        file_path = input("Type file path: ")
        k, n, masses, values = read_input_file(file_path)
        break
    except FileNotFoundError:
        print("File not found. The path was incorrect. Try once again.")

best_combination = brute_force_knapsack(k, n, masses, values)

# Wynik, czyli najlepsza kombinacja w postaci wektoru, suma wartości i wag
print("\nResult:")
print("Best combination:", best_combination)
print("Best value:", sum(values[i] for i in range(n) if best_combination[i] == '1'))
print("Best weight:", sum(masses[i] for i in range(n) if best_combination[i] == '1'))
