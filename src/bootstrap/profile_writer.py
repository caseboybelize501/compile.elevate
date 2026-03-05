import json
import os

class ProfileWriter:
    def __init__(self):
        self.profile_file = "system_profile.json"

    async def write(self, profile):
        try:
            with open(self.profile_file, 'w') as f:
                json.dump(profile, f, indent=2)
            print(f"Profile written to {self.profile_file}")
        except Exception as e:
            print(f"Error writing profile: {e}")
