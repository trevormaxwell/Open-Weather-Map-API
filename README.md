# Collecting Current Weather Data via OpenWeatherMap API
## Introduction
This program connects to the OpenWeatherMap API to gather the current weather of the inputted location.

## Configuration
An API key for OpenWeatherMap will be needed to connect to the API.
This key needs to be inputted in the program at lines 16, 55, 94, and 132:
  - **"api_key = 'your_API_key_here'"**

## Input
When the program is ran, it will take an input to specify the method of how the data will be collected for the location:
- type *city* to collect current weather based on city and state.
- type *zip* to collect current weather based on zip code.
- type *quit* to quit the program.

After the specification is inputted, the units must be specified for the output:
 - type *F* for units in Fahrenheit.
 - type *C* for units in Celsius.
 - type *K* for units in Kelvin.
 - type *quit* to quit the program.

After the units are specified, the city/state or zip code is needed to collect the current weather data for that location:
 - if *zip* was entered:
   - enter zip code, e.g. **19103**
   - or type *quit* to quit the program.
 - if *city* was entered:
   - enter city name when prompted, e.g. **Philadelphia**
   - or type *quit* to quit the program.
   - enter state abbreviation when prompted, e.g. **PA**
   - or type *quit* to quit the program.

## Output
After the input prompts are specified, the following weather data is pulled from the API:
 - Current weather, e.g. overcast clouds
 - Current temperature, e.g. 62 &deg;F
 - Feels like, e.g. 60 &deg;F
 - Minimum temperature, e.g. 52 &deg;F
 - Maximum temperature, e.g. 66 &deg;F
 - Humidity, e.g. 83%
 - Pressure, e.g. 1013 hPa

After the output is generated:
 - type *Y* to generate another weather report.
 - type *N* to exit.
