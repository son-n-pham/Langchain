import os
import requests

# # This is to use the PROXYCURL API to scrape the information from the LinkdIn profile
# # Don't need it, just create a gist in Github to store a profile for practice
# def scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/son-n-pham/"):
#     """scrape informaiton from LinkedIn profile,
#     Manually scrape the information from the LinkdIn profile"""

#     api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
#     linkedin_profile_url = 'https://www.linkedin.com/in/williamhgates'
#     PROXYCURL_API_KEY = os.environ.get('PROXYCURL_API_KEY')
#     header_dic = {'Authorization': f'Bearer {PROXYCURL_API_KEY}'}

#     response = requests.get(api_endpoint,
#                             params={'url': linkedin_profile_url},
#                             headers=header_dic)

#     return response


def scrape_linkedin_profile(url='https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json'):
    response = requests.get(url)
    data = response.json()

    data = {
        k: v for k, v in data.items() if v not in ([], '', None) and k not in ('people_also_view', 'certifications')
    }

    if data.get('groups'):
        for group_dict in data.get('groups'):
            group_dict.pop('profile_pic_url')
    return data
