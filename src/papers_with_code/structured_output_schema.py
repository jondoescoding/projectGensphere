# advanced_search_schemas.py



from pydantic import BaseModel, Field

from typing import List



class ResearchPaper(BaseModel):
    paper_title: str = Field(..., description="The name of the research paper")
    
    release_date: str = Field(..., description="The date when the research paper was released")
    
    url: str = Field(..., description="The url link of the research paper")
    
    author: str = Field(..., description="The individual/group who wrote the research paper") 



class ResearchPaperList(BaseModel):

    information_list:List[ResearchPaper]