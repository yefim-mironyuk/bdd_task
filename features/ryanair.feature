Feature: Flights

    Background:
        Given Ryanair home page is displayed

    Scenario Outline: Verify Guest can see valid Flight page
        When Guest searches flight from "<Departure Location>" to "<Destination Location>" in next dates: departure - "21 Dec 2021", return - "23 Dec 2021"
        Then Guest should see flights from "<Departure Location>" to "<Destination Location>" on "21 Dec 2021" and back on on "23 Dec 2021"
        Examples:
            | Departure Location | Destination Location |
            | Aalborg            | Stockholm Arlanda    |
            | Tel Aviv           | Krakow               |