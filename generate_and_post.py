import random
import json
import requests

sample_data = {
    "Invoice": [
        "Invoice number {num} due {date} amount ${amount}",
        "Invoice #{num} total due ${amount} client {client}",
        "Bill for project {client} dated {date} - total amount ${amount}"
    ],
    "Receipt": [
        "Receipt for payment of ${amount} made on {date}",
        "Receipt issued for subscription on {date}, total ${amount}",
        "Payment received on {date} - amount: ${amount}"
    ],
    "Timesheet": [
        "Employee timesheet for {month}, hours worked {hours}",
        "Timesheet log for {name} for {month} {day}",
        "{name}'s work hours recorded: {hours} hrs in {month}"
    ]
}

clients = ["ABC Ltd", "XYZ Corp", "MegaBuild", "QuickSoft"]
names = ["John Doe", "Jane Smith", "Alice Brown", "Michael Chan"]
months = ["January", "February", "March", "April", "May", "June"]

dataset = []
for _ in range(20):
    label = random.choice(list(sample_data.keys()))
    template = random.choice(sample_data[label])
    text = template.format(
        num=random.randint(10000, 99999),
        date=f"2023-{random.randint(1,12):02}-{random.randint(1,28):02}",
        amount=random.randint(100, 1000),
        client=random.choice(clients),
        name=random.choice(names),
        month=random.choice(months),
        day=random.randint(1, 28),
        hours=random.randint(40, 200)
    )
    dataset.append({"text": text, "label": label})
    
    try:
        res = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"text": text},
            headers={"Content-Type": "application/json"}
        )
        prediction = res.json()
    except Exception as e:
        prediction = {"error": str(e)}

    print(f"Text: {text}\n→ Prediction: {prediction}\n")

dataset[:5]  # shows some generated samples
