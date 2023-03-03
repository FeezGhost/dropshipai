import openai

from .models import Product

# use your own api key
openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def GetSuggestion():
# get unique product in 5 words or less

    product = generate_response("Can you name one single unique product in no more than 5 words (limitations: no food, NO NAME BRAND PRODUCTS, something that can be shipped on the internet)")

# get store name
    store_name = generate_response(f"Recommend a store name for {product}")

# get platform
    platform = generate_response(f"Recommend one platform to advertise {product}")

# get username
    username = generate_response(f"Recommend a username for a social account that advertises {product}")

# get bio
    bio = generate_response(f"Create a BIO for a social media account that sells {product}")

# get marketing campaign
    marketing_campaign = generate_response(f"What would be an effective 5-step marketing campaign for {product} on {platform}")

# get web design
    web_design = generate_response(f"code an E-commerce website that sells {product} with the name {store_name} and has a simple, modern, sleek, consistent, and effective design for the user to purchase {product} and that includes: unique colorscheme, catalog page, add to cart, and mission statement. All in HTML")

#GET ad idea
    ad_idea = generate_response(f"Create an idea for an video Advert for an E-commerce store that sells {product} and is named {store_name} and whose marketing plan is {marketing_campaign}")

#scaling advice
    scaling = generate_response(f"Create a 5-step plan in order to help scale an E-commerce store that sells {product} and is named {store_name} and whose markeitng plan is {marketing_campaign} and is beign addvertized on {platform}")
    productCreated = {
        'product'            : product,
        'store_name'         : store_name,
        'platform'           : platform,
        'username'           : username,
        'bio'                : bio,
        'marketing_campaign' : marketing_campaign,
        'web_design'         : web_design,
        'ad_idea'            : ad_idea,
        'scaling'            : scaling
    }
    return productCreated

# product, store_name, platform, username, bio, marketing_campaign, web_design, ad_idea, scaling = GetSuggestion(generate_response)

# # display the outputs
# print("Product: ", product)
# print("Store Name: ", store_name)
# print("Platform: ", platform)
# print("Username: ", username)
# print("Bio: ", bio)
# print("Marketing Campaign: ", marketing_campaign)
# print("Website: ", web_design)
# print("First AD: ", ad_idea)
# print("scaling: ", scaling)