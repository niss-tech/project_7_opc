import csv

#  Fonction pour lire le fichier CSV
def read_csv(file):
    actions = []
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()}
            name = row['Actions']
            cost = float(row['Coût'])

            profit_str = row['Bénéfice']
            if '%' in profit_str:
                #  Si le bénéfice est en pourcentage → le convertir en décimal
                profit = float(profit_str.replace('%', '')) / 100
            else:
                #  Si le bénéfice est une valeur brute → le ramener entre 0 et 1
                profit = float(profit_str) / 100

            #  On ne prend que les actions valides (coût > 0 et bénéfice > 0)
            if cost > 0 and profit > 0:
                actions.append({'name': name, 'cost': cost, 'profit': profit})
    return actions

#  Fonction pour obtenir la meilleure combinaison optimisée
def get_best_combination_optimized(actions, max_budget):
    num_actions = len(actions)

    #  Conversion du budget en centimes pour une meilleure précision
    max_budget = int(max_budget * 100)

    #  Crée une table (initialisée à 0)
    dp = [[0 for _ in range(max_budget + 1)] for _ in range(num_actions + 1)]

    for i in range(1, num_actions + 1):
        for budget in range(max_budget + 1):
            action = actions[i - 1]
            cost = int(action['cost'] * 100)  #  Conversion du coût en centimes
            profit = action['profit'] * action['cost']

            if cost > budget:
                dp[i][budget] = dp[i - 1][budget]
            else:
                dp[i][budget] = max(dp[i - 1][budget], dp[i - 1][budget - cost] + profit)

    #  Reconstruction de la meilleure combinaison
    best_combination = []
    budget = max_budget
    total_profit = round(dp[num_actions][max_budget], 2)
    total_cost = 0

    for i in range(num_actions, 0, -1):
        cost = int(actions[i - 1]['cost'] * 100)
        if budget >= cost and dp[i][budget] == dp[i - 1][budget - cost] + actions[i - 1]['profit'] * actions[i - 1]['cost']:
            action = actions[i - 1]
            best_combination.append(action)
            budget -= cost
            total_cost += action['cost']

    return best_combination, total_profit, round(total_cost, 2)

#  Fonction principale
def main():
    file = 'Liste_actions.csv'  #  Change le nom du fichier ici si besoin
    actions = read_csv(file)
    max_budget = 500  #  Budget en euros

    best_combination, best_profit, total_cost = get_best_combination_optimized(actions, max_budget)

    if best_combination:
        print("\n🥇 Meilleure combinaison optimisée :")
        for action in best_combination:
            profit = round(action['profit'] * action['cost'], 2)
            print(f"{action['name']} - Coût : {action['cost']}€ - Bénéfice : {profit}€")
        print(f"\n💰 Coût total : {total_cost:.2f}€")
        print(f"💰 Profit total : {best_profit:.2f}€")
    else:
        print("\n❌ Aucune combinaison rentable dans la limite de 500€.")

if __name__ == "__main__":
    main()
