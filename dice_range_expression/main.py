with open('./input.txt', 'r') as f:
  input = f.read()

print(input)
def dice_range_expression(min_val, max_val):
    dice_sizes = [20, 10, 8, 6, 4, 3, 2]
    range_size = max_val - min_val + 1
    best_expr = None

    # Próbáljuk ki az összes dobókockát különböző számú példányban
    for i in range(1, 4):  # Legfeljebb 3 kockát kombinálunk
        from itertools import product
        for combo in product(dice_sizes, repeat=i):
            combo = sorted(combo, reverse=True)
            total_min = sum(1 for _ in combo)
            total_max = sum(d for d in combo)
            total_range = total_max - total_min + 1

            if total_range == range_size:
                offset = min_val - total_min
                # Kifejezés összeállítása
                expr = '+'.join(f"1d{d}" for d in combo)
                if offset != 0:
                    expr += f"{offset:+d}"
                # Legyen ez a legjobb, ha kevesebb kockát használunk
                if best_expr is None or len(combo) < best_expr[0]:
                    best_expr = (len(combo), expr)

    if best_expr:
        return best_expr[1]
    else:
        return "N/A"

print(dice_range_expression(2, 5))      # ➜ 1d4+1
print(dice_range_expression(1, 23))     # ➜ 1d4+1d20-1
print(dice_range_expression(5, 10))     # ➜ 1d6+4
