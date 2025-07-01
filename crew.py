from crewai import Crew,Process
from tools import yt_tool 
from agents import article_researcher,article_writer
from tasks import research_task,write_task
crew=Crew(
    agents=[article_researcher,article_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
print(result)