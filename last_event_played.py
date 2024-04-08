from tba_api import get_data
from pandas import DataFrame, concat

def get_cali_teams(year: int):
    team_df = DataFrame()
    # for x in range (1):
    for x in range (33):
        team_data_arr = get_data(f"/teams/{year}/{x}/simple")
        team_df = concat([team_df, DataFrame(team_data_arr)])
    # cali_team_nums = (team_df[team_df['state_prov'] == 'California']['team_number']).reset_index(drop=True)
    # return cali_team_nums    