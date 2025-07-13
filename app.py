# Before viewing the code, add three variables in .env file, which is:
# LANGCHAIN_API_KEY="langchain_api_key" -> Get it from the langSmith portal.
# OPENAI_API_KEY="open_ai_api_key" -> Get it from the openai plattform.
# LANGCHAIN_PROJECT="Name of a Project" -> Any name which will be shown in langsmith portal as a project name.

# Importing Libraries
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Importing the environment variables
load_dotenv()
# OPENAI_API_KEY
open_api_key = os.getenv("OPENAI_API_KEY")
if open_api_key is not None:
    os.environ["OPENAI_API_KEY"] = open_api_key
# LANGCHAIN_API_KEY
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# LANGCHAIN_TRACING_V2 - For tracing the project when we update it. v2 means versions 2 (Always true - so we trace the project)
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt is
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You ar a helpful asssitant. Your task is to reponse to the user request only based on the given context."),
        ("user","Question: {question}\nContext:{context}"),
    ]
)

# Model is
llm = ChatOpenAI(
    model='gpt-3.5-turbo'
)

# Chain is
chain = prompt | llm | StrOutputParser()

# Question & context is
quesiton="who develop you??"
context=""" Even though you are only a very small speck of ocean, of the 300 million children on whose shoulders the future of India rests, you can ignite the minds, light the fire, become a burning candle to light another candle. My dear children, you work in the school for about 25000 hours before you complete 12th std. Within the school curriculum / school hours, I want you to contribute to the Mission of Developed India by involving in the student centric activities like Literacy Development, Eco-Care Movement.

India after its independence was determined to move ahead with planned policies for Science & Technology. Now, India is very near to self-sufficiency in food, making the ship to mouth existence of 1950s, an event of the past. Also improvements in the health sector, have eliminated few contagious diseases. There is a increase in life expectancy. Small scale industries provide high percentage of National GDP - a vast change in 1990s compared to 1950s. Today India can design, develop and launch world class geo-stationary and sun synchronous, remote sensing satellites.

The nuclear establishments have reached the capability of building nuclear power stations, nuclear medicine and nuclear irradiation of agricultural seeds for growth in agricultural production. Today India has become a Nuclear Weapon State. Defence Research had led to design, development and production of Main Battle Tanks, strategic missile systems, electronic warfare systems and various armours. India is a missile power. Also we have seen growth in the Information Technology; the country is progressing in hardware and software export business of more than 10 billion dollars even though there are low ebbs in the last few years. India yet is a developing country. What Technology can do further?

Technology has multiple dimensions. Geopolitics convert the technology to a particular nation's policy. The same policy will lead to economic prosperity and capability for national security. For example, the developments in chemical engineering brought fertilizers for higher yield of crops while the same science led to chemical weapons. Likewise, rocket technology developed for atmospheric research helped in launching satellites for remote sensing and communication applications which are vital for the economic development. The same technology led to development of missiles with specific defense needs that provides security for the nation. The aviation technology development has led to fighter and bomber aircraft, and the same technology will lead to passenger jet and also help operations requiring quick reach of support to people affected by disasters. At this stage, let us study global growth of technology and impact in human life."""

# Running the chain
print(chain.invoke({'question':quesiton,'context':context}))


# Once you run this dummy project then as a your project_name will be shown on langSmith portal(https://smith.langchain.com/)
# Then select that project and sees different things like: charts, error_rate, tracing, calls,..etc..