from airflow.decorators import dag, task
import pendulum
# build out of data and time

import requests
import xmltodict


@dag(
    dag_id='podcast_summary2',
    schedule_interval='@daily',
    start_date=pendulum.datetime(2024, 6, 23),
    catchup=False
)
def podcast_summary2():
    pass 
    @task()
    def get_episodes():
        link = "https://marketplace.org/feed/podcast/marketplace"
        data = requests.get("https://marketplace.org/feed/podcast/marketplace")
        feed = xmltodict.parse(data.text)
        episodes= feed["rss"]["channel"]["item"]
        print(f"Found {len(episodes)} episodes.")
        return episodes
    podcast_episodes = get_episodes()


summary = podcast_summary2()
