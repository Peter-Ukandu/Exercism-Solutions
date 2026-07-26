package leap

is_leap_year :: proc(year: int) -> bool {
	if year % 100 == 0 {
        if year % 400 == 0 {
            return true
        }
    } else if year % 4 == 0 {
        return true
    }
	return false
}
