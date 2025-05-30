#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 18:45:12 2025

@author: kavyadeepak
"""

from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import pandas as pd
import os

os.environ["PANDASAI_API_KEY"] = "your_openai_key"  # or use dotenv

def chat_with_data(df, query):
    llm = OpenAI(api_token=os.getenv("PANDASAI_API_KEY"))
    sdf = SmartDataframe(df, config={"llm": llm})
    return sdf.chat(query)