from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="A orange cat",
)

image_url = response.data[0].url

print(image_url)
