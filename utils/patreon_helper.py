import patreon
from utils.patreon_info import (
    CREATOR_ID, TIER_IDS, CAMPAIGN_ID, PAGE_SIZE,
)

def get_supporter_name(pledge, pledges_response):
    reward = pledge.relationship('reward')
    if reward.id() in TIER_IDS:
        patron = pledge.relationship('patron')
        patron_id = patron.id()
        user = pledges_response.find_resource_by_type_and_id('user', patron_id)
        return user.attribute('full_name')