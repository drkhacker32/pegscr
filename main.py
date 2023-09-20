from pyrogram import Client, filters
import re
import requests

API_ID = 24507409
API_HASH = "6110a1e8f610e7266ee92809504f10cb"
# you can add target chats here
source1_id = -1001613093650
source3_id = "@CashCardHubCC"
source2_id = "@teamnastyscr"
destination_chat_id = -1001819333581

app = Client(name="ultroid", api_id=API_ID, api_hash=API_HASH, phone_number='+94760005108')

def get_bin_data(bin_number):
    url = f'https://lookup.binlist.net/{bin_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}  # Add a User-Agent header to mimic a browser request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None
    
@app.on_message((filters.chat(source1_id) | filters.chat(source2_id) | filters.chat(source3_id)))
def forward_message(client, message):
    try:
        message = message.text
        pattern = r'(\d+\|\d+\|\d+\|\d+)'
        match = re.search(pattern, message)
        if match:
            card_number = match.group(1)
            bin_number = card_number[:6]
             # Replace with the BIN you want to look up
            bin_data = get_bin_data(bin_number)
            type = bin_data['type'].upper()
            brand = bin_data['brand'].upper()
            scheme = bin_data['scheme'].upper()
            country = bin_data['country']['name'].upper()

            sender_message = f"**CHECKED ✅**\n\n**CC** → `{card_number}`\n\n**BIN Info** : {scheme} - {type} - {brand}\n**Country** : {country} {bin_data['country']['emoji']}\n\n©️ @fckyou32"

            client.send_message(destination_chat_id, sender_message)

        #client.forward_messages(destination_chat_id, source_chat_id, [message.id])
    except Exception as e:
        print(f"Error forwarding message: {e}")

if __name__ == "__main__":
    print('Start sending cc to the Owner!')
    app.run()
