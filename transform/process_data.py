# Logic to clean/transform data

def transform(raw_data):
    cleaned = []
    
    for holiday in raw_data:
        cleaned.append({
            "name": holiday["name"],
            "date_year": holiday["date_year"],
            "date_month": holiday["date_month"],
            "date":holiday["date"],
            "week_day": holiday["week_day"],
            "country": holiday["country"],
        })
        
    return cleaned

# I need to call this function in the main script and fix this 