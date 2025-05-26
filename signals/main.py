with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

def decode_signals(input_data):
    code_to_possible_events = {}

    for codes_today, events_today in input_data:
        events_set = set(events_today)
        for code in codes_today:
            if code not in code_to_possible_events:
                code_to_possible_events[code] = events_set.copy()
            else:
                code_to_possible_events[code] = code_to_possible_events[code].intersection(events_set)

    decoded_map = {}
    codes_to_decode = set(code_to_possible_events.keys())

    while codes_to_decode:
        new_single_mappings_found = False
        
        for code in list(codes_to_decode):
            if len(code_to_possible_events[code]) == 1:
                event = code_to_possible_events[code].pop()
                decoded_map[code] = event
                codes_to_decode.remove(code)
                new_single_mappings_found = True
                
                for other_code in codes_to_decode:
                    if event in code_to_possible_events[other_code]:
                        code_to_possible_events[other_code].remove(event)
        
        if not new_single_mappings_found and codes_to_decode:
            break

    return decoded_map
    
    decoded_result = decode_signals(input)
    print(decoded_result)
