
# gpt_prompt.py
import ollama
import json

# Load user input
with open("trip_data.json", "r") as f:
    data = json.load(f)

# Build prompt from user input (simplified example)
prompt = f"""
Plan a {data['purpose']} trip for {data['num_travelers']} traveler(s) from {data['departure_place']} to {data['destinations']} 
from {data['dates']['start']} to {data['dates']['end']}. 
The weather of {data['destinations']} is {data['weather']}. also tell about the weather and tell the required precationary clothes to be taken.
Preferred activities: {', '.join(data['activities'])}.
Must-visit attractions: {data['must_visit']}.
Accommodation: {data['stay_type']} rated {data['star_rating']} stars.
Budget: {data['budget']} {data['currency']}.
Transportation modes: {', '.join(data['transport_modes'])}, travel class: {data['travel_class']}.
Meals: {', '.join(data['meal_type'])}.
Insurance: {data['insurance']}, Guide: {data['guide']}.
Additional notes: {data['notes']}.
The name of the person is {data['name']}.
if visa is required to travel from {data['departure_place']} to {data['destinations']} then tell about it in 2 lines also.
Now suggest an itinerary, estimate hotel and flight prices, and share tips.
make all this text in interesting format. and use tables and pointers in it.
"""

# Send to LLaMA 3.2
response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}]
)

# Only return the response message
print(response['message']['content'])
