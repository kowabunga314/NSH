from clients.neows import NeoWs


class AsteroidApi():
    """
    The AsteroidAPI class consumes the NeoWs API and processes
        the raw data that is retrieved. It uses this raw data to
        provide interesting summaries.
    """

    def get_closest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        closest_approach = dict(day=None, distance=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                distance = approach['close_approach_data'][0]['miss_distance']['kilometers']
                # Compare this approach to current closest approach
                if closest_approach['distance'] is None or distance > closest_approach['distance']:
                    closest_approach = dict(day=day, distance=distance, pos=i)
        
        # Return approach
        return data['near_earth_objects'][closest_approach['day']][closest_approach['pos']]

    def get_largest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        largest_encounter = dict(day=None, size=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                size = (
                    approach['estimated_diameter']['kilometers']['estimated_diameter_min']
                    + approach['estimated_diameter']['kilometers']['estimated_diameter_max']
                ) / 2
                # Compare this approach to current closest approach
                if largest_encounter['size'] is None or size > largest_encounter['size']:
                    largest_encounter = dict(day=day, size=size, pos=i)
        
        # Return approach
        return data['near_earth_objects'][largest_encounter['day']][largest_encounter['pos']]

    def get_fastest_approach(self):
        n = NeoWs()
        this_week = n.get_approaches_by_date()
        data = this_week.get('data')

        # Initialize closest approach tracker
        fastest_encounter = dict(day=None, r_vel=None, pos=-1)

        # Data is grouped by day, iterate over each day
        for day in data['near_earth_objects']:
            # Day contains list of approaches, iterate over each approach
            for i, approach in enumerate(data['near_earth_objects'][day]):
                # Get distance of this approach
                r_vel = approach['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
                # Compare this approach to current closest approach
                if fastest_encounter['r_vel'] is None or r_vel > fastest_encounter['r_vel']:
                    fastest_encounter = dict(day=day, r_vel=r_vel, pos=i)

        # Return approach
        return data['near_earth_objects'][fastest_encounter['day']][fastest_encounter['pos']]
