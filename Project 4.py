import requests

import json

class Covid:
    def __init__(self, daily_state, daily_statecode, daily_active, daily_confirmed, daily_deaths, daily_recovered):
        self.daily_state = daily_state
        self.daily_statecode = daily_statecode
        self.daily_active = daily_active
        self.daily_confirmed = daily_confirmed
        self.daily_deaths = daily_deaths
        self.daily_recovered = daily_recovered

    def __str__(self):
        return "{} | {} | {} | {} | {} | {}\n".format(self.daily_state, self.daily_statecode, self.daily_active, self.daily_confirmed, self.daily_deaths, self.daily_recovered)


class fetchapidata:

    def fetch(self, save_data):

        url = "https://api.covid19india.org/data.json"
        response = requests.get(url)
        covid_data = json.loads(response.text)
        covid_data_daily = covid_data["statewise"]
        i = 0
        covid_data_state = []
        covid_data_statecode = []
        covid_data_active = []
        covid_data_confirmed = []
        covid_data_deaths = []
        covid_data_recovered = []

        for i in range(0, len(covid_data_daily)):
            covid_data_state.append(covid_data_daily[i]["state"])

        for i in range(0, len(covid_data_daily)):
            covid_data_statecode.append(covid_data_daily[i]["statecode"])

        for i in range(0, len(covid_data_daily)):
            covid_data_active.append(covid_data_daily[i]["active"])

        for i in range(0, len(covid_data_daily)):
            covid_data_confirmed.append(covid_data_daily[i]["confirmed"])

        for i in range(0, len(covid_data_daily)):
            covid_data_deaths.append(covid_data_daily[i]["deaths"])

        for i in range(0, len(covid_data_daily)):
            covid_data_recovered.append(covid_data_daily[i]["recovered"])

        covid_csv = []
        for i in range(0, len(covid_data_state)):
            data = Covid(covid_data_state[i], covid_data_statecode[i], covid_data_active[i], covid_data_confirmed[i], covid_data_deaths[i], covid_data_recovered[i])
            covid_csv.append(data)
        if save_data:
            file = open('State_Wise.csv', 'a')
            for team in covid_csv:
                file.write(str(team))


def main():
    data = fetchapidata()
    data.fetch(True)


if __name__ == '__main__':
    main()
