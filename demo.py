import requests

# ✅ API ana bilgileri (kendi API key'in ile değiştir)
base_url = "https://generativelanguage.googleapis.com"
api_key = "YOUR_API_KEY"  # <-- kendi API anahtarını buraya yaz

# ✅ Gönderilecek prompt ve ayarlar
payload = {
    "contents": [
        {
            "parts": [
                {"text": "Translate 'Hello' to French."}
            ]
        }
    ]
}
params = {
    "key": api_key
}

# ✅ Tam endpoint URL'si
full_url = f"{base_url}/v1beta/models/gemini-pro:generateContent"

# ✅ POST isteği gönderilir
response = requests.post(full_url, params=params, json=payload)

# ✅ Yanıt kontrolü
if response.status_code == 200:
    result = response.json()
    print("✅ Gemini Output:\n", result['candidates'][0]['content']['parts'][0]['text'])
else:
    print("❌ API Error:", response.status_code, response.text)
