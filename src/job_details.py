"""
job_details.py

This script extracts detailed job information from individual job listing pages.
It scrapes key job attributes such as experience, salary, location, and 
required skills from the job posting.

Main functionalities:
1. Fetches the HTML content of a job listing page.
2. Extracts:
   - Required experience
   - Salary range
   - Job location
   - Required skills
3. Returns the extracted job details as a dictionary.

Usage:
- Call `JobDetails.get_job_details(job_url)` with a valid job listing URL 
  to retrieve structured job details.

"""

import requests
from bs4 import BeautifulSoup
import re


class JobDetails:
    """
    Extracts detailed job information from a given job listing page.
    """

    @staticmethod
    def get_job_details(job_url):
        """
        Fetches detailed job information such as experience, salary, location, 
        and required skills from a job listing page.

        :param job_url: The URL of the job listing.
        :return: Dictionary containing job details.
        """
        if job_url == 'N/A':
            return {}

        response = requests.get(job_url)

        if response.status_code != 200:
            print(f"Failed to fetch job details from {job_url}. Status code: {response.status_code}")
            return {}

        job_soup = BeautifulSoup(response.text, 'lxml')

        # Extract experience and salary details
        details_list = job_soup.find('ul', class_='top-jd-dtl d-flex mt-8')
        experience, salary = 'N/A', 'N/A'

        if details_list:
            list_items = details_list.find_all('li')
            for li in list_items:
                text = " ".join(li.stripped_strings)
                text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
                if li.find('i', class_='srp-icons experience'):
                    experience = text
                elif li.find('i', class_='srp-icons salary'):
                    salary = text

        # Extract location
        location_tag = job_soup.find('span', class_='job-location-trunicate')

        # Extract required skills
        skill_tags = job_soup.find_all('span', class_='jd-skill-tag')
        skills = [re.sub(r'\s+', ' ', skill.text.strip()) for skill in skill_tags if skill.text.strip()]

        return {
            "experience": experience,
            "salary": salary,
            "location": location_tag.text.strip() if location_tag else 'N/A',
            "skills": skills
        }
