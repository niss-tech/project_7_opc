import csv
import itertools

def read_csv(file):
    actions = []
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()}
            name = row['Actions']
            cost = float(row['Coût'])
            profit = float(row['Bénéfice'].replace('%', '')) / 100
            actions.append({'name': name, 'cost': cost, 'profit': profit})
    return actions

# Lire le fichier CSV
file = 'Liste_actions.csv'
actions = read_csv(file)

def generate_combinations(actions):
    all_combinations = []
    for size in range(1, len(actions) + 1):
        combinations = itertools.combinations(actions, size)
        all_combinations.extend(combinations)
    return all_combinations

def get_best_combination(combinations, max_budget):
    best_profit = 0
    best_combination = None

    for combination in combinations:
        # Calcul du coût total
        total_cost = sum(action['cost'] for action in combination)
        # Calcul du bénéfice total
        total_profit = sum(action['profit'] * action['cost'] for action in combination)

        # Vérification du budget et comparaison des bénéfices
        if total_cost <= max_budget and total_profit > best_profit:
            best_profit = total_profit
            best_combination = combination

    return best_combination, best_profit

# Générer toutes les combinaisons
all_combinations = generate_combinations(actions)
max_budget = 500

# Trouver la meilleure combinaison
best_combination, best_profit = get_best_combination(all_combinations, max_budget)

# Affichage du résultat
if best_combination:
    total_cost = sum(action['cost'] for action in best_combination)  # Calcul du coût total
    print("\n🥇 Meilleure combinaison d'actions :")
    for action in best_combination:
        print(f"{action['name']} - Coût : {action['cost']}€ - Bénéfice : {action['profit'] * action['cost']}€")
    print(f"\n💰 Coût total : {total_cost}€")  # Affichage du coût total
    print(f"💰 Profit total : {best_profit}€")
else:
    print("\n❌ Aucune combinaison rentable dans la limite de 500€.")
