# coolingTower
The repository calculates the thermodynamic proparties and flowrates of a given packed cooling tower. The equations governing the mass and heat flow of a given counter-flow, wet cooling tower are Ordinary Differential Equations with unknown boundary conditions on both sides of the cooling tower. The maximum and minimum of these boundary conditions are guessed which is followed with a binary search with which the program determines the outflow of water and the influx of air which will satisfy the problem determined by the governing differental equations. For determinding the annually evaporated water the relevant wheahter data is also required. For scraping the relevant wheather data a script was written using Beautiful Soup as well. 

The construction of the program calculating and validating the program for calculating the thermodynamic properties of the wet cooling tower was done according the following publications:

1. Kloppers JC. A critical evalutaion and refinement of the performance prediction of wet-cooling towers. 2003;(December).
2. Klimanek A. Numerical Modelling of Natural Draft Wet-Cooling Towers. Arch Comput Methods Eng. 2013;20(1):61-109. doi:10.1007/s11831-013-9081-9
