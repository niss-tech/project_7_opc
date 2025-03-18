import csv

def read_csv(file):
    actions = []
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()}
            name = row['Actions']
            cost = float(row['Coût'])
            profit = float(row['Bénéfice'].replace('%', '')) / 100
            if cost > 0 and profit > 0:
                actions.append({'name': name, 'cost': cost, 'profit': profit})
    return actions

def get_best_combination_optimized(actions, max_budget):
    num_actions = len(actions)
    dp = [[0 for _ in range(max_budget + 1)] for _ in range(num_actions + 1)]

    for i in range(1, num_actions + 1):
        for budget in range(max_budget + 1):
            action = actions[i - 1]
            cost = action['cost']
            profit = action['profit'] * cost
            
            if cost > budget:
                dp[i][budget] = dp[i - 1][budget]
            else:
                dp[i][budget] = max(dp[i - 1][budget], dp[i - 1][budget - int(cost)] + profit)

    best_combination = []
    budget = max_budget
    total_profit = round(dp[num_actions][max_budget], 2)  # ✅ Arrondi à deux décimales
    total_cost = 0

    for i in range(num_actions, 0, -1):
        if dp[i][budget] != dp[i - 1][budget]:
            action = actions[i - 1]
            best_combination.append(action)
            budget -= int(action['cost'])
            total_cost += action['cost']

    return best_combination, total_profit, total_cost

def main():
    file = 'Liste_actions.csv'
    actions = read_csv(file)
    max_budget = 500

    best_combination, best_profit, total_cost = get_best_combination_optimized(actions, max_budget)

    if best_combination:
        print("\n🥇 Meilleure combinaison optimisée :")
        for action in best_combination:
            # ✅ Arrondi du bénéfice individuel à deux décimales
            profit = round(action['profit'] * action['cost'], 2)
            print(f"{action['name']} - Coût : {action['cost']}€ - Bénéfice : {profit}€")
        print(f"\n💰 Coût total : {total_cost:.2f}€")  # ✅ Arrondi à deux décimales
        print(f"💰 Profit total : {best_profit:.2f}€")  # ✅ Arrondi à deux décimales
    else:
        print("\n❌ Aucune combinaison rentable dans la limite de 500€.")

if __name__ == "__main__":
    main()
