from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"] and job["max_salary"].isdigit()
        ]
        return max(salaries, default=0)

    def get_min_salary(self) -> int:
        salaries = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"] and job["min_salary"].isdigit()
        ]
        return min(salaries, default=0)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if not all(key in job for key in ("min_salary", "max_salary")):
            raise ValueError("Deve conter 'min_salary' e 'max_salary'.")

        try:
            min_salary = float(job["min_salary"])
            max_salary = float(job["max_salary"])
            current_salary = float(salary)
        except (ValueError, TypeError):
            raise ValueError("o valores devem ser numéricos.")

        if min_salary > max_salary:
            raise ValueError("'min_salary' não pode ser > 'max_salary'.")
        return min_salary <= current_salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
