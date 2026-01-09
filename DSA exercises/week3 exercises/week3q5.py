def plan_itinerary(destinations, target_city):
    try:
        if target_city not in destinations:
            raise ValueError(f"City '{target_city}' not found.")
    except ValueError as e:
        return set(), [] 
    selected_attractions = set()  
    all_cities = list(destinations.keys())

    for city, attractions in destinations.items():
        if city == target_city:
        
            for attr in attractions:
                
                if attr.startswith('M'):
                    selected_attractions.add(attr) 

    return selected_attractions, all_cities

destinations = {
    "Paris": ["Eiffel Tower", "Museum Louvre"],
    "New York": ["Statue of Liberty", "Museum of Modern Art"]
}

print(plan_itinerary(destinations, "Paris"))
