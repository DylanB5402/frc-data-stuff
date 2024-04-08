from tba_api import get_data
from pandas import DataFrame, concat

def get_cali_teams(year: int):
    team_df = DataFrame()
    # for x in range (1):
    for x in range (33):
        team_data_arr = get_data(f"/teams/{year}/{x}/simple")
        team_df = concat([team_df, DataFrame(team_data_arr)])
    cali_team_nums = (team_df[team_df['state_prov'] == 'California']['team_number']).reset_index(drop=True)
    return cali_team_nums    

def get_outside_cali_events(year : int):
    cali_teams = get_cali_teams(year)
    all_events = DataFrame()
    for team in cali_teams:
        events = DataFrame(get_data(f'/team/frc{team}/events/{year}/simple'))
        events['team'] = team
        all_events = concat([all_events, events])
    all_events = all_events[(all_events['key'] != f'{year}cmptx') & all_events['event_type'] == 0].reset_index(drop=True)
    print(f'california teams are playing {len(all_events)} plays')
    outside_cali_events = all_events[all_events['state_prov'] != 'CA'][['team', 'name', 'state_prov']].reset_index(drop=True)
    print(f'california teams are playing {len(outside_cali_events)} plays out of state')

def get_num_cali_plays(year : int):
    all_events = get_data(f'/events/{year}/simple')
    # print(all_events[0])
    cali_events = list(filter(lambda x: (x['key'].startswith(f'{year}ca') and x['event_type'] == 0),  all_events))
    num_teams = 0
    num_outside_teams = 0
    calif_teams = set()
    for ev in cali_events:
        ev_key = ev['key']
        event_data = get_data(f'/event/{ev_key}/teams/simple')
        for team in event_data:
            if (team['state_prov'] != "California"):
                # print(ev_key, team['key'])
                num_outside_teams += 1
            else:
                calif_teams.add(team['key'])
        num_teams += len(event_data)
    print(f'{num_teams} plays available in california')
    print(f'out of state teams are playing {num_outside_teams} plays in california')
    print(f'{len(calif_teams)} teams in california')

# years = [2018, 2019, 2022, 2023, 2024]
years = [2024]

for year in years:
    print(f'{year}:')
    get_num_cali_plays(year)
    get_outside_cali_events(year)
# print('------')
# get_outside_cali_events(2019)
# get_num_cali_plays(2019)

