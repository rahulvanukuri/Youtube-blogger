from crewai import Task
from tools import yt_tool 
from agents import article_researcher,article_writer

##Research task
research_task=Task(
    description=("identify the video {topic}."
                 "Get the detailed information about the yt video from the channel"),
    expected_output="A comprehensive 2 paragraphs report based on the {topic} of the video and its featured content",
    tools=[yt_tool],
    agent=article_researcher,
)

write_task=Task(
    description=("Get the info from the youtube channel on the {topic}"),
    expected_output="Summarize the info from the youtube channel video based on the {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=article_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)