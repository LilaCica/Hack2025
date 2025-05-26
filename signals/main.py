with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

def decode_signals(days):
    from collections import defaultdict

    possible = defaultdict(set)  # kód -> lehetséges események

    # 1. Gyűjtés: minden kódhoz felvesszük a potenciális eseményeket
    for codes, events in days:
        for code in codes:
            if code in possible:
                possible[code] &= set(events)  # Metszet: csak a közösek maradnak
            else:
                possible[code] = set(events)

    final_mapping = {}

    # 2. Fokozatos szűkítés – amíg van új egyértelmű megfejtés
    while possible:
        # Azok a kódok, amelyeknek már csak 1 lehetséges eseményük van
        resolved = {code: list(events)[0] for code, events in possible.items() if len(events) == 1}

        if not resolved:
            break  # nincs további egyértelmű megfejtés

        # Frissítjük a végleges megfejtést
        for code, event in resolved.items():
            final_mapping[code] = event
            del possible[code]

        # Eseményt eltávolítjuk a többi kód lehetséges értékei közül
        for event in resolved.values():
            for code in possible:
                possible[code].discard(event)

    return final_mapping

decoded = decode_signals(input)
print(decoded)
