import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',', quotechar='"')
            self.jobs_list = [row for row in csv_reader]

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            if 'job_type' in job:
                job_types.add(job['job_type'])
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict[str, str]
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        return [job for job in jobs
                if self._matches_criteria(job, filter_criteria)]

    def _matches_criteria(
            self, job: Dict[str, str],
            filter_criteria: Dict[str, str]) -> bool:
        for criterion, value in filter_criteria.items():
            if job.get(criterion) != value:
                return False
        return True
