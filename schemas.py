from pydantic import BaseModel, Field, field_validator
from typing import Literal
from predictor import valid_crops, valid_states

class CropData(BaseModel):

    crop: str = Field(..., description='Enter the Crop name')
    state: str = Field(..., description='Enter the State name')
    season: Literal['Kharif', 'Rabi', 'Summer', 'Whole Year'] = Field(..., description = 'Kharif, Rabi, Summer, Whole Year')
    year: int = Field(..., ge = 1997, description ='Current Year' )
    area: float = Field(..., gt = 0, description ='Enter the area in hectres')
    rainfall: float = Field(..., gt = 0, description ='Enter the avg rainfall in mm')
    pesticide: float = Field(..., gt = 0, description = 'Enter the pesticides used in kgs')
    fertilizer: float = Field(..., gt = 0, description = 'Enter the fertilizers used in kg')

    @field_validator('crop')
    @classmethod
    def validate_crop(cls, value):
        if value in valid_crops:
            return value
        else:
            raise ValueError ('Crop InValid!!')
        
    @field_validator('state')
    @classmethod
    def validate_state(cls, value):
        if value in valid_states:
            return value
        else:
            raise ValueError ('State InValid!!')



class PredictedData(BaseModel):
    predicted_yield:float
    total_production:float
    total_quintals:float
