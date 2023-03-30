from tba_api import get_data
# import pandas
from pandas import DataFrame, concat

def get_cali_teams():
    team_df = DataFrame()
    # for x in range (1):
    for x in range (18):
        team_data_arr = get_data(f"/teams/2023/{x}/simple")
        team_df = concat([team_df, DataFrame(team_data_arr)])
    cali_team_nums = (team_df[team_df['state_prov'] == 'California']['team_number']).reset_index(drop=True)
    return cali_team_nums    

def get_outside_cali_events(year : int):
    cali_teams = get_cali_teams()
    all_events = DataFrame()
    for team in cali_teams:
        events = DataFrame(get_data(f'/team/frc{team}/events/{year}/simple'))
        events['team'] = team
        all_events = concat([all_events, events])
    all_events = all_events[(all_events['key'] != f'{year}cmptx')].reset_index(drop=True)
    print(f'california teams are playing {len(all_events)} plays')
    outside_cali_events = all_events[all_events['state_prov'] != 'CA'][['team', 'name', 'state_prov']].reset_index(drop=True)
    print(f'california teams are playing {len(outside_cali_events)} plays out of state')

def get_num_cali_plays(year : int):
    all_events = get_data(f'/events/{year}/keys')
    cali_events = list(filter(lambda x: x.startswith(f'{year}ca'),  all_events))
    print (cali_events)
    num_teams = 0
    for ev in cali_events:
        event_data = get_data(f'/event/{ev}/teams/keys')
        num_teams += len(event_data)
    print(f'{num_teams} plays available in california')

get_outside_cali_events(2023)
get_num_cali_plays(2023)
print('------')
get_outside_cali_events(2019)
get_num_cali_plays(2019)

