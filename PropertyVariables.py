from pydantic import BaseModel, StrictFloat, StrictInt

class PropertyPricePrediction(BaseModel):
    Property_Type: StrictInt = 1
    Club_House: StrictInt = 1
    School_University_In_Township: StrictInt = 1
    Hospital_In_Township: StrictInt = 1
    Mall_In_Township: StrictInt = 1
    Park_Jogging_Track: StrictInt = 1
    Swimming_Pool: StrictInt = 1
    Gym: StrictInt = 1
    Property_Area_in_SqFt: StrictFloat = 2027.85
    Price_By_SubArea: StrictFloat = 0.0
    Amenities_Score: StrictInt = 7
    Price_By_Amenities_Score: StrictFloat = 0.0
    Noun_Counts: StrictInt = 0
    Verb_Counts: StrictInt = 0
    Adjective_Counts: StrictInt = 0
    boasts_elegant: StrictInt = 1
    elegant_towers: StrictInt = 0
    every_day: StrictInt = 0
    great_community: StrictInt = 0
    mantra_gold: StrictInt = 1
    offering_bedroom: StrictInt = 0
    quality_specification: StrictInt = 0
    stories_offering: StrictInt = 0
    towers_stories: StrictInt = 0
    world_class: StrictInt = 1