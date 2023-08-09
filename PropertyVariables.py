from pydantic import BaseModel, StrictFloat, StrictInt

class PropertyPricePrediction(BaseModel):
    Property_Type: StrictInt
    Club_House: StrictInt
    School_University_In_Township: StrictInt
    Hospital_In_Township: StrictInt
    Mall_In_Township: StrictInt
    Park_Jogging_Track: StrictInt
    Swimming_Pool: StrictInt
    Gym: StrictInt
    Property_Area_in_SqFt: StrictFloat
    Price_By_SubArea: StrictFloat
    Amenities_Score: StrictInt
    Price_By_Amenities_Score: StrictFloat
    Noun_Counts: StrictInt
    Verb_Counts: StrictInt
    Adjective_Counts: StrictInt
    boasts_elegant: StrictInt
    elegant_towers: StrictInt
    every_day: StrictInt
    great_community: StrictInt
    mantra_gold: StrictInt
    offering_bedroom: StrictInt
    quality_specification: StrictInt
    stories_offering: StrictInt
    towers_stories: StrictInt
    world_class: StrictInt    