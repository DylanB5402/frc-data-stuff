from tba_api import get_data

if __name__ == "__main__":
    states = {}
    for x in range (18):
        team_data = get_data(f"/teams/2023/{x}/simple")
        for data in team_data:
            st = data['state_prov']
            if (st in states):
                states[st] += 1
            else:
                states[st] = 0
    print(states)

