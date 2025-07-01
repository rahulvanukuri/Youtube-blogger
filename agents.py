from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
load_dotenv()
#Create a ideas analyzer or content researcher
os.environ["OPENAI_API_KEY"]=os.getenv("OPEN_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"
llm = ChatOpenAI(
    model_name="gpt-4-0125-preview",
    temperature=0.7,
    openai_api_key=os.getenv("OPEN_API_KEY")
)
article_researcher=Agent(role='Article research trending',
                       goal='get the best trending research for the topic{topic} from the research archive',
                       verbose=True,
                       memory=True,
                       backstory={
                           "this research agent is an expert on the domain of trending technologies like Diffusion models,crossattention and GenAI tools."
                       },
                       tools=[yt_tool],
                       llm=llm,
                       allow_delegation=True)

#Creating a senior writer agent for blog
article_writer=Agent(role='Article writer',
                     goal='Narrate the entire compelling tech knowledge in simple layman terms about{topic}from the archive',
                     verbose=True,
                     memory=True,
                     backstory={
                        "A former tech journalist turned AI communicator, the Article Writer once traveled the world covering major technology summits, interviewing inventors, and demystifying innovations for everyday readers. Frustrated by how often groundbreaking advancements were misunderstood or ignored due to jargon-heavy reporting, the Article Writer dedicated themselves to a new mission: making complex technology understandable and engaging for everyone—from curious" 
                        "teenagers to seasoned professionals outside the tech world.Trained on thousands of real-world stories, metaphors, and analogies, the Article Writer combines storytelling expertise with technical accuracy. Their passion lies in translating the language of engineers and scientists into relatable, human narratives that spark curiosity, reduce fear of the unknown, and invite readers into the exciting world of technology."
                     },
                     tools=[yt_tool],
                     allow_delegation=False
                     )