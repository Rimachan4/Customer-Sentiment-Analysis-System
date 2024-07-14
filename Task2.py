import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Streamlit setup
st.title("Customer Sentiment Analysis System")

# Initialize the language model (llm)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

# instruction
instruction = '''Based on the customer sentiment and their reviews draft an Email with Customer name and Email from the review.
For positive review, send a thank you email to customer and also recommend a new product for them to try
For negative review, send an apology email to customer and also send an internal mail to a senior customer service representative to address customer concern
'''

#review
reviews=[
{
    "customer_name": "Isabella Garcia",
    "customer_email": "igarcia@email.com",
    "text": """
    These premium wireless earbuds exceeded my expectations! The sound quality is exceptional, with rich bass and crystal-clear highs. The noise cancellation feature blocks out distractions, allowing me to focus on my music or calls. They're incredibly comfortable and secure, perfect for my daily commute and workouts. The touch controls are intuitive, and the charging case is sleek and compact. I also appreciate the fast charging and long battery life. Overall, a fantastic investment!
    """
},

{
    "customer_name": "Ethan Wilson",
    "customer_email": "ewilson@email.com",
    "text": """
    I'm impressed by the sound quality and comfort of these sports earbuds. They stay put during my runs and bike rides, and the IPX5 sweat resistance is a lifesaver. The ear hooks provide extra stability, and the touch controls are easy to use. The charging case is a bit bulkier than I'd like, but it's still pocket-friendly. The quick-charging feature is a lifesaver when I forget to charge them overnight. I'd recommend their armband phone case for a secure way to carry my phone during workouts.
    """
},

{
    "customer_name": "Sophia Anderson",
    "customer_email": "sophia.a@email.com",
    "text": """
    These true wireless earbuds are a steal for the price! The sound is well-balanced, and the passive noise isolation effectively blocks out background noise. They're incredibly lightweight and comfortable for extended wear. The touch controls are responsive, and the case is small enough to fit in my purse. I also appreciate the multipoint connection feature, allowing me to switch between devices seamlessly. The battery life could be slightly better, but it's still decent for the price. I'd recommend their compact wireless charging pad for easy charging on the go.
    """
},
{
    "customer_name": "Alexander Clark",
    "customer_email": "aclark@email.com",
    "text": """
    I wanted to love these designer earbuds for their unique look, but the sound quality fell short. The bass is overpowering, and the highs sound tinny. The touch controls are finicky and often don't register my input. The case is bulky and feels cheap. On the bright side, the design and color options are eye-catching. However, I expected better performance for the price. I'd steer clear of these and opt for a more reliable brand.
    """
},


{
    "customer_name": "Olivia Thompson",
    "customer_email": "olivia.t@email.com",
    "text": """
    I bought these affordable wireless earbuds on a whim, but they've been underwhelming. The sound is muddy, and there's a noticeable delay during video calls. The connection keeps dropping, and the touch controls are unreliable. The case is lightweight, but the build quality feels flimsy. On the plus side, the battery life is decent, and they're comfortable to wear. I'd recommend spending a bit more on a reliable brand for better performance and connectivity.
    """
} ]


# Products
products = [
    "Protective Carrying Case",
    "Earbud Tips Replacement Pack",
    "Wireless Charging Pad",
    "Waterproof Case"
]

# Prompt template
review_template = """
You are a helpful AI assistant. Review from {customer_name} ({customer_email}):{reviews}
Analyze the review based on the customer sentiment - positive or negative.
"""

# Output parser
output_parser = StrOutputParser()

#Review analysis
def analyze(reviews):
  analyze_review=[]
  for review in reviews:
    prompt = ChatPromptTemplate.from_template(review_template)
    chain = prompt | llm | output_parser
    formatted_prompt1={
      "reviews": review["text"],
      "customer_name": review["customer_name"],
      "customer_email": review["customer_email"]
    }
    result = chain.invoke(formatted_prompt1)
    analyze_review.append(result)
  return analyze_review


#Template to generate Email
email_template ='''
You are a helpful AI assistant. You have access to the following instructions: {instruction}.
Based on the review analysis draft Emails according to the instructions, review analysis: {analyze_review}.
My company name is Horizon 
'''


prompt = ChatPromptTemplate.from_template(email_template)



def get_response():
    analysis=analyze(reviews)
    chain = prompt | llm | output_parser
    formatted_prompt2 = {
        "instruction": instruction,
        "analyze_review":  "\n".join(analysis),}
    result = chain.invoke(formatted_prompt2)
    st.write(result)

get_response()
