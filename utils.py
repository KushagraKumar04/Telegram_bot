# utils.py
def get_daily_horoscope(sign, day):
    # For simplicity, this example uses a static response.
    # You should replace this with an actual API call or database query.
    horoscope_data = {
        "Aries": "Today is a great day to on personal growthh.",
        "Taurus": "You might find unexpected financial gainns today.",
        "Gemini": "Take Care of your health and be physically fit.",
        "Cancer": "You might find someone special in your life.",
        "Leo": "Today you might get an increment in your job .",
        # Add more signs and messages as needed.
    }
    
    return {
        "data": {
            "horoscope_data": horoscope_data.get(sign, "No horoscope available."),
            "date": day
        }
    }
