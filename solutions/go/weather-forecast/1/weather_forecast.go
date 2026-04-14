// Package weather provides tools that forecast
// the current weather conditions of cities in
// Globinocus.
package weather

var (
    // CurrentCondition stores the current weather
    // condition of any city whose weather is  being
    // forecasted.
	CurrentCondition string
    // CurrentLocation stores the location of a city
    // you want to forecast.
	CurrentLocation  string
)

// Forecast returns the current weather condition for
// any specified Globinocus city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
