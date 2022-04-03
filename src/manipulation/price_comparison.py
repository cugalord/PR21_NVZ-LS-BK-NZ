"""
Module that contains functions used to answer the first question of this project, which is
analyzing and comparing prices of different energy sources.
"""

from setup import data_extraction as de

household_prices = de.read(
    '../data/Cene el. energije za gospodinjske odjemalce.csv')
nonhousehold_prices = de.read(
    '../data/Cene el. energije za negospodinjske odjemalce.csv')

# Compare prices between different user groups in different years.
# Compare prices between different seasons.
# Compare prices between household and nonhousehold users.
# Analysis of taxes on energy prices.
