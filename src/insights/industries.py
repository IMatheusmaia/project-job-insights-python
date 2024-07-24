from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()
        self.jobs_list = []

    def get_unique_industries(self) -> List[str]:
        return list(
            {row["industry"] for row in self.jobs_list
             if row["industry"]})
