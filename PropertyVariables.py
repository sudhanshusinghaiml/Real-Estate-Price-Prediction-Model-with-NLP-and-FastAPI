from pydantic import BaseModel, StrictFloat

class PropertyPricePrediction(BaseModel):
    Property_Type: StrictFloat
    Club_House: StrictFloat
    School_University_In_Township: StrictFloat
    Hospital_In_Township: StrictFloat
    Mall_In_Township: StrictFloat
    Park_Jogging_Track: StrictFloat
    Swimming_Pool: StrictFloat
    Gym: StrictFloat
    Property_Area_in_SqFt: StrictFloat
    Price_By_SubArea: StrictFloat
    Amenities_Score: StrictFloat
    Price_By_Amenities_Score: StrictFloat
    Noun_Counts: StrictFloat
    Verb_Counts: StrictFloat
    Adjective_Counts: StrictFloat
    boasts_elegant: StrictFloat
    elegant_towers: StrictFloat
    every_day: StrictFloat
    great_community: StrictFloat
    mantra_gold: StrictFloat
    offering_bedroom: StrictFloat
    quality_specification: StrictFloat
    stories_offering: StrictFloat
    towers_stories: StrictFloat
    world_class: StrictFloat    