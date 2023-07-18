# FootballLeagueTable
My own Football standings table for the Premier League where I fill it from all the fixtures mixing Python and Excel

Last year I created a Spreadsheet to follow up the Premier League season, so I design a few sheets for the purpose, one for the standings where I will collect the data from the fixtures along the season.
Another sheet will have the standings sorted by the points and goal average.
I included one more with all the fixtures in order to use this data with formulas to fill up the standings table.

Week after week I typed the results manually, and this year, for the upcoming season I decided to automatize some things, so some parts previously done with Excel, I will do them with Python instead.
I am currently implementing these upgrades in order to have all set and ready for the opening day of the 23/24 season.

I will attach the last year excel file in case someone is interested on the process, the file has some sheets with raw data and tests I´ve been doing along the year, sorry if it´s a mess.
The next couple wweks I will update the repository with the Python addings.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


I uploaded the jupyter notebook file where I am doing tests with python to upgrade the excel.
I am scrapping the worldoffootball.net web to get all the matchweeks and the fixtures and append them to a dataframe.
Then I am reshaping and adapting it to my purpose and then the final step is to add it to a sheet in the Excel book but still working on it,
with all this I wouldnt need to type the results so I will fill them automatically just refreshing the date in the Excel sheets.
